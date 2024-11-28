from typing import Annotated
from fastapi import APIRouter, Depends
from repository import PersonRepository
from schemas import SPersonAdd, SPerson
from typing import Optional


router = APIRouter(
    prefix="/persons",
    tags=["test_api"],
)


@router.post("")
async def add_person(person: Annotated[SPersonAdd, Depends()]):
    person_id = await PersonRepository.add_one(person)
    return  {"ok": True, "person_id": person_id}


@router.get("")  
async def get_persons(
    name: Optional[str] = None,
    surname: Optional[str] = None,
    age: Optional[int] = None,
    post: Optional[str] = None,
    description: Optional[str] = None
    ) -> list[SPerson]:
    
    persons = await PersonRepository.show_all()
    if not any([name, surname, age, post, description]):
        return persons
    
    else:
        return_list = []
        for person in persons:
            if (name is None or person.name == name) and \
                (surname is None or person.surname == surname) and \
                    (age is None or person.age == age) and \
                        (post is None or person.post == post) and \
                            (description is None or person.description == description):
                return_list.append(person)
        return return_list
