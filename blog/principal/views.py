from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from principal.forms.forms import FormularioPublicacion
from django.contrib.auth.models import User
from datetime import datetime, date

from principal.models import Clasificacion, Publicacion

# Create your views here.
# Publicaciones

def index_view(request):
  return render(request, 'index.html', {})

class PublicacionListView(TemplateView):
  template_name = 'publicaciones/registros.html'
  
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context["publicaciones"] = Publicacion.objects.all()
    return context

class PublicacionEditView(TemplateView):
  template_name = 'publicaciones/registro.html'

  def get(self, request, *args: Any, **kwargs: Dict[str, Any]):
    form = FormularioPublicacion()
    if kwargs['pk'] != 0:
      publicacion = Publicacion.objects.get(id=kwargs['pk'])
      form.fields['titulo'].initial = publicacion.titulo
      form.fields['bajada'].initial = publicacion.bajada
      form.fields['contenido'].initial = publicacion.contenido
      if publicacion.fecha_publicacion is not None:
        form.fields['fecha_publicacion'].initial = datetime.date(publicacion.fecha_publicacion).strftime('%Y-%m-%d')
      form.fields['autor_id'].initial = publicacion.autor_id
      form.fields['clasificacion_id'].initial = publicacion.clasificacion_id
    data = {
      'form': form,
      'usuarios': [],
      'clasificaciones': []
    }
    data["usuarios"] = User.objects.all()
    data["clasificaciones"] = Clasificacion.objects.all()
    return render(request, self.template_name, data)

  # def get_context_data(self, **kwargs: Any):
  #   context = super().get_context_data(**kwargs)
  #   form = FormularioPublicacion()
  #   # context["publicacion"] = Publicacion.objects.get(pk=kwargs['pk'])
  #   context["form"] = form
  #   return context
  
  def post(self, request, *args: Any, **kwargs: Dict[str, Any]):
    form = FormularioPublicacion(request.POST)
    if form.is_valid():
      if kwargs['pk'] == 0:
        publicacion = Publicacion()
      else:
        publicacion = Publicacion.objects.get(id=kwargs['pk'])
      publicacion.titulo = form.cleaned_data['titulo']
      publicacion.bajada = form.cleaned_data['bajada']
      publicacion.contenido = form.cleaned_data['contenido']
      publicacion.fecha_publicacion = form.cleaned_data['fecha_publicacion']
      publicacion.autor_id = form.cleaned_data['autor_id']
      publicacion.clasificacion_id = form.cleaned_data['clasificacion_id']
      publicacion.save()
      data = {
        'form': form,
        'usuarios': [],
        'clasificaciones': []
      }
      data["usuarios"] = User.objects.all()
      data["clasificaciones"] = Clasificacion.objects.all() 
      return redirect('publicaciones')
    else:
      return render(request, 'publicaciones/registro.html', data)

class PublicacionDeleteView(TemplateView):
  pass