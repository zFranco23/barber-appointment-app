from marshmallow import Schema, fields

class BarbershopPaymentMethodSchema(Schema):
    id = fields.Integer(dump_only=True)
    barbershop_id = fields.Integer(dump_only=True)
    payment_method_id = fields.Integer(required=True)

    payment_method = fields.Nested('PaymentMethodSchema', dump_only=True, exclude=('id',))