from django.urls import path
from .views import polls_detail, home_detail, create_user, auth_user, logout_user

urlpatterns = [
    path('', home_detail, name='home_detail'),
    path('login/', auth_user, name='login'),
    path('register/', create_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('<path>/', polls_detail, name='polls_detail'),
]
