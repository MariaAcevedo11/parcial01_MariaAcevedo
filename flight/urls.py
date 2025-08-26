from django.urls import path
from .views import RegistrarPageView, ListarPageView, EstadisticasPageView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("registrar/", RegistrarPageView.as_view(), name="registrar_vuelo"),
    path("listar/", ListarPageView.as_view(), name="listar_vuelos"),
    path("estadisticas/", EstadisticasPageView.as_view(), name="estadisticas_vuelos"),
]