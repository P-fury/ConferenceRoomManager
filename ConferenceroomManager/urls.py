"""
URL configuration for ConferenceroomManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RoomManager import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.MainView.as_view(), name='main'),
    path('about/', views.about, name='about'),
    path('rooms', views.rooms, name='rooms'),
    path('room/<int:id>', views.room_details, name='RoomDetails'),
    path('room/new/', views.AddRoom.as_view(), name='AddRoom'),
    path('room/edit/<int:id>', views.RoomEdit.as_view(), name='EditRoom'),
    path('room/delete/<int:id>', views.RoomDelete.as_view(), name='RoomDelete'),
    path('room/reserve/<int:id>', views.RoomReserve.as_view(), name='RoomReserve'),

]
