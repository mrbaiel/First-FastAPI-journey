from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, del_tables
from route import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await del_tables()
    print("Данные очищены")
    await create_tables()
    print("БД готова к работе")
    yield
    print("Выключение ")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)