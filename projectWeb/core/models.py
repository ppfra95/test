from django_mongoengine import document
from django_mongoengine.fields import *
from django_mongoengine.mongo_auth.models import User
import datetime
from PIL import Image, ImageShow
from django.conf import settings
import pymongo.errors

"""Models to Service app"""
class Service(document.Document):
    title = StringField(max_length=50)
    content = StringField(max_length=200)
    image = ImageField()
    url_image = StringField(blank=True)
    created = DateTimeField()
    updated = DateTimeField()


    class Meta:
        verbose_name = ['Service']
        verbose_name_plural = ['Services']

    def __str__(self):
        return '%s - Creado %s - Actualizado %s' % (self.title, self.created,
                self.updated)

    def clean(self):
        errors = {}

        if Service.objects(title__exact=self.title).count() > 1 :
            errors[self.title] = ValidationError(
                                """Campo repetido, actualize el
                                existente o cree uno nuevo""",
                                field_name=self.title)

        if errors:
            raise ValidationError('ValidationError', errors=errors)

    def save(self, *args, **kwargs):
        path = settings.MEDIA_URL+"services/"+self.title+".jpg"
        if not self.created:
            self.created = datetime.datetime.now()
            self.url_image=path
        self.updated = datetime.datetime.now()
        img = Image.open(self.image)
        Image.Image.save(img,fp="."+path,formato="JPEG")
        self.image.replace("."+path, content_type='image/JPEG')

        return super(Service, self).save(*args, **kwargs)


"""Models to Blog App"""
class Category(document.Document):
    category = StringField(max_length=50)
    created = DateTimeField()
    updated = DateTimeField()

    class Meta:
        verbose_name = ['Category']
        verbose_name_plural = ['Categories']

    def __str__(self):
        return '%s - Creado %s - Actualizado %s' % (self.category, self.created,
                self.updated)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        return super(Category, self).save(*args, **kwargs)


class Post(document.Document):
    title = StringField(max_length=50)
    content = StringField(max_length=200)
    image = ImageField(null=True,blank=True)
    url_image = StringField(blank=True)
    author = ListField(ReferenceField('User', reverse_delete_rule='CASCADE'))
    category = ListField(ReferenceField('Category', reverse_delete_rule='CASCADE'))
    created = DateTimeField()
    updated = DateTimeField()


    class Meta:
        verbose_name = ['Post']
        verbose_name_plural = ['Posts']

    def __str__(self):
        return '%s - Creado %s - Actualizado %s' % (self.title, self.created,
                self.updated)

    def save(self, *args, **kwargs):
        path = settings.MEDIA_URL+"blog/"+self.title+".jpg"
        if not self.created:
            self.created = datetime.datetime.now()
            self.url_image=path
        self.updated = datetime.datetime.now()
        img = Image.open(self.image)
        Image.Image.save(img,fp="."+path,formato="JPEG")
        self.image.replace("."+path, content_type='image/JPEG')

        return super(Post, self).save(*args, **kwargs)
