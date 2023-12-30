from django.contrib import admin
from .models import cuenta,transaccion,montoefectivo

# Register your models here.
admin.site.register(cuenta)
admin.site.register(transaccion)
admin.site.register(montoefectivo)