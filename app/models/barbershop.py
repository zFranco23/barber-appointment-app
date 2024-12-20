
from app.database.db import db
from sqlalchemy.orm import Mapped, mapped_column

class Barbershop(db.Model):
    __tablename__ = 'barbershops'

    # __schema__ = 'barbershops'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    experience_years: Mapped[int]