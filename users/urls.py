from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.RegisterUser.as_view()),
    path("accounts/login/", views.LoginView.as_view()),
    path("accounts/refresh/", jwt_views.TokenRefreshView.as_view()),
]