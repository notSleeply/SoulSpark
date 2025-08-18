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
    - 返回: display_textbox - 供其他模块使用的文本框
    """
    display_frame = ctk.CTkFrame(parent)
    display_frame.pack(expand=True, fill="both", padx=10, pady=10)

    init_text = random_choice(QUOTE_FILE)

    display_textbox = ctk.CTkTextbox(
        display_frame,
        font=STYLE_CONTENT_FONT,
        wrap="word",  # 自动换行
        activate_scrollbars=True  # 激活滚动条
    )
    display_textbox.place(relx=0.02, rely=0.02,
                          relwidth=0.96, relheight=0.96, anchor="nw")

    # 插入初始文本
    display_textbox.insert("0.0", init_text)

    # 设置为只读模式（不能编辑）
    display_textbox.configure(state="disabled")

    return display_textbox
