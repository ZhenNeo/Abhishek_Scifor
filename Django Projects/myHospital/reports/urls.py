from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view),
    path('generate/', generate),
    path('do_generate/', doGenerate),
    path(r'change/(?P<id>\d+)/', change),
    path('do_change/', doChange),
    path(r'delete/(?P<id>\d+)/', delete),
]
