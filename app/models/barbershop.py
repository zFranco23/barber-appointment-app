
from app.database.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from typing import List


class Barbershop(db.Model):
    __tablename__ = 'barbershops'

    # __schema__ = 'barbershops'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    start_operations_date: Mapped[datetime.datetime]
    start_hour: Mapped[datetime.datetime] 
    end_hour: Mapped[datetime.datetime] 

    payment_methods: Mapped[List['BarbershopPaymentMethod']] = relationship()