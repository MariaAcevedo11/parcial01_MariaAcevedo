from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['nombre', 'tipo', 'precio']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio