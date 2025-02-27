from django.urls import path
from .views import crudCreateView, crudListView, crudUpdateView, crudDeleteView

urlpatterns = [
    path('listar/' , crudListView.as_view(), name='listar_cep'),
    path('novo/' , crudCreateView.as_view(), name='novo_cep'),
    path('<int:pk>/editar/', crudUpdateView.as_view(), name='cep_update'),
    path('<int:pk>/deletar/', crudDeleteView.as_view(), name='cep_delete'),
]
