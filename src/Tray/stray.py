from pystray import Icon, Menu, MenuItem
from PIL import Image
from src.config import ICON_FILE
import threading
import sys
import os


_main_window = None

def on_quit(icon, item):
    icon.stop()
    if _main_window:
        _main_window.destroy() 
    sys.exit(0)


def on_show(icon, item):
    if _main_window:
        _main_window.deiconify()
        _main_window.after(0, _main_window.lift) 
    else:
        print("主窗口对象未设置，无法显示。")


def set_main_window(window):
    global _main_window
    _main_window = window


def create_tray_icon():
    icon_path = os.path.abspath(ICON_FILE)
    image = Image.open(icon_path)

    menu = Menu(
        MenuItem('显示主窗口', on_show),
        MenuItem('退出', on_quit)
    )

    icon = Icon("SoulSpark", image, "SoulSpark", menu)
    # 用线程启动，避免阻塞主线程
    threading.Thread(target=icon.run, daemon=True).start()
    return icon
