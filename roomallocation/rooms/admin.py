from django.contrib import admin

# Register your models here.
from .models import Flat, Floor, Application
admin.site.register(Flat)
admin.site.register(Floor)
admin.site.register(Application)
