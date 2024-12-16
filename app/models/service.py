
from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import db

from typing import Optional



class Service(db.Model):
    __tablename__ = 'services'

    # __schema__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[float]


    