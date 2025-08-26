from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg


class HomePageView(TemplateView):
    template_name = "home.html"

class RegistrarPageView(TemplateView):
    template_name = "registrar_vuelo.html"

    def get(self, request, *args, **kwargs):
        form = FlightForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_vuelos")  # redirige a la lista después de guardar
        return render(request, self.template_name, {"form": form})


class ListarPageView(TemplateView):
    template_name = "listar_vuelos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # vuelos ordenados por precio ascendente
        context["vuelos"] = Flight.objects.all().order_by("precio")
        return context

class EstadisticasPageView(TemplateView):
    template_name = "estadisticas_vuelos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Contar vuelos por tipo
        context["nacionales"] = Flight.objects.filter(tipo="NACIONAL").count()
        context["internacionales"] = Flight.objects.filter(tipo="INTERNACIONAL").count()

        # Promedio de precio solo para nacionales
        promedio = Flight.objects.filter(tipo="NACIONAL").aggregate(Avg("precio"))
        context["promedio_nacionales"] = promedio["precio__avg"]

        return context