from django.urls import path, include
from .views import *
# from .apiview import CRUD_APIte
# from .genericAPIClassview import CommonView

urlpatterns = [
    path('students/', getAllStudents),
    path('student/<int:id>/', getStudentById),
    path('student/add/', addStudent),
    path('student/delete/<int:id>/', deleteStudent),
    path('student/update/<int:id>/', updateStudent),
    # path('drf/<int:stu_id>/', CRUD_API),
    # path("generic/", CommonView.as_view())

]
