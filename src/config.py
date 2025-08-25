"""
`config.py`  - **配置中心** 
1. 路径参数：定义文件路径和名称
2. 软件参数：定义软件名称和版本
3. 通知参数：定义通知相关的设置
"""

# ========== 路径参数 ========== #
QUOTE_FILE = "Bible.txt"
"""默认语录存储文件"""
ICON_FILE = "../icon.ico"
"""托盘图标文件路径"""

# ========== 软件参数 ========== #
NAME = "SoulSpark"
"""软件名称"""
VERSION = "1.0.0"
"""软件版本"""


# ========== 样式参数 ========== #
GEOMETRY = "720x480"
"""窗口大小"""
STYLE_BUTTON_FONT = ("微软雅黑", 14)
"""默认按钮字体样式"""
STYLE_CONTENT_FONT = ("微软雅黑", 22)
"""默认内容字体样式"""
STYLE_MODE = "system"
"""默认主题模式，可选: "light", "dark", "system" """
STYLE_COLOR = "blue"
"""默认主题颜色，可选: "green", "dark-blue", 自定义json"""

# ========== 通知参数 ========== #
TIME_SHOW = 300
"""随机时间"""