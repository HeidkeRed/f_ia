from django import forms
from .models import Artista, CancionFavorita, CancionSimilar

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre']

class CancionFavoritaForm(forms.ModelForm):
    class Meta:
        model = CancionFavorita
        fields = ['titulo', 'artista']

class CancionSimilarForm(forms.ModelForm):
    class Meta:
        model = CancionSimilar
        fields = ['titulo']
