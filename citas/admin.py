from django.contrib import admin
from .models import procedimientos

# Register your models here.
class procedimientosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'dni', 'procedimientos', 'celular', 'doctor', 'fecha_de_cita')
    list_filter = ('procedimientos', 'doctor', 'fecha_de_cita') 
    
admin.site.register(procedimientos, procedimientosAdmin)
