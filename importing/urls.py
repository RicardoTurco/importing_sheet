from django.urls import path
from importing.views import importar, listagem


urlpatterns = [
    path('importar/', importar, name='importar'),
    path('listagem/', listagem, name='listagem')
]
