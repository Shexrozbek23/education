from decimal import Decimal

from django.core.management import BaseCommand
from django.utils import timezone
import pandas as pd

from users.models import User


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        col_names = ('section', 'position', 'full_name', 
                    'date_of_birthday', 'gender','degree', 'inps_number', 
                    'phone',)
        info = pd.read_csv("static/Book.csv", sep=";", names=col_names, header=None)
        for index, info in info.iterrows():
            User.objects.create(
                position=info.position,
                full_name=info.full_name,
                date_of_birthday=info.date_of_birthday,
                gender=info.gender,
                degree=info.gender,
                inps_number=info.inps_number,
                phone=info.phone,
            )
