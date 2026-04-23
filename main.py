from fastapi import FastAPI
from router import router as tasks_router


app = FastAPI(title="Тестовое задание :)")

app.include_router(tasks_router)