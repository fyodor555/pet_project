from database import new_session, TaskTable
from schemas import STaskAdd, STaskGet
from sqlalchemy import select


class TaskRepository():
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dictionary = data.model_dump()
            task = TaskTable(**task_dictionary)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
        
    @classmethod
    async def add_image(cls, data: str):
        async with new_session() as session:
            task = TaskTable()
            task.image_adress = data
            session.add(task.image_adress)
            await session.flush()
            await session.commit()
            return task.id
    
    @classmethod
    async def show_all(cls) -> list[STaskGet]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
        
