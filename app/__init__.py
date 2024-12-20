from flask import Flask
from flask_smorest import Api

from app.controllers.user import user_bp as UserBlueprint
from app.controllers.appointment import appointment_bp as AppointmentBlueprint
from app.controllers.service import service_bp as ServiceBlueprint
from app.controllers.barbershop import barbershop_bp as BarbershopBlueprint
from app.controllers.payment_method import payment_method_bp as PaymentMethodBlueprint


from app.models.user import User
from app.models.appointment import Appointment
from app.models.service import Service
from app.models.barbershop import Barbershop
from app.models.appointment_barbershop_service import AppointmentBarbershopService
from app.models.barbershop_service import BarbershopService
from app.models.payment_method import PaymentMethod
from app.models.barbershop_payment_method import BarbershopPaymentMethod

def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "Barberly API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///barberly_temp.db"

    from app.database.db import db
    db.init_app(app)

    api = Api(app)


    with app.app_context():
        db.create_all()

    # register blueprints

    api.register_blueprint(UserBlueprint, url_prefix="/api/users")
    api.register_blueprint(AppointmentBlueprint, url_prefix="/api/appointments")
    api.register_blueprint(ServiceBlueprint, url_prefix="/api/services")
    api.register_blueprint(BarbershopBlueprint, url_prefix="/api/barbershop")
    api.register_blueprint(PaymentMethodBlueprint, url_prefix="/api/payment-method")

    return app