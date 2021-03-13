from django.urls import path

from .views import IndexView, HomeView, SobreView, CadView, Cadastro


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('home/', HomeView.as_view(), name="home"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('cad/', CadView.as_view(), name="cad"),
    path('cadastro/', Cadastro.as_view(), name="cadastro"),
]