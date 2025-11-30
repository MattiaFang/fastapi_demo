# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Base config module
"""
import os.path
from pydantic_settings import BaseSettings
from typing import List

class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJEST_NAME: str = "FastAPI Demo"
    DESCRIPTION: str = "A simple FastAPI project"
    # 静态文件信息
    STATIC_DIR: str = os.path.join(os.path.dirname(__file__), "static")
    # 跨域访问
    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    SECRET_KEY: str = "your_secret_key_here"
    
    

settings = Config()