from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .models import Pessoa


def cadastro(request):
    pessoas = Pessoa.objects.all()

    context = {
        'pessoas': pessoas,

    }
    return render(request, 'paginas/cadastro.html', context)
    

class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

class CadView(TemplateView):
    template_name = 'cad.html'

class Cadastro(TemplateView):
    template_name = 'cadastro.html'

