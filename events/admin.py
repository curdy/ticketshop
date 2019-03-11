from django.contrib import admin
from .models import Event

class AdminTheme(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Event, AdminTheme)
