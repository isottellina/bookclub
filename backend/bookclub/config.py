from os import getenv


POSTGRES_HOST: str = getenv("POSTGRES_HOST", "postgres")
POSTGRES_USER: str = getenv("POSTGRES_USER", "debug")
POSTGRES_PASSWORD: str = getenv("POSTGRES_PASSWORD", "debug")
POSTGRES_DB: str = getenv("POSTGRES_DB", "bookclub")


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
