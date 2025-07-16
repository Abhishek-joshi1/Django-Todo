from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
    path('markAsUnDone/<int:pk>/', views.markAsUnDone, name='markAsUnDone'),
    path('Edit_Task/<int:pk>/', views.Edit_Task, name='Edit_Task'),
    path('Delete_Task/<int:pk>/', views.Delete_Task, name='Delete_Task'),
]
