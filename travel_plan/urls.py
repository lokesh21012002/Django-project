"""
URL configuration for travel_plan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from student.viewset import viewClassSet
from student.modelviewset import viewSetStudent
from rest_framework.authtoken.views import obtain_auth_token
from student.auth import CustomAuth
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# import student


# from .views import *

# from user import views
# import plan
# import user
# from plan import views as view_plan  # Alias solution for multiple views


# from plan.views import plan        Import function directly

router = DefaultRouter()
router.register('api', viewSetStudent, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('authtoken/', obtain_auth_token),  # inbulit
    path('customauth/', CustomAuth.as_view()),  # custom auth
    path('token-jwt/', TokenObtainPairView.as_view(), name="Token"),
    path('refresh-token-jwt/', TokenRefreshView.as_view(), name="Refresh Token"),
    path('verify-jwt/', TokenVerifyView.as_view(), name="Verify Jwt"),







    # path('hello/', parseJson)

    # path('home/', include('student.urls')),
    # path('home',classviews.StudentView.as_view())

    # path('home/', include('user.urls'))
    # path('hello/user/', views.hello),
    # path('hello/name/', views.name),
    # path("hello/<int:id>/", views.dynamic)
    # path("hello/plan", view_plan.plan)
    # path('hello/plan/', plan),



    # path('hello-world/')
]
