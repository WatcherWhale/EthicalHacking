from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logoutaccount, name='logout'),
    path('login/', views.loginaccount, name='login'),
]
