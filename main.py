from contextlib import asynccontextmanager
from typing import Optional, Annotated

import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from database import create_tables, del_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await del_tables()
    print("Данные очищены")
    await create_tables()
    print("БД готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)


class TaskAdd(BaseModel):
    name: str
    desc: str | None  # str | None == Optional[str] = None


class Task(TaskAdd):
    id: int


@app.post("/tasks")
async def add_task(task: Annotated[TaskAdd, Depends()]):
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Letcode", description="Решить задачу")
#     return {"data": task}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='127.0.0.1')
