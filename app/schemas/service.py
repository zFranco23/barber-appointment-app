from marshmallow import Schema, fields

class ServiceSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True)
                                