"""
`ui_display.py`  - **UI模块** 
1. 中间展示区：创建和管理中间展示区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
import random
from src.config import STYLE_CONTENT_FONT


def create_display_frame(parent):
    """
    - 名称: 中间展示区
    - 功能: 创建并管理中间展示区
    - 参数: parent - CTk实例
    - 返回: 无
    """
    display_frame = ctk.CTkFrame(parent)
    display_frame.pack(expand=True, fill="both", padx=30, pady=10)

    display_label = ctk.CTkLabel(
        display_frame,
        text="展示",
        font=STYLE_CONTENT_FONT
    )
    display_label.place(relx=0.5, rely=0.5, anchor="center")


def update_display(label):
    """
    - 功能: 更新中间展示区显示内容
    - 参数:
        label - CTkLabel 实例
    """
    if not words_list:
        label.config(text="没有语录可显示")
        return

    word = random.choice(words_list)
    label.config(text=word)

