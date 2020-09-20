# from django.contrib import admin

from django_mongoengine import mongo_admin as admin
from core.models import adminUser

@admin.register(adminUser)
class AuthorAdmin(admin.DocumentAdmin):
    pass

# admin.decorators.register(adminUser)
# Register your models here.
