from rest_framework import serializers

from chatfuel_akiza.apps.backend.cliente.models import InformacionInicialCliente

class InformacionInicialClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = InformacionInicialCliente
        fields = ('token', 'fecha_creacion', 'ultimo_cambio', 'nombres', 'nombres', 'correo', 'telefono', 'detalles', 'servicio_seleccionado')
        lookup_field = 'token'
        extra_kwargs = {
            'url': {'lookup_field': 'token'}
        }