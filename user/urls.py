
from django.urls import path
from user import views

from django.views import *

urlpatterns = [
    path('hello/user/<int:id>/', views.getALlUsers,
         {"username": "lokesh", "password": "password"}),
    path('hello/user/<int:id>/<int:sub_id>/', views.gettAllUserByExtra),

    path('all/', views.all),
    path('class/', views.ClassView.as_view(), name='demo')







]
