import src.UI as UI
from src.Mutex import check_single_instance, release_mutex

def main():
    print("程序启动")
    UI.main_window()

if __name__ == "__main__":
    mutex = check_single_instance()
    try:
        main()
    finally:
        release_mutex(mutex)
