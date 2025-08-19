"""
`app_state.py`  - **应用状态管理** 
1. 管理应用的当前状态（如“添加”或“展示”模式）
2. 存储和更新UI组件的引用
3. 处理不同UI组件之间的交互逻辑
"""
from src.Words import text_to_file 
from src.config import QUOTE_FILE
from src.Words import random_choice
from src.UI.show_click import show_textbox


class UIState:
    """
    - 名称: 应用状态管理
    - 功能: 管理应用的当前状态
    - 参数: 无
    - 返回: 无
    """
    def __init__(self):
        """
        - 名称: 初始化应用状态
        - 功能: 设置初始状态和UI组件引用
        - 参数: 无
        - 返回: 无
        """
        self.mode = "show"
        self.display_textbox = None
        self.btn_random = None
        self.saved_text = ""
        
    def show_click_text(self, text):
        """
        - 名称: 展示点击事件
        - 功能: 处理展示按钮的点击事件，显示当前文本框中的内容
        - 参数: 无
        - 返回: 无
        """
        self.saved_text = text
        show_textbox(self.display_textbox, text)

    def on_random_click(self):
        """
        - 名称: 随机按钮点击事件
        - 功能: 处理随机按钮的点击事件，显示随机语录
        - 参数: 无
        - 返回: 无
        """
        new_text = random_choice(QUOTE_FILE)
        show_textbox(self.display_textbox, new_text)

    def set_components(self, display_textbox, btn_random):
        """
        - 名称: 设置UI组件引用
        - 功能: 存储UI组件的引用以供后续使用
        - 参数: display_textbox - 用于显示语录的文本框, btn_random - 随机按钮实例
        - 返回: 无
        """
        self.display_textbox = display_textbox
        self.btn_random = btn_random
        self.btn_random.configure(command=self.on_bottom_click)
        self.on_random_click()

    def on_add_click(self):
        """
        - 名称: "添加"按钮点击事件
        - 功能: 处理添加按钮的点击事件，允许用户输入新的语录
        - 参数: 无
        - 返回: 无
        """
        self.mode = "add"
        self.saved_text = self.display_textbox.get("0.0", "end-1c")
        self.display_textbox.configure(state="normal")
        self.display_textbox.delete("0.0", "end")
        self.btn_random.configure(text="确定")

    def on_show_click(self):
        """
        - 名称: "展示"按钮点击事件
        - 功能: 处理展示按钮的点击事件，显示当前文本框中的内容
        - 参数: 无
        - 返回: 无
        """
        self.mode = "show"
        self.show_click_text(self.saved_text)
        self.display_textbox.configure(state="disabled")
        self.btn_random.configure(text="随机一下")

    def on_bottom_click(self):
        """
        - 名称: 底部按钮点击事件
        - 功能: 处理底部按钮的点击事件，根据当前模式执行不同操作
        - 参数: 无
        - 返回: 无
        """
        if self.mode == "add":
            new_text = self.display_textbox.get("0.0", "end-1c").strip()
            if new_text:
                text_to_file(QUOTE_FILE, new_text)
                print(f"添加新语录: {new_text}")

            self.on_show_click()
            self.display_textbox.insert("0.0", new_text)
        else:
            self.on_random_click()
