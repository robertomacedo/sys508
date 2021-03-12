from django.urls import path

from .views import IndexView, HomeView, SobreView, CadView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('home/', HomeView.as_view(), name="home"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('cad/', CadView.as_view(), name="cad"),
]