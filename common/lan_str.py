# Language string constants
from .utils import VER_NUMBER

class LanStr:
    """ String constants for default language (English) """
    LANGUAGE_NAME = 'English'

    # GUI
    APP_TITLE = 'Mahjong Copilot'
    START_BROWSER = "Start Web Client"
    WEB_OVERLAY = "Overlay"
    AUTOPLAY = "Autoplay"
    OPEN_LOG_FILE = "Open Log File"
    SETTINGS = "Settings"
    HELP = "Help"
    EXIT = "Exit"
    EIXT_CONFIRM = "Are you sure you want to exit?"
    AI_OUTPUT = 'AI Guidance'
    GAME_INFO = 'Game Info'
    HELP_STR = f"""Mahjong Copilot v{VER_NUMBER}

A Mahjong AI assistant for Majsoul, based on Mortal Mahjong AI. Currently the model only supports 4-person Mahjong game. When you enter a game in Majsoul, AI will give you step-by-step guidance.

🔳 Start Web Client: Start the game in browser with AI assistant. This program uses built-in Chromium browser. First time entering Majsoul will take a while to download game assets.
🔘 Web Overlay: Show/Hide the AI Guidance overlayed on Web Page.
🔘 Autoplay: Enable/Disable Autoplay. Autoplay clicks on the browser according to AI guidance.
🔘 Autojoin: Auto join next game given settings.
🔳 Settings: View and configure settings.
🔳 Open Log File: Open the log file with system default program.
    
Github: https://github.com/latorc/MahjongCopilot
    
Credits:
Mortal: https://github.com/Equim-chan/Mortal
Akagi: https://github.com/shinkuan/Akagi
MJAI: https://mjai.app
"""
    ON = "On"
    OFF = "Off"
    DOWNLOAD_UPDATE = "Download Update"
    START_UPDATE = "Update & Restart"
    CHECK_FOR_UPDATE = "Check Update"
    CHECKING_UPDATE = "Checking for new update..."
    UPDATE_AVAILABLE = "New update available"
    NO_UPDATE_FOUND = "No new update found"
    DOWNLOADING = "Downloading..."
    UNZIPPING = "Unzipping..."
    UPDATE_PREPARED = "Update prepared. Click the button to update and restart."

    # Settings
    SAVE = "Save"
    CANCEL = "Cancel"
    SETTINGS_TIPS = "A restart is needed to apply some settings"
    AUTO_LAUNCH_BROWSER = "Auto Launch Browser"
    MITM_PORT = "MITM Server Port"
    BROWSER_WIDTH = "Web Client Width"
    BROWSER_HEIGHT = "Web Client Height"
    CLIENT_SIZE = "Web Client Size"
    MAJSOUL_URL = "Majsoul URL"
    LANGUAGE = "Language"
    MODEL_TYPE = "AI Model Type"
    AI_MODEL_FILE = "Local Model File"
    MJAPI_URL = "MJAPI URL"
    MJAPI_USER = "MJAPI User"
    MJAPI_SECRET = "MJAPI Secret"
    MJAPI_MODEL_SELECT = "MJAPI Model Select"
    LOGIN_TO_REFRESH = "Log in to refresh"
    MITM_PORT_ERROR_PROMPT = "Invalid MITM Port (must between 1000~65535)"
    AUTO_PLAY_SETTINGS = "Autoplay Settings"
    RANDOM_DELAY_RANGE = "Base Delay Range (sec)"
    AUTO_JOIN_GAME = "Auto Join"
    GAME_LEVELS = ["Bronze", "Silver", "Gold", "Jade", "Throne"]
    GAME_MODES = ["4-p East","4-p South","3-p East","3-p South"]
    MOUSE_RANDOM_MOVES = "Random Moves"
    
    # Status
    MAIN_THREAD  = "Main Thread"
    MITM_SERVICE = "MITM Service"
    BROWSER = "Browser"
    GAME_RUNNING = "Game Running"
    GAME_ERROR = "Game Error!"
    MODEL_FILE_ERROR = "Model File not Found!"
    MITM_SERVER_ERROR = "MITM Service Error!"
    MAIN_THREAD_ERROR = "Main Thread Error!"
    SYNCING = "Syncing..."
    CALCULATING = "Calculating..."
    READY_FOR_GAME = "Ready"
    GAME_STARTING = "Game Starting"
    KYOKU = "Kyoku"
    HONBA = "Honba"
    MODEL = "Model"
    AWAIT_BOT = "Model not loaded"
    MAIN_MENU = "Main Menu"
    GAME_ENDING = "Game Ending"
    GAME_NOT_RUNNING = "Game Not Launched"
    
    # Reaction/Actions
    PASS = "Skip"
    DISCARD = "Discard"
    CHI = "Chi"
    PON = "Pon"
    KAN = "Kan"
    KAKAN = "Kakan"
    DAIMINKAN = "Daiminkan"
    ANKAN = "Ankan"
    RIICHI = "Riichi"
    AGARI = "Agari"
    TSUMO = "Tsumo"
    RON = "Ron"
    RYUKYOKU = "Ryukyoku"
    NUKIDORA = "Nukidora"
    OPTIONS_TITLE = "Options:"    
    
    MJAI_2_STR = {
        '1m': '1 Man', '2m': '2 Man', '3m': '3 Man', '4m': '4 Man', '5m': '5 Man',
        '6m': '6 Man', '7m': '7 Man', '8m': '8 Man', '9m': '9 Man',
        '1p': '1 Pin', '2p': '2 Pin', '3p': '3 Pin', '4p': '4 Pin', '5p': '5 Pin',
        '6p': '6 Pin', '7p': '7 Pin', '8p': '8 Pin', '9p': '9 Pin',
        '1s': '1 Sou', '2s': '2 Sou', '3s': '3 Sou', '4s': '4 Sou', '5s': '5 Sou',
        '6s': '6 Sou', '7s': '7 Sou', '8s': '8 Sou', '9s': '9 Sou',
        'E': 'East', 'S': 'South', 'W': 'West', 'N': 'North',
        'C': 'Chun', 'F': 'Hatsu', 'P': 'Haku',
        '5mr': 'Red 5 Man', '5pr': 'Red 5 Pin', '5sr': 'Red 5 Sou',
        'reach': 'Riichi', 'chi_low': 'Chi Low', 'chi_mid': 'Chi Mid', 'chi_high': 'Chi High', 'pon': 'Pon', 'kan_select':'Kan',
        'hora': 'Agari', 'ryukyoku': 'Ryukyoku', 'none':'Skip'
    }
      
    def mjai2str(self, mjai_option:str) -> str:
        """ convert mjai option/tile to string in this language"""    
        if mjai_option not in self.MJAI_2_STR:
            return mjai_option        
        return self.MJAI_2_STR[mjai_option]
    

class LanStrZHS(LanStr):
    """ String constants for Chinese Simplified"""
    LANGUAGE_NAME = '简体中文'
    
    # GUI
    APP_TITLE = '麻将 Copilot'
    START_BROWSER = "启动网页客户端"
    WEB_OVERLAY = "网页 HUD"
    AUTOPLAY = "自动打牌"
    OPEN_LOG_FILE = "打开日志文件"
    SETTINGS = "设置"
    HELP = "帮助"
    EXIT = "退出"
    EIXT_CONFIRM = "确定退出程序?"
    AI_OUTPUT = 'AI 提示'
    GAME_INFO = '游戏信息'
    HELP_STR = f"""麻将 Copilot v{VER_NUMBER}

一款雀魂麻将 AI 助手, 基于 Mortal 麻将 AI。 目前模型只支持四人麻将游戏。 当你进入游戏后, AI会对每一步行动进行指导。
    
🔳 启动网页客户端: 在浏览器中启动游戏和AI助手。 本程序使用自带的 Chromium 浏览器。 首次进入雀魂时, 会因为下载游戏资源而耗时较长。
🔘 网页 Hud: 显示/隐藏网页中覆盖显示的 AI 指导信息。
🔘 自动打牌: 打开/关闭自动打牌, 自动点击浏览器根据 AI 提示打牌。
🔘 自动加入: 根据设置的条件, 自动加入下一局游戏
🔳 设置: 查看和修改设置选项。
🔳 打开日志文件: 用系统默认程序打开日志文件。
    
本项目 Github: https://github.com/latorc/MahjongCopilot
    
鸣谢:
Mortal: https://github.com/Equim-chan/Mortal
Akagi: https://github.com/shinkuan/Akagi
MJAI: https://mjai.app
"""
    ON = "开"
    OFF = "关"
    DOWNLOAD_UPDATE = "下载更新"
    START_UPDATE = "开始更新"
    UPDATE_AVAILABLE = "有新的更新可用"
    
    CHECK_FOR_UPDATE = "检查更新"
    CHECKING_UPDATE = "正在检查更新..."
    NO_UPDATE_FOUND = "未发现更新"
    UNZIPPING = "解压中..."
    DOWNLOADING = "下载中..."
    UPDATE_PREPARED = "更新已准备好。点击按钮更新并重启。"
    
    
    # Settings
    SAVE = "保存"
    CANCEL = "取消"
    SETTINGS_TIPS = "部分设置项重启后生效"
    MITM_PORT = "MITM 服务端口"
    BROWSER_WIDTH = "网页客户端宽度"
    BROWSER_HEIGHT = "网页客户端高度"
    CLIENT_SIZE = "网页客户端大小"
    MAJSOUL_URL = "雀魂网址"
    LANGUAGE = "语言" 
    MODEL_TYPE = "AI 模型类型"
    AI_MODEL_FILE = "本地 AI 模型文件"
    MJAPI_URL = "MJAPI 网址"
    MJAPI_USER = "MJAPI 用户名"
    MJAPI_SECRET = "MJAPI 秘密 Secret"
    MJAPI_MODEL_SELECT = "MJAPI 模型选择"
    LOGIN_TO_REFRESH = "登录后刷新"
    AUTO_LAUNCH_BROWSER = "自动启动浏览器"
    MITM_PORT_ERROR_PROMPT = "错误的 MITM 服务端口(必须是1000~65535)"
    AUTO_PLAY_SETTINGS = "自动打牌设置"
    AUTO_JOIN_GAME = "自动加入"
    RANDOM_DELAY_RANGE = "基础延迟随机范围(秒)"
    GAME_LEVELS = ["铜之间", "银之间", "金之间", "玉之间", "王座之间"]
    GAME_MODES = ["四人东","四人南","三人东","三人南"]
    MOUSE_RANDOM_MOVES = "鼠标随机移动次数"
    
    # Status
    MAIN_THREAD  = "主程序"
    MITM_SERVICE = "MITM 服务"
    BROWSER = "浏览器"
    GAME_RUNNING = "对局进行中"
    GAME_ERROR = "对局发生错误!"
    MODEL_FILE_ERROR = "无法找到模型文件!"
    MITM_SERVER_ERROR = "MITM 服务错误!"
    MAIN_THREAD_ERROR = "主进程发生错误!"
    SYNCING = "同步中…"
    CALCULATING = "计算中…"
    READY_FOR_GAME = "等待游戏"
    GAME_STARTING = "准备开始"
    KYOKU = "局"
    HONBA = "本场"
    MODEL = "模型"
    AWAIT_BOT = "模型未加载"
    MAIN_MENU = "游戏主菜单"
    GAME_ENDING = "游戏结束"
    GAME_NOT_RUNNING = "游戏未启动"
    
    # Reaction/Actions
    PASS = "跳过"
    DISCARD = "切"
    CHI = "吃"
    PON = "碰"
    KAN = "杠"
    KAKAN = "加杠"
    DAIMINKAN = "大明杠"
    ANKAN = "暗杠"
    RIICHI = "立直"
    AGARI = "和牌"
    TSUMO = "自摸"
    RON = "荣和"
    RYUKYOKU = "流局"
    NUKIDORA = "拔北"
    OPTIONS_TITLE = "候选项:"    
    
    MJAI_2_STR ={
        '1m': '一萬', '2m': '二萬', '3m': '三萬', '4m': '四萬', '5m': '伍萬',
        '6m': '六萬', '7m': '七萬', '8m': '八萬', '9m': '九萬',
        '1p': '一筒', '2p': '二筒', '3p': '三筒', '4p': '四筒', '5p': '伍筒',
        '6p': '六筒', '7p': '七筒', '8p': '八筒', '9p': '九筒',
        '1s': '一索', '2s': '二索', '3s': '三索', '4s': '四索', '5s': '伍索',
        '6s': '六索', '7s': '七索', '8s': '八索', '9s': '九索',
        'E': '東', 'S': '南', 'W': '西', 'N': '北',
        'C': '中', 'F': '發', 'P': '白',
        '5mr': '赤伍萬', '5pr': '赤伍筒', '5sr': '赤伍索', 
        'reach': '立直', 'chi_low': '吃-低', 'chi_mid': '吃-中', 'chi_high': '吃-高', 'pon': '碰', 'kan_select':'杠',
        'hora': '和牌', 'ryukyoku': '流局', 'none': '跳过'
    }



LAN_OPTIONS:dict[str, LanStr] = {
    'EN': LanStr(),
    'ZHS': LanStrZHS(), 
}
""" dict of {language code: LanString instance}"""