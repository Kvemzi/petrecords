from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]