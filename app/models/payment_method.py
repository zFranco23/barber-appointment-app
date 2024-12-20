
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import db

class PaymentMethod(db.Model):
    __tablename__ = 'payment_methods'

    # __schema__ = 'payment_methods'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]