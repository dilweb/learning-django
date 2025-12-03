from django.contrib import admin

from .models import Product, Order

# admin.site.register(Product, ProductAdmin)


class OrederInLine(admin.TabularInline):
     model = Order.products.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrederInLine,
    ]
    list_display = "pk", "name", "description_short", "price", "discount"
    list_display_links = "pk", "name"
    ordering = "pk",
    search_fields = "name", "description"
    fieldsets = [
         (None, {
              "fields": ("name", "description")
         }),
         ("Price options", {
             "fields": ("price", "discount"),
             "classes": ("collapse",),
         }),
         ("Additional options", {
             "fields": ("archived",),
             "classes": ("collapse",),
             "description": "Archived products are not displayed in the store"
         })
    ]

def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class ProductInline(admin.StackedInline):
    model = Product.orders.through


@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promo", "created_at", "user_verbose"

    def get_queryset(self, request):
         return Order.objects.select_related("user").prefetch_related("products")
    
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
    # ordering = "pk",
    # search_fields = "delivery_address", "promocode", "created_at", "user__username"

    # def user_verbose(self, obj: Order) -> str:
    #     return obj.user.first_name or obj.user.username
