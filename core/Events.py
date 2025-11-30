# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Events listener module
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager
# from app.database.mysql import init_db
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时执行
    print("应用启动完成")
    
    yield
    
    # 应用关闭时执行
    print("应用正在关闭")




"""
    旧版本实现，已失效
    def startup(app: FastAPI):
        async def app_start() -> None:
            # APP 启动完成后触发
            print("App startup complete.")
            
        return app_start

    def stopping(app: FastAPI):
        async def app_stop() -> None:
            # APP 关闭前触发
            print("App is shutting down.")
            
        return app_stop
"""