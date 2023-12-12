from django.urls import path, include
from .views import *
from .apiview import CRUD_API

urlpatterns = [
    path('student/all/', getAllStudents),
    path('student/<int:id>/', getStudentById),
    path('student/add/', addStudent),
    path('student/delete/<int:id>/', deleteStudent),
    path('student/update/<int:id>/', updateStudent),
    path('drf/', CRUD_API)
]
