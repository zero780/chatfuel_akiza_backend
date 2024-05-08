from django.urls import path

from rest_framework.routers import DefaultRouter

from chatfuel_akiza.apps.backend.api.cliente.views import InformacionInicialClienteViewSet

router = DefaultRouter()

# router.register(r'transaccion', TransaccionViewSet)
router.register(r'cliente', InformacionInicialClienteViewSet)

url_patterns = [
]

router = router.urls + url_patterns
