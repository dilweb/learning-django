from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin

class OrderInline(admin.TabularInline):
    model = Order.products.through


@admin.action(description="Mark selected products as archived")
def mark_archived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet[Product]
) -> None:
    queryset.update(archived=True)


@admin.action(description="Mark selected products as unarchived")
def mark_unarchived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet[Product]
) -> None:
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = "name", "description"
    fieldsets = [
        (None, {"fields": ("name", "description")}),
        (
            "Price options",
            {
                "fields": ("price", "discount"),
                "classes": ("collapse",),
            },
        ),
        (
            "Additional options",
            {
                "fields": ("archived",),
                "classes": ("collapse",),
                "description": "Archived products are not displayed in the store",
            },
        ),
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
    list_display = "delivery_address", "promo", "created_at", "user_verbose", "zalupa"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username

    # ordering = "pk",
    # search_fields = "delivery_address", "promocode", "created_at", "user__username"

    # def user_verbose(self, obj: Order) -> str:
    #     return obj.user.first_name or obj.user.username
