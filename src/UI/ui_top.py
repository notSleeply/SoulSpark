"""
`ui_top.py`  - **UI模块** 
1. 顶部按钮区：创建和管理顶部按钮区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""

import customtkinter as ctk
from src.config import STYLE_BUTTON_FONT


def top_show_button(parent):
    """
    - 名称: 展示按钮
    - 功能: 创建并管理“展示”按钮
    - 参数: parent - 按钮所在的父容器
    - 返回: CTkButton 实例
    """
    btn_show = ctk.CTkButton(
        parent,
        text="展示",
        font=STYLE_BUTTON_FONT,
        width=120,
        height=40,
        command=lambda: print("展示 clicked")
    )
    btn_show.pack(side="left", expand=True, fill="x", padx=(30, 5), pady=5)
    return btn_show


def top_add_button(parent):
    """
    - 名称: 添加按钮
    - 功能: 创建并管理“添加”按钮
    - 参数: parent - 按钮所在的父容器
    - 返回: CTkButton 实例
    """
    btn_add = ctk.CTkButton(
        parent,
        text="添加",
        font=STYLE_BUTTON_FONT,
        width=120,
        height=40,
        command=lambda: print("添加 clicked")
    )
    btn_add.pack(side="right", expand=True, fill="x", padx=(5, 30), pady=5)
    return btn_add


def top_frame(parent):
    """
    - 名称: 顶部按钮区
    - 功能: 创建并管理顶部按钮区
    - 参数: parent - CTk实例
    - 返回: 无
    """
    top_frame = ctk.CTkFrame(parent, fg_color="transparent")
    top_frame.pack(side="top", fill="x", pady=10)

    top_show_button(top_frame)
    top_add_button(top_frame)
