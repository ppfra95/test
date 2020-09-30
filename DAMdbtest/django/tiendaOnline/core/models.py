from django_mongoengine import document, fields
from django_mongoengine.mongo_auth.models import User
from mongoengine import *


class Customer(document.Document):
    name = fields.StringField(max_length=30)
    last_Name = fields.StringField(max_length=30)
    age=fields.IntField(max_length=3,min_length=1)
    address = fields.StringField(max_length=30)
    email = fields.EmailField()
    cell_Phone = fields.IntField(max_length=10,min_length=10)

    def __str__(self):
        return '%s - %s -%s -%s -%s' % (self.name, self.last_Name, self.address, self.email, self.cell_Phone)

#
# class Item(document.Document):
#     name = fields.StringField(max_length=30)
#     seccion = fields.StringField(max_length=30)
#     cost = fields.FloatField(max_length=10)
#     discount = fields.IntField(max_length=2,blank=True)
#
#     def __str__(self):
#         return '%s - %s -%s -%s' % (self.name, self.seccion, self.cost, self.discount)
#
# class Order(document.Document):
#     no_Order = fields.IntField(max_length=20)
#     date = fields.DateTimeField()
#     status = fields.BooleanField()
#
#     def __str__(self):
#         return '%s - %s -%s' % (self.no_Order, self.date, self.status)
#
#
# class FContacto(document.Document):
#     subject=fields.StringField(max_length=70)
#     email=fields.EmailField()
#     message=fields.StringField(max_length=500)
#
#     def __str__(self):
#         return '%s - %s -%s' % (self.subject, self.email, self.message)
