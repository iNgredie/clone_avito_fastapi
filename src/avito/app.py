from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='Avito',
    description='Сервис объявлений',
    version='1.0.0',
)

app.include_router(router)
