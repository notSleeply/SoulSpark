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
    new_text = random_choice(QUOTE_FILE)
    show_textbox(instance.display_textbox, new_text)


def start_random_timer(instance):
    """
    功能: 启动随机定时器，每隔一分钟自动更新语录
    """
    if instance.mode == "show" and instance.timer_id is None:
        on_random_click(instance)
    instance.timer_id = instance.root.after(
        60000, lambda: start_random_timer(instance))


def stop_random_timer(instance):
    """
    功能: 停止随机定时器
    """
    if instance.timer_id:
        instance.root.after_cancel(instance.timer_id)
        instance.timer_id = None
