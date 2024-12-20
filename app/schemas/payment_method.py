from marshmallow import Schema, fields

class PaymentMethodSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    


