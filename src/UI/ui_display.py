"""
`ui_display.py`  - **UI模块** 
1. 中间展示区：创建和管理中间展示区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
from src.config import STYLE_CONTENT_FONT,QUOTE_FILE
from src.Words import random_choice


def display_show(parent):
    """
    - 名称: 展示内容
    - 功能: 显示当前文本框中的内容
    - 参数: parent - 文本框的父容器
    - 返回: display_textbox - 配置好的文本框实例
    """
    init_text = random_choice(QUOTE_FILE)
    display_textbox = ctk.CTkTextbox(
        parent,
        font=STYLE_CONTENT_FONT,
        wrap="word",  
        activate_scrollbars=True 
    )
    display_textbox.bind("<Return>", lambda e: "break")
    display_textbox.place(relx=0.02, rely=0.02,
                          relwidth=0.96, relheight=0.96, anchor="nw")
    display_textbox.insert("0.0", init_text)
    display_textbox.configure(state="disabled")
    return display_textbox, init_text

def display_frame(parent):
    """
    - 名称: 中间展示区
    - 功能: 创建并管理中间展示区
    - 参数: parent - CTk实例
    - 返回: display_textbox - 供其他模块使用的文本框
    """
    display_frame = ctk.CTkFrame(parent)
    display_frame.pack(expand=True, fill="both", padx=10, pady=10)

    display_textbox, init_text = display_show(display_frame)

    return display_textbox, init_text
