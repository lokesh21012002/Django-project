from django.contrib import admin
from plan.models import Plan

# Register your models here.


class TravelAdminModel(admin.ModelAdmin):
    list_display = ("id", 'name', 'destination', 'description')


admin.site.register(Plan, TravelAdminModel)
