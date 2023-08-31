import datetime
from datetime import timedelta
from random import choices, randint

from django.core.management.base import BaseCommand
from django.utils import timezone
from hw_2_app.models import Client


class Command(BaseCommand):
    help = "Fill Clients."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            start_date = datetime.date(2022, 1, 1)
            end_date = datetime.date(2022, 12, 31)
            client = Client(name=f'Name{i}',
                            email=f'mail{i}@mail.ru',
                            phone=int(f'7{randint (1111111111,9999999999)}'),
                            address=f"Город Энск, ул. Строителей, "
                            f"дом. {randint (1,32)}, "
                            f"корпус {randint (1,3)},"
                            f"квартира {randint (1,100)}",
                            reg_date=datetime.date(
                                2022, 1, 1) + timedelta(days=randint(1, (end_date - start_date).days))
                            )
            client.save()
        self.stdout.write(f"{i} clents created")
