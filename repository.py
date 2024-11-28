from database import new_session, PersonTable
from schemas import SPersonAdd, SPerson
from sqlalchemy import select


class PersonRepository():
    @classmethod
    async def add_one(cls, data: SPersonAdd) -> int:
        async with new_session() as session:
            person_dictionary = data.model_dump()
            person = PersonTable(**person_dictionary)
            session.add(person)
            await session.flush()
            await session.commit()
            return person.id
        
    @classmethod
    async def show_all(cls) -> list[SPerson]:
        async with new_session() as session:
            query = select(PersonTable)
            result = await session.execute(query)
            person_models = result.scalars().all()
            return person_models
