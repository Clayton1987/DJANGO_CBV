from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoModelForm
from django.urls import reverse_lazy



# Create your views here.
class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome','preco']
    success_url = reverse_lazy('index')