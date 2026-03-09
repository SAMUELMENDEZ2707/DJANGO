from django.contrib import admin
from users.models import product


@admin.register(product)
class ProdctAdmin(admin.ModelAdmin)
    list_display = ("name", "price", "is_active")
    list_display = ("is_active")
# Register your models here.
