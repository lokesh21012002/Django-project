from django.contrib import admin
from user.models import User
# Register your models here.


# @admin.register(User, UserAdminModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ("id", 'username',  'email', 'phone')


# @admin.register(User, UserAdminModel)
admin.site.register(User, UserAdminModel)
