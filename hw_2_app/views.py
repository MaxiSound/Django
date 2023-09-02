import datetime
from datetime import timedelta, date
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.shortcuts import render
from hw_2_app.models import Order
from hw_2_app.forms import ProductForm
from hw_2_app.models import Product


def get_orders(request, client_id):
    orders = Order.objects.filter(customer__pk=client_id)
    context = {'orders': orders}
    return render(request, 'orders.html', context)


def get_history(request, client_id, days_before):
    orders = (Order.objects.filter(customer__pk=client_id)) and Order.objects.filter(
        date_ordered__gt=(datetime.date.today() - timedelta(days=days_before)))
    context = {'orders': orders}
    return render(request, 'orders.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(title=title, price=price, amount=amount,
                              add_date=add_date, image=image)
            product.save()

    else:
        form = ProductForm()

    return render(request, 'hw_2_app/product.html', {'form': form})
