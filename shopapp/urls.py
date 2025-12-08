from .views import shop_index, groups_list, orders_list

from django.urls import path

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups"),
    path("orders/", orders_list, name="orders"),

]