
import os

def resolve_file_path(filepath):
    """
    - 名称: 解析文件路径
    - 功能: 检查文件是否存在，如果不存在则尝试在 ./dist/ 目录下查找
    - 参数: filepath - 原始文件路径
    - 返回: 实际存在的文件路径，如果都不存在则返回 None
    """
    if os.path.exists(filepath):
        return filepath

    # 如果原始路径不存在，尝试在 ./dist/ 目录下查找
    dist_filepath = os.path.join("./dist", filepath)
    if os.path.exists(dist_filepath):
        return dist_filepath

    # 都不存在
    print(f"文件不存在: {filepath} 和 {dist_filepath}")
    return None
