from marshmallow import Schema, fields


class BarberSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    experience_years = fields.Integer(required=True)