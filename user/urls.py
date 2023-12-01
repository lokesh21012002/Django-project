
from django.urls import path
from user import views

urlpatterns = [
    path('hello/user/<int:id>/', views.getALlUsers,
         {"username": "lokesh", "password": "password"}),
    path('hello/user/<int:id>/<int:sub_id>/', views.gettAllUserByExtra)


]
