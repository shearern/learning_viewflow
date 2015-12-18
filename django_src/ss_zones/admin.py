from django.contrib import admin

# Register your models here.

from .models import SecurityDevice
from .models import SecurityComponent

admin.site.register(SecurityDevice)
admin.site.register(SecurityComponent)