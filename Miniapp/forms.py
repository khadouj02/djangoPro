from django import forms
from .models import Intervenant
from .models import Client
from .models import Intervention

class IntervenantForm(forms.ModelForm):
    class Meta:
        model = Intervenant
        fields = ['nom', 'prenom', 'post']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'direction']


class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ['date', 'type', 'motive', 'etat','id_intervenant','id_client']

    