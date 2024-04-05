""" Logging helper functions """
import datetime
import logging
import queue

from .utils import LOG_DIR, sub_file

DEFAULT_LOGGER_NAME = 'majsoul_copilot'
LOGGER = logging.getLogger(DEFAULT_LOGGER_NAME)
LOG_FILE_NAME:str = None

def config_logging(file_prefix:str=DEFAULT_LOGGER_NAME, console=True, file=True):
    """ Initialize logging format/output. Run once.
    params:
        file_prefix(str): prefix of the log file name
        console (bool): if output to console
        file (bool): if output to file
    """
    global LOG_FILE_NAME

    logger = LOGGER
    logger.setLevel(logging.DEBUG)
    formatter = log_formatter()
    
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    if file:
        file_name = file_prefix + '_' + dt_string() + '.log'
        LOG_FILE_NAME = sub_file(LOG_DIR, file_name)
        file_handler = logging.FileHandler(LOG_FILE_NAME, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

def log_formatter() -> str:
    """ return the default log formatter"""
    return logging.Formatter('%(asctime)s %(levelname)s [%(threadName)s]%(filename)s:%(lineno)d | %(message)s')

def dt_string() -> str:
    """ return datetime string"""
    return datetime.datetime.now().strftime(r'%Y-%m-%d_%H-%M-%S')

class QueueHandler(logging.Handler):
    """ Log handler to send logging records to a thread-safe queue """
    def __init__(self, log_queue:queue.Queue):
        super().__init__()
        self.log_queue = log_queue 
        formatter = log_formatter()
        self.setLevel(logging.DEBUG)
        self.setFormatter(formatter)
        
    def emit(self, record):
        self.log_queue.put(record)