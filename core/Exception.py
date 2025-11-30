# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Exception handling module
"""
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """
    HTTP异常处理器
    :param _: 请求对象
    :param exc: HTTP异常实例
    :return: JSON响应
    """
    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "data": exc.detail
         },status_code=exc.status_code
    )

class UnicornException(Exception):
    """
    自定义异常类
    """
    def __init__(self, code: int = 400, message: str = "Unicorn Exception", data: Union[dict, list, str] = None):
        if data is None:
            data = {}
        self.code = code
        self.message = message
        self.data = data

async def unicorn_exception_handler(_: Request, exc: UnicornException) -> JSONResponse:
    """
    自定义异常处理器
    :param _: 请求对象
    :param exc: UnicornException实例
    :return: JSON响应
    """
    return JSONResponse({
        "code": exc.code,
        "message": exc.message,
        "data": exc.data
         },status_code=exc.code
    )

async def http_validation_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError]) -> JSONResponse:
    """
    请求验证异常处理器
    :param _: 请求对象
    :param exc: 验证异常实例
    :return: JSON响应
    """
    return JSONResponse({
        "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "message": f"Validation Error {exc.errors()}",
        "data": exc.errors()
         },status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )