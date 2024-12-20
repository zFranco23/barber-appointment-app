from marshmallow import Schema, fields

class BarbershopServiceSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    barbershop_id = fields.Integer(dump_only=True)
    service_id = fields.Integer(required=True)
    price = fields.Float(required=True)
    hours_duration = fields.Integer(required=True)

    service = fields.Nested('ServiceSchema', dump_only=True)


