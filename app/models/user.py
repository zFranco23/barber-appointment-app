
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db import db

from typing import List



class User(db.Model):
    __tablename__ = 'users'

    # __schema__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    phone: Mapped[str]
    password: Mapped[str]

    ## relationships

    appointments: Mapped[List["Appointment"]] = relationship()


    