from django.contrib import admin
from .models import Employees, Devices, History, Access

admin.site.register(Employees)
admin.site.register(History)
admin.site.register(Access)
admin.site.register(Devices)
