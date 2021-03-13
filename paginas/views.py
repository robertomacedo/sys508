from django.views.generic import TemplateView

from django.shortcuts import render, redirect



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

