from django_mongoengine import document, fields
from django_mongoengine.mongo_auth.models import User
from mongoengine import *
import datetime
from PIL import Image, ImageShow
from django.conf import settings
import pymongo.errors


class Service(document.Document):
    title = fields.StringField(max_length=50)
    content = fields.StringField(max_length=200)
    image = fields.ImageField()
    created = fields.DateTimeField()
    updated = fields.DateTimeField()

    class Meta:
        verbose_name = ['Service']
        verbose_name_plural = ['Services']

    def clean(self):
        errors = {}

        if Service.objects(title__exact=self.title).count() != 0:
            errors[self.title] = ValidationError(
                                """Campo repetido, actualize el
                                existente o cree uno nuevo""",
                                field_name=self.title)

        if errors:
            raise ValidationError('ValidationError', errors=errors)

    def __str__(self):
        return '%s - Creado %s - Actualizado %s' % (self.title, self.created,
                self.updated)

    def save(self, *args, **kwargs):
        path ="."+settings.MEDIA_URL+self.title+".jpg"

        if not self.created:
            self.created = datetime.datetime.now()
            img = Image.open(self.image)
            Image.Image.save(img,fp=path,formato="JPEG")
        self.updated = datetime.datetime.now()
        self.image.replace(path, content_type='image/JPEG')

        return super(Service, self).save(*args, **kwargs)
