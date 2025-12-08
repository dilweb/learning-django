from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpRequest
from django.shortcuts import render

from .models import Order


def shop_index(request: HttpRequest):
    context = {
        "time_running" : default_timer,
    }
    return render(request, "shopapp/shop-index.html", context=context)

def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.all()
    }
    return render(request, "shopapp/groups-list.html", context=context)

def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").all()
    }
    return render(request, "shopapp/orders-list.html", context=context)
