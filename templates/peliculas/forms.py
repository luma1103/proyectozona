from django import forms
from .models import Pelicula, Actor

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('nombre', 'anio', 'actores')

def __init__ (self, *args, **kwargs):
    super(PeliculaForm, self).__init__(*args, **kwargs)
    self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["actores"].help_text = "Ingrese los Actores que participaron en la película"
    self.fields["actores"].queryset = Actor.objects.all()
