from fastapi import APIRouter
from sqlalchemy import select

from src.api.dependencies import SessionDep, PaginationDep
from src.database import engine, Base
from src.models.courses import СoursesModel
from src.schemas.courses import CoursesSchema, CoursesGetSchema

router = APIRouter()


@router.post('/create', tags=['Создание БД'])
async def setup_datebase():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@router.post("/cours", tags=['Добавление курсов'] )
async def add_book(cours: CoursesSchema, session: SessionDep) -> CoursesSchema:
    new_book = СoursesModel(
        title=cours.title,
        author=cours.author,
        price=cours.price,
    )
    session.add(new_book)
    await session.commit()
    return cours


@router.get('/courses', tags=['Получение курсов'])
async def get_books(session: SessionDep,
                    pagination: PaginationDep) -> list[CoursesGetSchema]:
    query = (select(СoursesModel)
             .limit(pagination.limit)
             .offset(pagination.offset))
    result = await session.execute(query)
    return result.scalars().all()
