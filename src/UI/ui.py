"""
`ui.py` - **UI模块**
1. 主窗口：创建和管理主应用窗口
2. 组件：定义和管理UI组件
3. 事件：处理用户交互和事件
"""

import customtkinter as ctk
from src.config import NAME, GEOMETRY, STYLE_COLOR, STYLE_MODE
from src.UI.ui_top import top_frame
from src.UI.ui_bottom import bottom_frame
from src.UI.ui_display import display_frame
from src.UI.ui_state import UIState

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

    ui_state = UIState(root)

    top_frame(root, on_add_click=ui_state.on_add_click,
              on_show_click=ui_state.on_show_click)
    display_textbox = display_frame(root)
    btn_random = bottom_frame(root)

    ui_state.set_components(display_textbox, btn_random)

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

