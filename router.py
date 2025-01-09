from typing import Annotated
from fastapi import Depends, APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from schemas import STaskAdd
from repository import TaskRepository
from config import image_adress
import shutil
import os

router = APIRouter(
    prefix="/tasks"
)



@router.post("")
async def get_tasks(
    task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.show_all()
    return {"data": tasks}

@router.get("/file/download")
async def download_file():
    return FileResponse(path='image.png', filename='image.png', media_type='multipart/form-data')

@router.post("/file/upload")
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as wf:
        shutil.copyfileobj(file.file, wf)
        os.rename(f'{file.filename}', image_adress)
        file.file.close()
    return file.filename
