from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'userapp'

urlpatterns = [
    path("", views.register, name="register"),  # URL pour /users/
    path("register/", views.register, name="register_form"),  # URL pour /users/register/
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]