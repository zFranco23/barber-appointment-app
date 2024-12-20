from marshmallow import Schema, fields


class BarbershopSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    experience_years = fields.Integer(required=True)