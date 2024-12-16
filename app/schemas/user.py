from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True) 
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

    appointments = fields.List(fields.Nested('AppointmentSchema', only=('id', 'appointment_date',)), dump_only=True)