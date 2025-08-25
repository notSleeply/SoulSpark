import sys
import win32event
import win32api
import winerror
import pywintypes


# 全局唯一互斥锁名称，建议用你的应用名或 GUID
MUTEX_NAME = "Global\\SoulSpark_OnlyOneInstance"


def check_single_instance():
    """
    检查是否已有实例在运行，若有则退出。
    返回互斥锁句柄，主程序退出时需关闭。
    """
    sa = pywintypes.SECURITY_ATTRIBUTES()
    mutex = win32event.CreateMutex(sa, True, MUTEX_NAME)
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        print("程序已在运行，不允许多开。")
        sys.exit(0)
    return mutex


def release_mutex(mutex):
    """释放互斥锁"""
    if mutex:
        win32api.CloseHandle(mutex)
