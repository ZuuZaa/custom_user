from django.urls import path
from .views import RegistrationView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
