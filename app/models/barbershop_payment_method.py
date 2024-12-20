
from app.database.db import db

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class BarbershopPaymentMethod(db.Model):
    __tablename__ = 'barbershop_payment_methods'

    id: Mapped[int] = mapped_column(primary_key=True)
    barbershop_id: Mapped[int] = mapped_column(ForeignKey('barbershops.id'))
    payment_method_id : Mapped[int] = mapped_column(ForeignKey('payment_methods.id'))

    payment_method: Mapped['PaymentMethod'] = relationship()