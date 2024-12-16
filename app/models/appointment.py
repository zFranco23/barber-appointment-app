
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.database.db import db



class Appointment(db.Model):
    __tablename__ = 'appointments'

    # __schema__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    appointment_date: Mapped[str] ## check how to handle dates
    # service_id: Mapped[int]
    # barber_id: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))

    ## relationships

    # user: Mapped['User'] = relationship(back_populates="appointments")
    service: Mapped['Service'] = relationship()


    