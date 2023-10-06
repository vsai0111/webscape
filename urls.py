from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('view/', views.view_bookmarks, name='view_bookmarks'),
]
