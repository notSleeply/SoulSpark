"""
励志话语提醒工具主程序
"""

# 导入所需模块
from src.Tools import load_quotes
from src.UI import main_window, add_menu, label_win, win_size, Button_window, get_window
from src.Tray import create_tray_icon, show_quote

def main():
    """主程序入口"""
    # 初始化语录
    load_quotes()
    
    # 创建并配置主窗口
    main_window()
    add_menu()
    label_win()
    win_size()
    Button_window()
    
    # 创建系统托盘图标
    create_tray_icon()
    
    # 开始显示通知
    show_quote()
    
    # 启动主循环
    window = get_window()
    window.mainloop()

if __name__ == "__main__":
    main()
