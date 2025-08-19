"""
`show_click.py`  - **事件处理模块** 
1. 负责处理展示按钮的点击事件
2. 负责处理随机按钮的点击事件
3. 负责管理不同UI组件之间的交互
"""


def show_textbox(display_textbox, text):
    """
        - 名称: 展示文本框
        - 功能: 封装文本框的更新逻辑，包括清空、插入和禁用
        - 参数: display_textbox - 要显示的文本框, text - 要显示在文本框中的文本
        - 返回: 无
        """
    display_textbox.configure(state="normal")
    display_textbox.delete("0.0", "end")
    display_textbox.insert("0.0", text)
    display_textbox.configure(state="disabled")
