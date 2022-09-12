from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
     path('', views.index,name='index'),
     path('addNewNote', views.addNewNote,name='addNewNote'),
     path('updateNote', views.updateNote,name='updateNote'),
     path('pin', views.pin,name='pin'),
     path('unpin', views.unpin,name='unpin'),
     path('delete', views.delete,name='delete'),
     
]