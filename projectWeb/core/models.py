from django_mongoengine import document, fields
from django_mongoengine.mongo_auth.models import User
from mongoengine import *
import datetime
from PIL import Image
from django.conf import settings


class Service(document.Document):
    title = fields.StringField(max_length=50)
    content = fields.StringField(max_length=200)
    image = fields.ImageField()
    created = fields.DateTimeField(defaul=datetime.datetime.now)
    updated = fields.DateTimeField(defaul=datetime.datetime.now)

    class Meta:
        verbose_name = ['Service']
        verbose_name_plural = ['Services']

    # def __str__(self):
    #     return '%s - %s -%s -%s -%s' % (self.title, self.content, self.created,
    #             self.updated)
    def __str__(self):
        return '%s' % (self.image)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
            # self.image.put()
        self.updated = datetime.datetime.now()

        img = Image.open(self.image)
        # img.show()
        Image.Image.save(img,fp=settings.MEDIA_URL+"1.PNG",formato="PNG")
        # print(self.image._fs)
        # print(self.image.grid_id)
        # print(self.image.key)
        # print(self.image.instance)
        # print(self.image.db_alias)
        # print(self.image.collection_name)
        # print(self.image.newfile)
        # print(self.image.gridout)


        return super(Service, self).save(*args, **kwargs)
