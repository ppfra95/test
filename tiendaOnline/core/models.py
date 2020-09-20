from django_mongoengine import Document, fields
from django_mongoengine.mongo_auth.models import User
from mongoengine import *



class adminUser(User):
    # USERNAME_FIELD = 'username'
    # # email=fields.EmailField()
    # # passw=fields.StringField(max_length=30)
    # # REQUIRED_FIELDS =([email,passw])
    #
    # REQUIRED_FIELDS =(['email'])
    pass



class Customers(Document):
    Name = fields.StringField(max_length=30)
    Last_Name = fields.StringField(max_length=30)
    Address = fields.StringField(max_length=30)
    Email = fields.EmailField()
    Cell_Phone = fields.IntField(max_length=10,min_length=10)

class Items(Document):
    Name = fields.StringField(max_length=30)
    Seccion = fields.StringField(max_length=30)
    Cost = fields.FloatField(max_length=10)
    Discount = fields.IntField(max_length=2,blank=True)

class Orders(Document):
    No_Order = fields.IntField(max_length=20)
    Date = fields.DateTimeField()
    Status = fields.BooleanField()
