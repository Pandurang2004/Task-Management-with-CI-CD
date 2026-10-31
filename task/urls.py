from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_task, name='add_task'),
    path('read', views.read_task, name='read_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    
]