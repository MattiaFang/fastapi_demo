# -*- coding: utf-8 -*-
"""
@Created on 2025-11-30
@Author: Mattia
@Description: APP Runner Module
"""
import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from api.Base import router
from core.Exception import http_error_handler, unicorn_exception_handler, UnicornException, http_validation_error_handler
from core.Events import lifespan
from core.Middleware import Middleware


application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJEST_NAME,
    lifespan=lifespan,
    )

# Event Listeners (old version, deprecated)
# application.add_event_handler("startup", startup(application))
# application.add_event_handler("shutdown", stopping(application))

# Exception Handlers
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)
application.add_exception_handler(RequestValidationError, http_validation_error_handler)

# api router
application.include_router(router)

# middlewares
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie="session_id",
    # max_age=86400,
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)
# static files mount
application.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")))

app = application