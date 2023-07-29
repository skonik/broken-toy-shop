from django.contrib import admin

from toys.models import Order, Toy


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("toy", "user")
