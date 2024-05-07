import uuid

from django.db import models

class InformacionInicialCliente(models.Model):
    SERVICIO_MARCA              = 'MARCA'
    SERVICIO_SAS                = 'SAS'
    SERVICIOS                   = (
                                    (SERVICIO_MARCA, 'Registro de Marca'),
                                    (SERVICIO_SAS, 'Creación de SAS'),
                                )
    
    fecha_creacion              = models.DateTimeField(auto_now_add=True)
    ultimo_cambio               = models.DateTimeField(auto_now=True)
    token                       = models.CharField(max_length=100, null=True)
    nombres                     = models.CharField(max_length=200, null=True)
    correo                      = models.CharField(max_length=100, null=True)
    telefono                    = models.CharField(max_length=20, null=True)
    detalles                    = models.CharField(max_length=500, null=True)
    servicio_seleccionado       = models.CharField(max_length=500, choices=SERVICIOS, null=True)
    
    def __str__(self):
        return str(self.fecha_creacion) + " | " + self.servicio_seleccionado + " | " + self.nombres + " | " +  self.correo
        
    def save(self, **kwargs):
        """ Verifica que el objeto no haya sido modificado por otra sesión """
        if self.token is None or self.token == '':
            self.token = self.generar_token()
        if self.id:
            obj_db = self.__class__.objects.get(pk=self.id)
            # if obj_db.ultimo_cambio > self.ultimo_cambio:
            #     raise ApplicationError(u"El registro ha sido modificado por otra persona, por favor intente nuevamente.")

        models.Model.save(self)
        
    def generar_token(self):
        token = str(uuid.uuid4())
        return token