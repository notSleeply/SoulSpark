import os
from src.Config import *



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
