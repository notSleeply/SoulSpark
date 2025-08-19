from src.Words import text_to_file
from src.config import QUOTE_FILE
from .ui_state_words import start_random_timer, stop_random_timer, on_random_click, show_click_text


def set_components(instance, display_textbox, btn_random):
    """
    功能: 存储UI组件的引用并设置按钮命令
    """
    instance.display_textbox = display_textbox
    instance.btn_random = btn_random
    instance.btn_random.configure(command=lambda: on_bottom_click(instance))
    on_random_click(instance)
    start_random_timer(instance)


def on_add_click(instance):
    """
    功能: 处理添加按钮的点击事件
    """
    stop_random_timer(instance)
    instance.mode = "add"
    instance.display_textbox.configure(state="normal")
    instance.display_textbox.delete("0.0", "end")
    instance.btn_random.configure(text="确定")


def on_show_click(instance):
    """
    功能: 处理展示按钮的点击事件
    """
    instance.mode = "show"
    if instance.saved_text:
        show_click_text(instance, instance.saved_text)
    instance.display_textbox.configure(state="disabled")
    instance.btn_random.configure(text="随机一下")
    start_random_timer(instance)


def on_bottom_click(instance):
    """
    功能: 处理底部按钮的点击事件，根据当前模式执行不同操作
    """
    if instance.mode == "add":
        new_text = instance.display_textbox.get("0.0", "end-1c").strip()
        if new_text:
            text_to_file(QUOTE_FILE, new_text)
            print(f"添加新语录: {new_text}")
    else:
        on_random_click(instance)
