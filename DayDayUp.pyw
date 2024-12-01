# 工具打包
# pip install pyinstaller
# pyinstaller --onefile --windowed DayDayUp.pyw  # 生成可执行文件

# ========== 导入必要模块 ========== #
import tkinter as tk  # 用于创建图形用户界面
import random  # 提供随机选择功能
import os  # 用于文件操作
import sys  # 系统操作
from pystray import Icon, MenuItem, Menu  # 创建系统托盘图标
from PIL import Image  # 图像处理
from tkinter import messagebox  # 创建消息弹窗
from win11toast import toast  # 实现桌面通知功能

# ========== 配置参数 ========== #
# 随机时间间隔 (单位: 毫秒)
TIME_RANDOM = 600000  # 每10分钟更新一次语录
WORD_LENGTH = 100  # 限制语录的最大字符长度
QUOTE_FILE = "Bible.txt"  # 默认语录存储文件
ICON_FILE = "icon.ico"  # 托盘图标文件路径
WINDOW_WIDTH = 1100  # 窗口宽度
WINDOW_HEIGHT = 500  # 窗口高度
MIN_WINDOW_WIDTH = 800  # 最小宽度
MIN_WINDOW_HEIGHT = 500  # 最小高度
quotes = [] # 暂时储存语录


# ========== 初始化语录 ========== #
def load_quotes():
    global quotes
    if os.path.exists(QUOTE_FILE):
        with open(QUOTE_FILE, "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file]
    else:
        quotes = ["为了明天的你", "我爱你，孙浩男"]

# ========== 保存语录到文件 ========== #
def save_quotes():
    with open(QUOTE_FILE, "w", encoding="utf-8") as file:
        file.writelines(f"{quote}\n" for quote in quotes)

# ========== 随机语录功能 ========== #
def update_quote_only():
    quote = random.choice(quotes)  # 随机选取语录
    formatted_quote = quote.replace(".", "\n").replace("：", "\n")  # 格式化
    label.config(text=formatted_quote)

# ========== 显示通知 ========== #
def show_quote():
    quote = random.choice(quotes)  # 随机选择语录
    timer = 0 # 计数器
    pages = 1 # 计算页数

    # 获取标题（取“：”前的内容）
    title, content = quote.split("：", 1) if "：" in quote else ("励志话语", quote)

    # 格式化语句为换行形式
    formatted_quote = content[:-1].replace(".", "\n") + content[-1] if content.endswith(".") else content.replace(".", "\n")
    label.config(text=formatted_quote)  # 在窗口中完整显示语句

    # 定义通知栏限制参数
    max_line_length = 25  # 单行最大字符数
    max_lines = 4  # 通知最多显示的行数
    max_notification_length = max_line_length * max_lines  # 通知最大字符数

    # 计算 timer 的值
    for line in formatted_quote.split("\n"):
        # 每遇到一个换行符，timer +1
        timer += 1
        if len(line) > 25:
            timer += 1
    # 根据 timer 值计算需要的页数
    if timer > 4:
        pages = (timer // 4) + (1 if timer % 4 != 0 else 0)  # 向上取整计算页数

    # 检查语句长度是否超出通知栏限制
    if  pages <= 1:
        # 如果没有超出限制，直接发送一条通知
        toast(title, formatted_quote, duration="short")
    else:
        # 将语句按行切分，并逐页发送通知
        lines = formatted_quote.split("\n")  # 分割成每行的列表
        chunks = []  # 用于存储分组的行

        # 将行分组，每组最多 max_lines 行
        for i in range(0, len(lines), max_lines):
            chunk = "\n".join(lines[i:i + max_lines])
            chunks.append(chunk)

        # 遍历分组，逐段发送通知
        for idx, chunk in enumerate(chunks):
            toast(f"{title} - 第 {idx + 1}/{pages} 页", chunk, duration="short")


    # 定时触发下一次更新
    window.after(TIME_RANDOM, show_quote)

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

# ========== 退出功能 ========== #
def quit_app():
    global icon
    if icon:
        icon.stop()  # 停止托盘图标
    window.quit()  # 关闭窗口
    sys.exit()  # 退出程序

# ========== 切换窗口状态 ========== #
def toggle_window(icon=None, item=None):
    if window.state() == "withdrawn":
        window.deiconify()
        window.lift()
    else:
        window.withdraw()

# ========== 隐藏窗口 ========== #
def on_window_cover():
    window.withdraw()  # 隐藏窗口

# ========== 显示窗口 ========== #
def show_window(icon=None, item=None):
    window.deiconify()  # 显示窗口
    window.lift()  # 将窗口提升到最前

# ========== 系统托盘功能 ========== #
def create_tray_icon():
    global icon
    try:
        icon_image = Image.open(ICON_FILE)  # 加载托盘图标
        icon = Icon(
            "励志话语", icon=icon_image,
            menu=Menu(
                MenuItem("切换", toggle_window, default=True,visible=False),
                MenuItem("退出", quit_app)
            )
        )
        icon.run_detached()  # 运行托盘图标
        icon.visible = True
    except Exception as e:
        messagebox.showerror("错误", f"加载托盘图标失败: {e}")
        sys.exit()

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

if __name__ == "__main__":
    load_quotes()
    main_window()
    add_menu()
    label_win()
    win_size()
    Button_window()
    create_tray_icon()
    show_quote()
    window.mainloop()
