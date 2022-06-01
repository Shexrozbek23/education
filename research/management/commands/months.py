from decimal import Decimal

from django.core.management import BaseCommand
from django.utils import timezone
import pandas as pd

from research.models import Months


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        col_names = ('pk', 'name')
        months = pd.read_csv("static/months.csv", sep=",", names=col_names, header=None)
        for index, months in months.iterrows():
            Months.objects.get_or_create(
                pk=months.pk,
                month=months.name,
            )
