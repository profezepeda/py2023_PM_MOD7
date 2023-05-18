from django.contrib import admin
from .models import Clasificacion

# Register your models here.
class ClasificacionAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre',)
  list_filter = ('nombre',)
  search_fields = ('nombre',)
  ordering = ('id', 'nombre',)
  fields = ('nombre',)
  readonly_fields = ('id',)

admin.site.register(Clasificacion, ClasificacionAdmin)