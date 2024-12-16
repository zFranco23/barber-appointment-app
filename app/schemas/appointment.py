from marshmallow import Schema, fields  

from app.schemas.service import ServiceSchema


class AppointmentSchema(Schema):
    id = fields.Integer(dump_only=True)
    appointment_date = fields.Str(required=True)
    service_id = fields.Integer(required=True)
    # barber_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)


    ## nested schemas
    user = fields.Nested('UserSchema', only=('id', 'name'), dump_only=True)
    # barber = fields.Nested(BarberSchema)
    service = fields.Nested(ServiceSchema( only=('id', 'name', 'price')),  dump_only=True)



