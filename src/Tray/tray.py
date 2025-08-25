"""
`tray.py`  - **托盘模块** 
1. 托盘图标：创建和管理系统托盘图标
2. 上下文菜单：定义托盘图标的右键菜单
3. 事件处理：处理托盘图标的各种事件
"""
from win11toast import toast

def show_notification(text, title="SoulSpark"):
    lines = text.splitlines()
    max_lines = 4
    display_text = "\n".join(lines[:max_lines])
    toast(title, display_text)
