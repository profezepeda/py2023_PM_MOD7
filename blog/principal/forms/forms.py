from django import forms

class FormularioPublicacion(forms.Form):
  id = forms.IntegerField(required=False, widget=forms.HiddenInput())
  titulo = forms.CharField(label='Título', max_length=200, required=True)
  bajada = forms.CharField(label='Bajada', max_length=200, required=False)
  contenido = forms.CharField(label='Contenido', widget=forms.Textarea, required=True)
  fecha_publicacion = forms.DateTimeField(label='Fecha de publicación', required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))
  autor_id = forms.IntegerField(label='Autor', required=False)
  clasificacion_id = forms.IntegerField(label='Clasificación', required=False)