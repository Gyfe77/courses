from pydantic import BaseModel, Field


class CoursesSchema(BaseModel):
    title: str
    author: str | None = Field('Не указан', title='Автор')
    price: int


class CoursesGetSchema(BaseModel):
    id: int
    title: str = Field(title='Название')
    author: str | None = Field('Не указан', title='Автор')
    price: int


class PaginationParam(BaseModel):
    limit: int = Field(5, ge=0, le=100, description="Кол-во выводимых строк")
    offset: int = Field(0, ge=0, description="Смещение пагинации")