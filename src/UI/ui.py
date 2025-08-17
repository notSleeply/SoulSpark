"""
`ui.py` - **UI模块 (customtkinter 版)**
1. 主窗口：创建和管理主应用窗口
2. 组件：定义和管理UI组件
3. 事件：处理用户交互和事件
"""

import customtkinter as ctk
from src.config import NAME, GEOMETRY, STYLE_BUTTON_FONT, STYLE_CONTENT_FONT, STYLE_COLOR, STYLE_MODE


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
    create_top_frame(root)
    create_display_frame(root)
    create_bottom_frame(root)

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
