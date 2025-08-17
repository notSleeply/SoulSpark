"""
`ui.py`  - **UI模块** 
1. 主窗口：创建和管理主应用窗口
2. 组件：定义和管理UI组件
3. 事件：处理用户交互和事件
"""

import tkinter as tk
from tkinter import ttk
from src.config import NAME, GEOMETRY, STYLE_BUTTON_FONT, STYLE_CONTENT_FONT


def main_window():
    """
    - 名称: 主窗口
    - 功能: 创建并显示主应用窗口
    - 参数: 无
    - 返回: 无
    """
    root = tk.Tk()
    config_frame(root)
    create_top_frame(root)
    create_display_frame(root)
    create_bottom_frame(root)

    root.mainloop()


def config_frame(root):
    """
    - 名称: root配置
    - 功能: 管理tk实例配置区
    - 参数: root - tk实例
    - 返回: 无
    """
    root.title(NAME)
    root.geometry(GEOMETRY)
    root.resizable(False, False) 


def create_top_frame(parent):
    """
    - 名称: 顶部按钮区
    - 功能: 创建并管理顶部按钮区
    - 参数: parent - tk实例
    - 返回: 无
    """
    top_frame = ttk.Frame(parent)
    top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

    style = ttk.Style()
    style.configure("Big.TButton", font=(STYLE_BUTTON_FONT))

    btn_show = ttk.Button(top_frame, text="展示",
                        style="Big.TButton", width=8, command=None)
    btn_show.pack(side=tk.LEFT, expand=True, fill=tk.X,
                padx=(30, 5), ipadx=20, ipady=8, anchor='w')

    btn_add = ttk.Button(top_frame, text="添加",
                        style="Big.TButton", width=8, command=None)
    btn_add.pack(side=tk.RIGHT, expand=True, fill=tk.X,
                 padx=(5, 30), ipadx=20, ipady=8, anchor='e')


def create_display_frame(parent):
    """
    - 名称: 中间展示区
    - 功能: 创建并管理中间展示区
    - 参数: parent - tk实例
    - 返回: 无
    """
    display_frame = ttk.Frame(parent, borderwidth=2, relief="groove")
    display_frame.pack(expand=True, fill=tk.BOTH, padx=30, pady=10)

    display_label = ttk.Label(display_frame, text="展示",
                              font=(STYLE_CONTENT_FONT))
    display_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def create_bottom_frame(parent):
    """
    - 名称: 底部按钮区
    - 功能: 创建并管理底部按钮区
    - 参数: parent - tk实例
    - 返回: 无
    """
    bottom_frame = ttk.Frame(parent)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    style = ttk.Style()
    style.configure("Big.TButton", font=(STYLE_BUTTON_FONT))

    btn_random = ttk.Button(bottom_frame, text="随机一下", style="Big.TButton")
    btn_random.pack(ipadx=40, ipady=8, pady=5)
