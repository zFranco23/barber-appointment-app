
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.database.db import db


class BarbershopService(db.Model):
    __tablename__ = 'barbershop_services'

    # __schema__ = 'barber_services'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    barbershop_id: Mapped[int] = mapped_column(ForeignKey('barbershops.id'))
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'))

    price: Mapped[float]
    hours_duration: Mapped[str] 


    ## relationships
    # barbershop: Mapped['Barbershop'] = relationship(back_populates="barbershop_services")
    service: Mapped['Service'] = relationship()