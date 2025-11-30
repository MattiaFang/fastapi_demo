# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Helper functions
"""

import hashlib
import uuid

def random_str() -> str:
    """生成随机字符串

    Args:
        length (int, optional): 字符串长度. Defaults to 8.

    Returns:
        str: 随机字符串
    """
    only = hashlib.md5(str(uuid.uuid4()).encode("utf-8")).hexdigest()
    return str(only)