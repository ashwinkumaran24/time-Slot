from django.contrib import admin
from django.urls import path
from schedule import views

urlpatterns = [
    path('', views.timetable_view, name='timetable'),
]