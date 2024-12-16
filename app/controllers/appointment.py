from flask.views import MethodView
from flask_smorest import Blueprint

from app.database.db import db

from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentSchema



appointment_bp = Blueprint('appointment', __name__, description='Appointment related operations')


@appointment_bp.route('/')
class AppointmentHandler(MethodView):

    ''' Get all appointments'''
    @appointment_bp.response(200, AppointmentSchema(many=True))
    def get(self):
        appointments = db.session.execute(
            db.select(Appointment)
        ).scalars()

        return appointments

        
    ''' Create new user'''
    @appointment_bp.response(201, AppointmentSchema)
    @appointment_bp.arguments(AppointmentSchema)
    def post(self, body):
    
        appointment = Appointment(**body)

        db.session.add(appointment)
        db.session.commit()


        return appointment

