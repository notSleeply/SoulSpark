"""
`ui.py` - **UI模块**
1. 主窗口：创建和管理主应用窗口
2. 组件：定义和管理UI组件
3. 事件：处理用户交互和事件
"""

import customtkinter as ctk
from src.config import NAME, GEOMETRY, STYLE_COLOR, STYLE_MODE
from src.UI.ui_top import create_top_frame
from src.UI.ui_bottom import create_bottom_frame
from src.UI.ui_display import create_display_frame

def main_window():
    """
    - 名称: 主窗口
    - 功能: 创建并显示主应用窗口
    - 参数: 无
    - 返回: 无
    """
    ctk.set_appearance_mode(STYLE_MODE)
    ctk.set_default_color_theme(STYLE_COLOR)

    root = ctk.CTk()
    config_frame(root)
    create_top_frame(root)
    display_textbox = create_display_frame(root)
    create_bottom_frame(root, display_textbox)

    root.mainloop()


def config_frame(root):
    """
    - 名称: root配置
    - 功能: 管理CTk实例配置区
    - 参数: root - CTk实例
    - 返回: 无
    """
    root.title(NAME)
    root.geometry(GEOMETRY)
    root.resizable(False, False)

