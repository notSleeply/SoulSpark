"""
`ui_bottom.py`  - **UI模块** 
1. 底部按钮区：创建和管理底部按钮区
2. 事件处理：处理用户交互和事件
3. 组件管理：定义和管理UI组件
"""
import customtkinter as ctk
from src.config import STYLE_BUTTON_FONT

def create_bottom_frame(parent):
    """
    - 名称: 底部按钮区
    - 功能: 创建并管理底部按钮区
    - 参数: parent - CTk实例
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
        command=lambda: print("随机一下 clicked")
    )
    btn_random.pack(pady=5)
