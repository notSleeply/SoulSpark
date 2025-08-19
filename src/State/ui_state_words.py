"""
`ui_state_words.py`  - **UI状态管理** 
1. 处理展示按钮的点击事件
2. 处理随机按钮的点击事件
3. 启动和停止定时器
"""

from threading import Timer
from src.Words import random_choice
from .show_click import show_textbox
from src.config import QUOTE_FILE


def show_click_text(instance, text):
    """
    功能: 处理展示按钮的点击事件，显示当前文本框中的内容
    """
    instance.saved_text = text
    show_textbox(instance.display_textbox, text)


def on_random_click(instance):
    """
    功能: 处理随机按钮的点击事件，显示随机语录
    """
    instance.saved_text = random_choice(QUOTE_FILE)
    show_textbox(instance.display_textbox, instance.saved_text)
    start_random_timer(instance)


def start_random_timer(instance):
    """
    功能: 启动随机定时器，每隔一分钟自动更新语录
    """
    # 停止旧的定时器，以防重复启动
    stop_random_timer(instance)

    # 创建并启动新的定时器
    # 60秒后调用 on_random_click 并传递 instance 参数
    instance.timer = Timer(3, on_random_click, args=[instance])
    instance.timer.daemon = True
    instance.timer.start()


def stop_random_timer(instance):
    """
    功能: 停止随机定时器
    """
    if instance.timer and instance.timer.is_alive():
        instance.timer.cancel()
        instance.timer = None
