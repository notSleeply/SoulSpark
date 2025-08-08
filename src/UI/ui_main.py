import tkinter as tk
from tkinter import messagebox
import random
from src.Config import *
from src.Tools import quotes, save_quotes

# 全局变量
window = None
label = None
menu_bar = None

# ========== 隐藏窗口 ========== #
def on_window_cover():
    window.withdraw()  # 隐藏窗口

# ========== 主窗口 ========== #
def main_window():
    global window
    window = tk.Tk()
    window.title("励志话语")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # 设置窗口大小
    window.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)  # 设置最小尺寸
    window.resizable(True, True)  # 窗口大小可调整
    window.protocol("WM_DELETE_WINDOW", on_window_cover)  # 自定义关闭事件

# ========== 自动调整文字换行 ========== #
def update_wraplength(event):
    new_width = event.width - 5
    if new_width > MIN_WINDOW_WIDTH:
        label.config(wraplength=new_width)

# ========== 窗口尺寸调整 ========== #
def win_size():
    window.bind("<Configure>", update_wraplength)

# ========== 显示语录 ========== #
def label_win():
    global label
    label = tk.Label(
        window, text=random.choice(quotes),
        font=("Microsoft YaHei", 24),
        padx=10, pady=20,
        wraplength=WINDOW_WIDTH, justify="center"
    )
    label.pack()

# ========== 随机语录功能 ========== #
def update_quote_only():
    quote = random.choice(quotes)  # 随机选取语录
    formatted_quote = quote.replace(".", "\n").replace("：", "\n")  # 格式化
    label.config(text=formatted_quote)

# ========== 添加新语录 ========== #
def add_quote():
    # 内部函数：保存新语录
    def save_new_quote():
        new_quote = entry.get().strip()  # 获取用户输入
        if not new_quote:
            messagebox.showwarning("警告", "输入不能为空！")  # 输入校验
        elif len(new_quote) > WORD_LENGTH:
            messagebox.showwarning("警告", f"输入的语录不能超过{WORD_LENGTH}个字符！")
        else:
            quotes.append(new_quote)  # 添加到语录列表
            save_quotes()  # 保存到文件
            entry_window.destroy()  # 关闭输入窗口

    # 创建输入窗口
    entry_window = tk.Toplevel(window)
    entry_window.title("添加新话语")
    tk.Label(entry_window, text=f"请输入新的话语（不超过{WORD_LENGTH}个字符）：").pack(pady=5)
    entry = tk.Entry(entry_window, width=50)  # 输入框
    entry.pack(padx=10, pady=10)
    tk.Button(entry_window, text="保存", command=save_new_quote).pack(pady=5)

# ========== 退出功能 ========== #
def quit_app():
    from src.Tray import stop_tray_icon
    stop_tray_icon()  # 停止托盘图标
    window.quit()  # 关闭窗口
    import sys
    sys.exit()  # 退出程序

# ========== 显示窗口 ========== #
def show_window(icon=None, item=None):
    window.deiconify()  # 显示窗口
    window.lift()  # 将窗口提升到最前

# ========== 切换窗口状态 ========== #
def toggle_window(icon=None, item=None):
    if window.state() == "withdrawn":
        window.deiconify()
        window.lift()
    else:
        window.withdraw()

# ========== 添加菜单栏 ========== #
def add_menu():
    global menu_bar
    menu_bar = tk.Menu(window)# 创建菜单栏

    # 添加菜单选项
    menu_file()
    menu_use()
    menu_help()

    # 将菜单栏添加到主窗口
    window.config(menu=menu_bar)

# ========== "文件"菜单 ========== #
def menu_file():
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="退出", command=quit_app)
    menu_bar.add_cascade(label="文件", menu=file_menu)

# ========== "使用"菜单 ========== #
def menu_use():
    use_menu = tk.Menu(menu_bar, tearoff=0)
    use_menu.add_command(label="添加话语", command=add_quote)
    menu_bar.add_cascade(label="功能", menu=use_menu)

# ========== "帮助"菜单 ========== #
def menu_help():
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="关于", command=show_about)
    menu_bar.add_cascade(label="帮助", menu=help_menu)

# ========== 关于信息窗口 ========== #
def show_about():
    messagebox.showinfo("关于", "励志话语\n版本: 1.0\n作者: 孙浩男")

# ========== 窗口底部标签 ========== #
def Button_window():
    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
    random_button = tk.Button(
        button_frame,
        text="随机话语",
        command=update_quote_only,
        font=("Microsoft YaHei", 12),
        bg="white"
    )
    random_button.pack(fill=tk.X, padx=20)

# ========== 获取窗口对象 ========== #
def get_window():
    return window

# ========== 获取标签对象 ========== #
def get_label():
    return label
