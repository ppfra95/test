from mongoengine import Document, fields


class Clientes(Document):
    nombre = fields.StringField(max_length=30, required=True)
    # direccion = StringField(max_length=30, required=True)
    # email = EmailField(required=True)
    # cel = DecimalField(max_length=10)
