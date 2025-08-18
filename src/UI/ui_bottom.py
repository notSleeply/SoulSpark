"""
`ui_bottom.py`  - **UI模块** 
1. 底部按钮区：创建和管理底部按钮区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
from src.config import STYLE_BUTTON_FONT, QUOTE_FILE
from src.Words import random_choice


def on_random_click(display_textbox):
    new_text = random_choice(QUOTE_FILE)
    display_textbox.configure(state="normal")  # 允许编辑
    display_textbox.delete("0.0", "end")       # 清空内容
    display_textbox.insert("0.0", new_text)    # 插入新内容
    display_textbox.configure(state="disabled")  # 只读


def create_bottom_frame(parent, display_textbox):
    """
    - 名称: 底部按钮区
    - 功能: 创建并管理底部按钮区
    - 参数: parent - CTk实例， display_textbox - 用于显示语录的文本框
    - 返回: 无
    """
    bottom_frame = ctk.CTkFrame(parent, fg_color="transparent")
    bottom_frame.pack(side="bottom", fill="x", pady=10)

    btn_random = ctk.CTkButton(
        bottom_frame,
        text="随机一下",
        font=STYLE_BUTTON_FONT,
        width=200,
        height=50,
        command=lambda: on_random_click(display_textbox)
    )
    btn_random.pack(pady=5)
