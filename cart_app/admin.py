from django.contrib import admin
from .models import *


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'product', 'count', 'total')
