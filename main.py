from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("база готова")
    yield
    print("вы включили")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

