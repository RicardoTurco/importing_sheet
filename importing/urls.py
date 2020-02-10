from django.urls import path
from .views import importar, listagem, listagem_v, listagem_d


urlpatterns = [
    path('importar/', importar, name='importar'),
    path('listagem/', listagem, name='listagem'),
    path('listagem_v/<str:listagem_id>', listagem_v, name='listagem_v'),
    path('listagem_d/<str:listagem_id>', listagem_d, name='listagem_d')
]
