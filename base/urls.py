from django.urls import path
from . import views


urlpatterns = [
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.registeruser, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('create-room/', views.createroom, name='create-room'),
    path('update-room/<str:pk>/', views.updateroom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteroom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('update-user', views.updateUser, name='update-user'),
    path('topics', views.topicsPage, name='topics'),
    path('activity', views.activityPage, name='activity'),
]