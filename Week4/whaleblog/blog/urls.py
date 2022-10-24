from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', views.view_post, name='post_view'),
    path('<slug:slug>/like', views.like_post, name='post_like'),
]
