from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "member"

urlpatterns = [
    path('login/', views.login_user, name="login_user"),
    path('register/', views.register_user, name="register"),
    path('logout/', views.logout_user, name="logout_user"),
    path('profile/<str:user>/', views.user_profile, name= "user_profile"),
    path('profile/edit/<str:user>/', views.edit_profile, name= "edit_profile"),
    path('profile/edit/arch/<str:user>/', views.architect_profile, name= "architect_profile"),
    path('profile/edit/const/<str:user>/', views.const_profile, name= "const_profile"),
    path('profile/edit/edu/<str:user>/', views.edu_profile, name= "edu_profile"),
]