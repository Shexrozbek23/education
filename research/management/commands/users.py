import pandas as pd

from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import UserInfo


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        # time = timezone.now().strftime('%X')
        # self.stdout.write("It's now %s" % time)

        col_names = ('id', 'section', 'position', 'full_name', 'date_of_birthday', 'gender', 'degree','inps_number', 'phone_number')
        users = pd.read_csv("static/users.csv", sep=",", names=col_names, header=None)
        for index, user in users.iterrows():
            if user.id == "id":
                continue

            new_user = UserInfo(
                section=user.section,
                position=user.position,
                full_name=user.full_name,
                date_of_birthday=user.date_of_birthday,
                gender=user.gender,
                degree=user.degree,
                inps_number=user.inps_number,
                phone_number=user.phone_number,
                username=f'work{str(user.phone_number)}'
            )
            if UserInfo.objects.filter(username=f'u{str(user.phone_number)}').exists() or UserInfo.objects.filter(
                    phone_number=user.phone_number).exists():
                print(f'This {user.full_name_latin} user is already exists')
                continue
            new_user.set_password(str(user.phone_number))
            new_user.save()
            # # print(f'User {user.full_name_latin} has been created successfully')
            # print(user.full_name)
