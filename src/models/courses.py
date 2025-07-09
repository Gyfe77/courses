from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class СoursesModel(Base):
    __tablename__ = "Сourses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    price: Mapped[int]