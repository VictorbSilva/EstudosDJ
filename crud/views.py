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