from marshmallow import Schema, fields


class BarbershopSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    start_operations_date = fields.DateTime(required=True) 
    address = fields.Str(required=True)
    start_hour = fields.DateTime(required=True)
    end_hour = fields.DateTime(required=True)

    payment_methods= fields.List(fields.Nested('BarbershopPaymentMethodSchema', dump_only=True, only=('id', 'payment_method'))) 