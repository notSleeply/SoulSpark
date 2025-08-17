"""
`ui_display.py`  - **UI模块** 
1. 中间展示区：创建和管理中间展示区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
import random
from src.config import STYLE_CONTENT_FONT,QUOTE_FILE
from src.Words import read_words_from_file



def create_display_frame(parent):
    """
    - 名称: 中间展示区
    - 功能: 创建并管理中间展示区
    - 参数: parent - CTk实例
    - 返回: 无
    """
    display_frame = ctk.CTkFrame(parent)
    display_frame.pack(expand=True, fill="both", padx=30, pady=10)

    words_list = read_words_from_file(QUOTE_FILE)
    if words_list:
        init_text = random.choice(words_list)
    else:
        init_text = "没有语录可显示"

    display_label = ctk.CTkLabel(
        display_frame,
        text=init_text,
        font=STYLE_CONTENT_FONT
    )
    display_label.place(relx=0.5, rely=0.5, anchor="center")
