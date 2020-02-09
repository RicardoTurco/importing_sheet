from django.urls import path
from importing.views import importar


urlpatterns = [
    path('importar/', importar, name='importar')
]
