from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_post/', views.add_post, name="add_post"),
    path('update_blog/<str:pk>/', views.update_blog, name="update_blog"),
    path('delete_post/<str:pk>/', views.delete_post, name="delete_student"),
]
