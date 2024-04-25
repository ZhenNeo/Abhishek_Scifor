from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view),
    path('generate/', generate),
    path('do_generate/', doGenerate),
    path(r'close/(?P<id>\d+)/', close),
    path(r'delete/(?P<id>\d+)/', delete),
]
