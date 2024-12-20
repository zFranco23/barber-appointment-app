from flask_smorest import Blueprint
from flask.views import MethodView

from app.schemas.barbershop import BarbershopSchema
from app.schemas.barbershop_service import BarbershopServiceSchema
from app.schemas.barbershop_payment_method import BarbershopPaymentMethodSchema

from app.models.barbershop import Barbershop
from app.models.barbershop_service import BarbershopService
from app.models.barbershop_payment_method import BarbershopPaymentMethod


from app.database.db import db




barbershop_bp = Blueprint("barbershop", __name__, description="Operations with barbershop")



@barbershop_bp.route("/")
class BarbershopHandler(MethodView):


    @barbershop_bp.response(200, BarbershopSchema(many=True))
    def get(self):
        barbershops = db.session.execute(
            db.select(Barbershop)
        ).scalars()

        return barbershops

    @barbershop_bp.response(201)
    @barbershop_bp.arguments(BarbershopSchema)
    def post(self, barber):

        barbershop = Barbershop(**barber)
        db.session.add(barbershop)
        db.session.commit()
        

@barbershop_bp.route("/<int:barbershop_id>/service")
class BarbershopServiceHandler(MethodView):


    @barbershop_bp.response(200, BarbershopServiceSchema(many=True))
    def get(self, barbershop_id):
        barbershop_services_by_barbershop = db.session.execute(
            db.select(BarbershopService).where(BarbershopService.barbershop_id == barbershop_id)
        ).scalars()

        return barbershop_services_by_barbershop


@barbershop_bp.route("/<int:barbershop_id>/payment-method")
class BarbershopPaymentMethodHandler(MethodView):

    @barbershop_bp.response(200, BarbershopPaymentMethodSchema(many=True))
    def get(self, barbershop_id):
        return db.session.execute(
            db.select(BarbershopPaymentMethod).where(BarbershopPaymentMethod.barbershop_id == barbershop_id)
        ).scalars()


    @barbershop_bp.response(201)
    @barbershop_bp.arguments(BarbershopPaymentMethodSchema)
    def post(self, body, barbershop_id):
        
        
        barbershop_payment_method = BarbershopPaymentMethod(
            barbershop_id = barbershop_id,
            payment_method_id = body['payment_method_id']
        )

        db.session.add(barbershop_payment_method)
        db.session.commit()






@barbershop_bp.route("/service")
class BarbershopServiceHandler(MethodView):


    @barbershop_bp.response(201)
    @barbershop_bp.arguments(BarbershopServiceSchema)
    def post(self, barbershop_service):
        barbershop_service = BarbershopService(**barbershop_service)
        db.session.add(barbershop_service)
        db.session.commit() 



