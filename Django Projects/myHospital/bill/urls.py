from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view),
    path(r'generate/(?P<case_id>\d+)/', generate),
    path('do_generate/', doGenerate),
    path(r'delete/(?P<id>\d+)/', delete),
    path('pay/', pay),
    path('medicines/', viewMedicine)
]
