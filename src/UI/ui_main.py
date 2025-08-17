"""
`ui_main.py`  - **UI模块** 
1. 主窗口：创建和管理主应用窗口
2. 组件：定义和管理UI组件
3. 事件：处理用户交互和事件
"""

import tkinter as tk
from tkinter import ttk
from src.config import NAME, GEOMETRY



# ========== 主窗口 ========== #
def main_window():
    root = tk.Tk()
    root.title(NAME)
    root.geometry(GEOMETRY)

    label = ttk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=20)

    button = ttk.Button(root, text="点击我", command=lambda: print("按钮被点击"))
    button.pack()

    root.mainloop()
