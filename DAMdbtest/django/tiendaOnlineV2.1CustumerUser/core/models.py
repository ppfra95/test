import binascii
import os

from django_mongoengine.mongo_auth.models import User, MongoUserManager, \
                                                 AbstractUser,\
                                                 make_password

from mongoengine import document, fields, CASCADE, signals


__all__ = ['Token', 'Customer']

class UserManager(MongoUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')

        user = Customer(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# class CustomerData(object):
#     """docstring for CustomerData."""
#
#     def __init__(self, arg):
#         super(CustomerData, self).__init__()
#         self.arg = arg


class Customer(AbstractUser):
    # first_name = fields.StringField(max_length=50)
    age=fields.IntField(max_length=3,min_length=1)
    address = fields.StringField(max_length=40)
    email = fields.EmailField(max_length=255, unique=True)
    cell_Phone = fields.IntField(max_length=10,min_length=10)
    # username =fields.StringField(blank=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)

    # objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=()


    def __str__(self):
        return '%s - %s' % (self.first_name, self.email)

    # def save(self, *args, **kwargs):
    #     # self.password=make_password(self.password)
    #     self.username=self.email
    #     return super(Customer, self).save(*args, **kwargs)


class Token(document.Document):
    """
    The default authorization token model.
    """
    key = fields.StringField(required=True, max_length=40)
    user = fields.ReferenceField(
        Customer, verbose_name='username',
        reverse_delete_rule=CASCADE, null=True
    )
    created = fields.DateTimeField(auto_now_add=True)

    meta = {
        'indexes': ['key', ],
        'collection': 'user_token'
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if not document.key:
            document.key = document.generate_key()

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
