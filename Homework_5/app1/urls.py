from django.urls import path
from app1.views import add_product, add_client
urlpatterns = [
    path('product/', add_product, name='product'),
    path('client/', add_client, name='client')]
