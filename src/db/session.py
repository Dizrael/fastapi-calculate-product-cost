import os
from .models import Base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"


engine = create_async_engine(DB_URL)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    """
    Инициализирует базу данных, создавая все необходимые таблицы.

    Пытается подключиться к базе данных и создать таблицы.
    В случае успеха выводит сообщение об успешном подключении.
    В случае ошибки выводит детальную информацию об ошибке и URL базы данных.

    Raises:
        Exception: Если не удалось подключиться к базе данных или создать таблицы
    """
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print(f"Successfully connected to the database at {DB_HOST}")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        print(f"Database URL: postgresql+asyncpg://{DB_USER}:***@{DB_HOST}:5432/{DB_NAME}")
        raise


async def get_db():
    """
    Функция-зависимость для получения сессии базы данных.

    Создает асинхронную сессию базы данных и предоставляет ее как зависимость
    для эндпоинтов FastAPI. После завершения запроса сессия автоматически закрывается.

    Yields:
        AsyncSession: Асинхронная сессия базы данных
    """
    async with AsyncSessionLocal() as session:
        yield session
