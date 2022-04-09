from django.contrib import admin

# Register your models here.

from User.models import *

@admin.register(CustomUser)
class ClientAdmin(admin.ModelAdmin):

    list_display = ('username', 'email')