"""
`words.py`  - **语录模块** 
1. 语录管理：增删改查语录
2. 语录推荐：根据用户喜好推荐语录
3. 语录搜索：根据关键词搜索语录
"""
import os
from src.config import QUOTE_FILE


def read_words_from_file(filepath):
    """
    - 名称: 从文件读取语录
    - 功能: 从指定文件读取语录，每行一条，返回语录列表
    - 参数: filepath - 文件路径
    - 返回: 语录列表
    """
    words = []

    actual_filepath = resolve_file_path(filepath)
    if actual_filepath is None:
        words.append("未找到语录文件，请检查配置。")
        return words

    try:
        with open(actual_filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    words.append(line)
    except Exception as e:
        print(f"读取语录文件失败: {e}")
    return words


def resolve_file_path(filepath):
    """
    - 名称: 解析文件路径
    - 功能: 检查文件是否存在，如果不存在则尝试在 ./dist/ 目录下查找
    - 参数: filepath - 原始文件路径
    - 返回: 实际存在的文件路径，如果都不存在则返回 None
    """
    if os.path.exists(filepath):
        return filepath

    # 如果原始路径不存在，尝试在 /dist 目录下查找
    dist_filepath = os.path.join("./dist", filepath)
    if os.path.exists(dist_filepath):
        return dist_filepath

    # 都不存在
    print(f"文件不存在: {filepath} 和 {dist_filepath}")
    return None
