import datetime
from decimal import Decimal

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse

from django.template import Template, Context

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from chatfuel_akiza.apps.backend.api.cliente.serializers import InformacionInicialClienteSerializer
from chatfuel_akiza.apps.backend.cliente.models import InformacionInicialCliente
from django.conf import settings

class JSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        # TODO: los formatos de las fechas deben estar relacionados a settings
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%d/%m/%Y, %I:%M:%S %p')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%d/%m/%Y')
        elif isinstance(obj, datetime.time):
            return obj.strftime('%I:%M %p')
        elif isinstance(obj, Decimal):
            return str(obj.__float__())
        return DjangoJSONEncoder.default(self, obj)
    
def jsonx(data):
    data = {"json_data": JSONEncoder(ensure_ascii=False).encode(data)}
    template = Template("{{json_data|safe}}")
    context = Context(data)
    return HttpResponse(template.render(context),
                        content_type="text/json-comment-filtered; charset=%s" % (settings.DEFAULT_CHARSET))
    
class InformacionInicialClienteViewSet(viewsets.ModelViewSet):
    queryset = InformacionInicialCliente.objects.all().order_by('-pk')
    serializer_class = InformacionInicialClienteSerializer
    lookup_field = 'token'
    permission_classes = []
    authentication_classes = []
    
    def get_queryset(self):
        queryset = self.queryset

        return queryset
    
    @action(detail=False, url_path='guardar-info-inicial-cliente', methods=['POST'], permission_classes=[AllowAny])
    def guardar_info_inicial_cliente(self, request):
        try:
            print("guardar_info_inicial_cliente")
            data = request.data
            print(data)
            print("==========================================")
            
            return HttpResponse()

        except Exception as err:
            print("EXCEP ERROR")
            print(str(err))
            return jsonx({'status': 'error', 'message': str(err), 'data': False})