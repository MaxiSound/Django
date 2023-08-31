import datetime
from datetime import timedelta
from random import randint, random
from django.core.management.base import BaseCommand
from hw_2_app.models import Product


class Command(BaseCommand):
    help = "Fill Products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            start_date = datetime.date(2022, 1, 1)
            end_date = datetime.date(2023, 8, 29)
            product = Product(title=f'Title{i}',
                              price=randint(1, 1000)+random(),
                              amount=randint(1, 100),
                              add_date=datetime.date(
                                  2022, 1, 1) + timedelta(days=randint(1, (end_date - start_date).days))
                              )
            product.save()
        self.stdout.write(f"{i} products created")
