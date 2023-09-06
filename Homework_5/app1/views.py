from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from app1.forms import ProductForm, ClientForm
from app1.models import Product, Client


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email,
                            phone=phone, address=address)
            client.save()
    else:
        form = ClientForm()
    return render(request, 'app1/client.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(title=title, price=price,
                              amount=amount, description=description, image=image)
            product.save()
    else:
        form = ProductForm()
    return render(request, 'app1/product.html', {'form': form})
