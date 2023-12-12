from django.urls import path, include
from .views import *
from .apiview import CRUD_API
from .genericAPIClassview import CommonView

urlpatterns = [
    path('student/all/', getAllStudents),
    path('student/<int:id>/', getStudentById),
    path('student/add/', addStudent),
    path('student/delete/<int:id>/', deleteStudent),
    path('student/update/<int:id>/', updateStudent),
    path('drf/<int:stu_id>/', CRUD_API),
    path("generic/", CommonView.as_view())

]
