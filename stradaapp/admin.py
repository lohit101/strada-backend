from django.contrib import admin
from .models import Product, Order, Message

# Register your models here.
admin.site.register(Product)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["fname", "lname", "phone", "email", "address1", "address2", "landmark", "city", "state", "country", "zipcode", "ordervalue", "total", "created"]
    list_display = ("fname", "completed", "total", "created")
    ordering = ("completed",)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ["fname", "lname", "email", "message", "created"]
    list_display = ("email", "created")