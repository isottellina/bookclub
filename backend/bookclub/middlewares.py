from .database import async_session


class SessionMiddleware:
    """
    Add a database session to the request.
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        async with async_session() as session:
            scope["session"] = session
            return await self.app(scope, receive, send)
