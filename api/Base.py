# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: Base API module
"""

from fastapi import APIRouter, Request
router = APIRouter()

@router.get("/")
async def home(request: Request):
    print("Request received at / endpoint")
    return "fastapi"