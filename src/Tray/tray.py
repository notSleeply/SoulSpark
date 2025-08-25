"""
`tray.py`  - **托盘模块** 
1. 托盘图标：创建和管理系统托盘图标
2. 上下文菜单：定义托盘图标的右键菜单
3. 事件处理：处理托盘图标的各种事件
"""

import time
from win11toast import toast

def show_notification(text, title="SoulSpark"):
    lines = text.splitlines()
    max_lines = 4
    total_pages = (len(lines) + max_lines - 1) // max_lines

    for i in range(total_pages):
        start = i * max_lines
        end = start + max_lines
        display_text = "\n".join(lines[start:end])
        page_title = f"{title} ({i+1}/{total_pages})" if total_pages > 1 else title
        toast(page_title, display_text)
        if i < total_pages - 1:
            time.sleep(1.5)
