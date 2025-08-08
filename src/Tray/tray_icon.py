from pystray import Icon, MenuItem, Menu
from PIL import Image
from tkinter import messagebox
import sys
from src.Config import *

# 全局变量
icon = None

# ========== 系统托盘功能 ========== #
def create_tray_icon():
    global icon
    try:
        icon_image = Image.open(ICON_FILE)  # 加载托盘图标
        
        # 延迟导入避免循环导入
        from src.UI import toggle_window, quit_app
        
        icon = Icon(
            "励志话语", icon=icon_image,
            menu=Menu(
                MenuItem("切换", toggle_window, default=True, visible=False),
                MenuItem("退出", quit_app)
            )
        )
        icon.run_detached()  # 运行托盘图标
        icon.visible = True
    except Exception as e:
        messagebox.showerror("错误", f"加载托盘图标失败: {e}")
        sys.exit()

# ========== 停止托盘图标 ========== #
def stop_tray_icon():
    global icon
    if icon:
        icon.stop()  # 停止托盘图标

# ========== 获取托盘图标对象 ========== #
def get_icon():
    return icon
