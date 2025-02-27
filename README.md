# EstudosDJ
Projeto simples usando CRUD em django
Documentação do Projeto: Integração com API de CEP

Este projeto é uma aplicação Django que permite buscar informações de CEP (Código de Endereçamento Postal) usando a API ViaCEP. Ele oferece funcionalidades para cadastrar, listar, editar e excluir CEPs, além de exibir a cidade e o estado correspondentes ao CEP inserido.
Funcionalidades

    Busca de CEP:

        O usuário pode inserir um CEP, e o sistema busca automaticamente a cidade e o estado correspondentes usando a API ViaCEP.

    CRUD de CEPs:

        Criar: Adicionar um novo CEP ao banco de dados.

        Listar: Visualizar todos os CEPs cadastrados.

        Editar: Atualizar as informações de um CEP existente.

        Excluir: Remover um CEP do banco de dados.

Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e diretórios:
Arquivos do App crud

    forms.py:

        Define o formulário cepForm para cadastrar e editar CEPs.

    models.py:

        Define o modelo cepModel, que armazena o CEP, cidade e estado.

    views.py:

        Contém as views para buscar CEPs e realizar operações CRUD.

    urls.py:

        Define as rotas do app crud.

    tests.py:

        Arquivo para testes automatizados (atualmente vazio).

    Templates:

        form.html: Formulário para cadastrar ou editar CEPs.

        list.html: Lista todos os CEPs cadastrados.

        confirm_delete.html: Confirmação para excluir um CEP.

Arquivos do Projeto Principal

    urls.py:

        Define as rotas principais do projeto, incluindo as rotas do app crud.

Como Funciona
1. Busca de CEP

    Quando o usuário insere um CEP, o sistema faz uma requisição à API ViaCEP (https://viacep.com.br/ws/{cep}/json/).

    Se o CEP for válido, a cidade e o estado são retornados e exibidos ao usuário.

2. CRUD de CEPs

    Criar: O usuário pode cadastrar um novo CEP usando o formulário em form.html.

    Listar: Todos os CEPs cadastrados são exibidos em list.html.

    Editar: O usuário pode atualizar as informações de um CEP existente.

    Excluir: O usuário pode remover um CEP do banco de dados.

Como Usar
1. Instalação

    Clone o repositório do projeto.

    Crie e ative um ambiente virtual:
    bash
    Copy

    python -m venv venv
    source venv/bin/activate  # No macOS/Linux
    venv\Scripts\activate     # No Windows

    Instale as dependências:
    bash
    Copy

    pip install django requests

    Execute as migrações para criar o banco de dados:
    bash
    Copy

    python manage.py migrate

2. Executando o Projeto

    Inicie o servidor de desenvolvimento:
    bash
    Copy

    python manage.py runserver

    Acesse a aplicação no navegador:

        URL base: http://127.0.0.1:8000/

3. Rotas Disponíveis

    Listar CEPs: http://127.0.0.1:8000/listar/

    Cadastrar Novo CEP: http://127.0.0.1:8000/novo/

    Editar CEP: http://127.0.0.1:8000/<id>/editar/

    Excluir CEP: http://127.0.0.1:8000/<id>/deletar/

Exemplos de Uso
1. Cadastrar um Novo CEP

    Acesse http://127.0.0.1:8000/novo/.

    Insira o CEP no formulário.

    Clique em Salvar.

    O CEP será cadastrado e exibido na lista de CEPs.

2. Listar CEPs Cadastrados

    Acesse http://127.0.0.1:8000/listar/.

    Todos os CEPs cadastrados serão exibidos em uma tabela.

3. Editar um CEP

    Na lista de CEPs, clique em Editar ao lado do CEP desejado.

    Atualize as informações no formulário.

    Clique em Salvar.

4. Excluir um CEP

    Na lista de CEPs, clique em Excluir ao lado do CEP desejado.

    Confirme a exclusão no formulário de confirmação.

Melhorias Futuras

    Validação de CEP:

        Adicionar validação para garantir que o CEP inserido seja válido.

    Autenticação:

        Implementar autenticação para proteger as operações CRUD.

    Testes Automatizados:

        Escrever testes unitários e de integração no arquivo tests.py.

    Interface Melhorada:

        Usar um framework CSS (ex.: Bootstrap) para melhorar a aparência da interface.

Conclusão

Este projeto é uma aplicação simples, mas poderosa, para gerenciar CEPs usando Django e a API ViaCEP. Ele serve como uma base sólida para expandir e adicionar funcionalidades mais avançadas. Sinta-se à vontade para contribuir e melhorar o projeto! 😊
Códigos de Exemplo
views.py
python
Copy

from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
import requests
from django.shortcuts import render
from .models import cepModel
from .forms import cepForm

def get_cep(request):
    cep = request.GET.get('cep')
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
        dado_cep = response.json()
        cepModel = {
            'cep': dado_cep['cep'],
            'cidade': dado_cep['localidade'],
            'estado': dado_cep['estado']
        }
    return render(request, 'crud/list.html', {'cepModel': cepModel})    

class crudCreateView(FormView):
    template_name = 'crud/form.html'
    form_class = cepForm
    success_url = reverse_lazy('novo_cep')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class crudListView(ListView):
    model = cepModel
    template_name = 'crud/list.html'
    context_object_name = 'ceps'

class crudUpdateView(UpdateView):
    model = cepModel
    fields = ['cep' , 'cidade', 'estado']
    template_name = 'crud/form.html'
    success_url = reverse_lazy('cep_update')

class crudDeleteView(DeleteView):
    model = cepModel
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('cep_delete')

urls.py (App crud)
python
Copy

from django.urls import path
from .views import crudCreateView, crudListView, crudUpdateView, crudDeleteView

urlpatterns = [
    path('listar/' , crudListView.as_view(), name='listar_cep'),
    path('novo/' , crudCreateView.as_view(), name='novo_cep'),
    path('<int:pk>/editar/', crudUpdateView.as_view(), name='cep_update'),
    path('<int:pk>/deletar/', crudDeleteView.as_view(), name='cep_delete'),
]

form.html
html
Copy

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FORM_CEP</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p}}
        <button type="submit">Salvar</button>
        <a href=" {% url 'listar_cep' %}">Listar</a>
    </form>
</body>
</html>

Run HTML
list.html
html
Copy

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de CEPs</title>
</head>
<body>
    <h1>Lista de CEPs</h1>
    <ul>
        {% for cep in ceps %}
            <li>{{ cep.cep }} - {{ cep.cidade }}/{{ cep.estado }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'novo_cep' %}">Adicionar Novo CEP</a>
</body>
</html>

Run HTML
