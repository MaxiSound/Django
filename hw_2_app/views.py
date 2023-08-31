import datetime
from datetime import timedelta, date
from django.db import models
from django.shortcuts import render
from hw_2_app.models import Order


def get_orders(request, client_id):
    orders = Order.objects.filter(customer__pk=client_id)
    context = {'orders': orders}
    return render(request, 'orders.html', context)


def get_history(request, client_id, days_before):
    orders = (Order.objects.filter(customer__pk=client_id)) and Order.objects.filter(
        date_ordered__gt=(datetime.date.today() - timedelta(days=days_before)))
    context = {'orders': orders}
    return render(request, 'orders.html', context)
