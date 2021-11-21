import sqlalchemy as sa
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from .models import Book


async def get_books_collection(request: Request) -> Response:
    return JSONResponse([])
