"""
`ui_display.py`  - **UI模块** 
1. 中间展示区：创建和管理中间展示区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
from src.config import STYLE_CONTENT_FONT,QUOTE_FILE
from src.Words import random_choice



def create_display_frame(parent):
    """
    - 名称: 中间展示区
    - 功能: 创建并管理中间展示区
    - 参数: parent - CTk实例
    - 返回: 无
    """
    display_frame = ctk.CTkFrame(parent)
    display_frame.pack(expand=True, fill="both", padx=10, pady=10)

    init_text = random_choice(QUOTE_FILE)

    display_label = ctk.CTkLabel(
        display_frame,
        text=init_text,
        font=STYLE_CONTENT_FONT,
        wraplength=660,
        justify="left"  
    )
    display_label.place(relx=0.02, rely=0.02, anchor="nw")
