from django.contrib import admin
from .models import User, History, Access

admin.site.register(User)
admin.site.register(History)
admin.site.register(Access)