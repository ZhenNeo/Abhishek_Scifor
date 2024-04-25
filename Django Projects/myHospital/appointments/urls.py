from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view),
    path('book/', book),
    path('do_book/', doBook),
    path(r'change_appointment/(?P<id>\d+)/', changeAppointment),
    path('do_change/', doChange),
    path(r'delete/(?P<id>\d+)/', delete),
]
