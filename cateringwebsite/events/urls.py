from django.contrib import admin
from django.urls import path

from . import views

app_name = "events"

urlpatterns = [    
    path('', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"),
    

]
