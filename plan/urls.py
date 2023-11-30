from django.urls import path


from plan import views

urlpatterns = [
    path('hello/plan/', views.plan)
]
