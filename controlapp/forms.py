from django import forms
from .models import Laboratorio, Evento

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ('nombre', 'encargado', 'eventos')

def __init__ (self, *args, **kwargs):
    super(LaboratorioForm, self).__init__(*args, **kwargs)
    self.fields["eventos"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["eventos"].help_text = "agregue el evento"
    self.fields["eventos"].queryset = Evento.objects.all()

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'fecha')
