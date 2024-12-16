from flask_smorest import Blueprint
from flask.views import MethodView

from app.database.db import db

from app.schemas.service import ServiceSchema
from app.models.service import Service


service_bp = Blueprint('service', __name__, description='Service related operations')



@service_bp.route('/')
class ServiceHandler(MethodView):

    ''' Get all services'''
    @service_bp.response(200, ServiceSchema(many=True))
    def get(self):

        services = db.session.execute(
            db.select(Service)
        ).scalars()

        return services
    

    ''' Create new services'''
    @service_bp.response(201)
    @service_bp.arguments(ServiceSchema)
    def post(self, body):
        service = Service(**body)
        db.session.add(service)
        db.session.commit() 


