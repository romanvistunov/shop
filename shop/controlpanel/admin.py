from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'fullname', 'email',
                    'city',]


admin.site.register(Client, ClientAdmin)
