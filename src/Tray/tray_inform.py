import random
from win11toast import toast
from src.Config import *
from src.Tools import quotes

# ========== 显示通知 ========== #
def show_quote():
    from src.UI import get_window, get_label
    
    window = get_window()
    label = get_label()
    
    if not window or not label:
        return
        
    quote = random.choice(quotes)  # 随机选择语录
    timer = 0 # 计数器
    pages = 1 # 计算页数

    # 获取标题（取"："前的内容）
    title, content = quote.split("：", 1) if "：" in quote else ("励志话语", quote)

    # 格式化语句为换行形式
    formatted_quote = content[:-1].replace(".", "\n") + content[-1] if content.endswith(".") else content.replace(".", "\n")
    label.config(text=formatted_quote)  # 在窗口中完整显示语句

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
    if pages <= 1:
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
