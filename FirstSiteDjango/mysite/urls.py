from django.urls import path, include
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('', home_detail, name='home_detail'),
    path('login/', auth_user, name='login'),
    path('register/', creat_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('next/', home_detail, name='home_detail'),
]
