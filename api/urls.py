from django.urls import include, path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
]