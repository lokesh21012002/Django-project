from django.urls import path, include, re_path
# from .views import *
from student.views.views import *
# from .apiview import CRUD_APIte
# from .genericAPIClassview import CommonView

urlpatterns = [
    re_path(r'^student/$', studentAPI),
    re_path(r'^student/([0-9]+)$', studentAPI),
    path('students', getAllStudents),
    # path('student/<int:id>/', getStudentById),
    # path('student/add/', addStudent),
    # path('student/delete/<int:id>/', deleteStudent),
    # path('student/update/<int:id>/', updateStudent),
    # path('student/<int:id>/', studentAPI),
    # re_path(r'^student/$', studentAPI),
    # re_path(r'^student/([0-9]+)$', studentAPI),

    # path('drf/<int:stu_id>/', CRUD_API),
    # path("generic/", CommonView.as_view())

]
