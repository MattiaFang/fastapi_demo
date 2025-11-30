# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Middleware module
"""
import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from core.Helper import random_str

class Middleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] in ("lifespan", "websocket", "http"):  # lifespan 和 websocket 不处理
            await self.app(scope, receive, send)
            return
 
        start_time = time.time()
        req = Request(scope, receive, send)

        if not req.headers.get("session"):
            req.session.setdefault("session", random_str())
        
        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                process_time = time.time() - start_time
                headers = MutableHeaders(scope=message)
                headers.append("X-Process-Time", str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)