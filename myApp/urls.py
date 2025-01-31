from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_blog, name="create_blog"),
    path('login/', views.login_view, name='login'),
    path('register/', views.UserCreateView.as_view(), name="register"),
    path('signout/', auth_views.logout_view, name="logout"),
]