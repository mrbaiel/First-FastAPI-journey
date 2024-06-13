from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepo
from schemas import TaskAdd, Task, TaskId

router = APIRouter(
    prefix="/tasks",
    default="Задачки",
)

@router.post("")
async def add_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepo.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskRepo.find_all()
    return tasks
