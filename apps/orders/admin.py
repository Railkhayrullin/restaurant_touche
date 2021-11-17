from django.contrib import admin
from .models import CartFood, Order


class CartFoodInline(admin.TabularInline):
    model = CartFood
  
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'paid', 'created_at', 'updated_at')
    list_filter = ('paid', 'created_at', 'updated_at', 'status')
    list_editable = ('paid',)
    search_fields = ('id', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CartFoodInline, ]


admin.site.register(Order, OrderAdmin)

