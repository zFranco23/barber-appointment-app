from app.database.db import db
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import ForeignKey


class AppointmentBarbershopService(db.Model):
    __tablename__ = 'appointment_barbershop_services'

    # __schema__ = 'appointment_barbershop_services'  

    id: Mapped[int] = mapped_column(primary_key=True)
    appointment_id: Mapped[int] = mapped_column(ForeignKey('appointments.id'))
    barbershop_service_id: Mapped[int] = mapped_column(ForeignKey('barbershop_services.id'))