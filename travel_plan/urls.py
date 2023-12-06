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

from .views import *

# from user import views
# import plan
# import user
# from plan import views as view_plan  # Alias solution for multiple views


# from plan.views import plan        Import function directly


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', parseJson)

    # path('home/', include('plan.urls')),

    # path('home/', include('user.urls'))
    # path('hello/user/', views.hello),
    # path('hello/name/', views.name),
    # path("hello/<int:id>/", views.dynamic)
    # path("hello/plan", view_plan.plan)
    # path('hello/plan/', plan),



    # path('hello-world/')
]
