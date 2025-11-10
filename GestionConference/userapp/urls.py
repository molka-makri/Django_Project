from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'userapp'

urlpatterns = [
    path("", views.RegisterView.as_view(), name="register"),  # URL pour /users/
    path("register/", views.RegisterView.as_view(), name="register_form"),  # URL pour /users/register/
    path("register-debug/", views.register, name="register_debug"),  # URL de débogage
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
]