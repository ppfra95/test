from django_mongoengine.mongo_auth.models import User, Group
from django_mongoengine import mongo_admin as admin
from core.models import *


#register the model admin and group to use in the admin site
@admin.register(Group)
class GroupAdmin(admin.DocumentAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.DocumentAdmin):
     pass


# register the customs models
@admin.register(Service)
class ServiceAdmin(admin.DocumentAdmin):
    readonly_fields=('created','updated')
    exclude = ('url_image',)
    pass


@admin.register(Category)
class CategoryAdmin(admin.DocumentAdmin):
    readonly_fields=('created','updated')
    pass


@admin.register(Post)
class PostAdmin(admin.DocumentAdmin):
    readonly_fields=('created','updated')
    exclude = ('url_image',)
    pass
