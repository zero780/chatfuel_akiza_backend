from django.contrib import admin

from chatfuel_akiza.apps.backend.cliente.models import InformacionInicialCliente

class InformacionInicialClienteAdmin(admin.ModelAdmin):
    model = InformacionInicialCliente
    search_fields       = ['servicio_seleccionado', 'nombres', 'correo']
    list_display        = ('servicio_seleccionado', 'nombres', 'correo')
    list_filter         = ('servicio_seleccionado', 'nombres', 'correo')
    exclude             = ('token',)

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()
        
        
admin.site.register(InformacionInicialCliente, InformacionInicialClienteAdmin)