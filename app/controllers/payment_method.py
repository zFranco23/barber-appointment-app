from flask_smorest import Blueprint
from flask.views import MethodView

from app.models.payment_method import PaymentMethod
from app.schemas.payment_method import PaymentMethodSchema


from app.database.db import db

payment_method_bp = Blueprint('payment_method', __name__, description="Operations with payment methods")



@payment_method_bp.route("/")
class PaymentMethodHandler(MethodView):


    @payment_method_bp.response(200, PaymentMethodSchema(many=True))
    def get(self):
        payment_methods = db.session.execute(
            db.select(PaymentMethod)
        ).scalars()

        return payment_methods

    @payment_method_bp.response(201)
    @payment_method_bp.arguments(PaymentMethodSchema)
    def post(self, payment_method):

        payment_method = PaymentMethod(**payment_method)

        db.session.add(payment_method)
        db.session.commit()
        