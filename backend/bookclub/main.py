#!/usr/bin/env python3
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import Response, JSONResponse
from starlette.requests import Request

async def hello(_request: Request) -> Response:
    return JSONResponse({
        "ping": "pong",
    })

def create_app():
    return Starlette(
        routes=[
            Route("/api/", hello),
        ]
    )
