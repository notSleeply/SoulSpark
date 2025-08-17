"""
`ui_top.py`  - **UI模块** 
1. 顶部按钮区：创建和管理顶部按钮区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""

import customtkinter as ctk
from src.config import STYLE_BUTTON_FONT

def create_top_frame(parent):
    """
    - 名称: 顶部按钮区
    - 功能: 创建并管理顶部按钮区
    - 参数: parent - CTk实例
    - 返回: 无
    """
    top_frame = ctk.CTkFrame(parent, fg_color="transparent")
    top_frame.pack(side="top", fill="x", pady=10)

    btn_show = ctk.CTkButton(
        top_frame,
        text="展示",
        font=STYLE_BUTTON_FONT,
        width=120,
        height=40,
        command=lambda: print("展示 clicked")
    )
    btn_show.pack(side="left", expand=True, fill="x", padx=(30, 5), pady=5)

    btn_add = ctk.CTkButton(
        top_frame,
        text="添加",
        font=STYLE_BUTTON_FONT,
        width=120,
        height=40,
        command=lambda: print("添加 clicked")
    )
    btn_add.pack(side="right", expand=True, fill="x", padx=(5, 30), pady=5)
