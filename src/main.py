from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.api.calculator import router
from src.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Контекстный менеджер для управления жизненным циклом приложения.

    Выполняет инициализацию базы данных при запуске приложения.

    Args:
        app: Экземпляр приложения FastAPI
    """
    await init_db()
    yield


app = FastAPI(title="Price Calculation Service", lifespan=lifespan)

app.include_router(router=router)


@app.get("/")
async def root():
    """
    Корневой эндпоинт приложения.

    Возвращает сообщение о том, что сервис расчета стоимости запущен и работает.

    Returns:
        dict: Словарь с сообщением о статусе сервиса
    """
    return {"message": "Price Calculation Service is running."}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
