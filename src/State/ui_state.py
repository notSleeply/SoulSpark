"""
`app_state.py`  - **应用状态管理** 
1. 管理应用的当前状态（如“添加”或“展示”模式）
2. 存储和更新UI组件的引用
3. 处理不同UI组件之间的交互逻辑
"""
from .ui_state_words import show_click_text, on_random_click, start_random_timer, stop_random_timer
from .ui_state_handlers import set_components, on_add_click, on_show_click, on_bottom_click


class UIState:
    """
    - 名称: 应用状态管理
    - 功能: 管理应用的当前状态
    - 参数: 无
    - 返回: 无
    """

    def __init__(self, root):
        """
        - 名称: 初始化应用状态
        - 功能: 设置初始状态和UI组件引用
        """
        self.root = root
        self.mode = "show"
        self.display_textbox = None
        self.btn_random = None
        self.saved_text = ""
        self.timer_id = None

    def show_click_text(self, text):
        show_click_text(self, text)

    def on_random_click(self):
        on_random_click(self)

    def set_components(self, display_textbox, btn_random):
        set_components(self, display_textbox, btn_random)

    def on_add_click(self):
        on_add_click(self)

    def on_show_click(self):
        on_show_click(self)

    def on_bottom_click(self):
        on_bottom_click(self)

    def start_random_timer(self):
        start_random_timer(self)

    def stop_random_timer(self):
        stop_random_timer(self)
