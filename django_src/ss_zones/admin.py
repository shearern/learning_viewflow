from django.contrib import admin

from .models import SecurityDevice
from .models import SecurityComponent

admin.site.register(SecurityDevice)
admin.site.register(SecurityComponent)