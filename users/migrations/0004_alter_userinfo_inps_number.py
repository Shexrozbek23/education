# Generated by Django 3.2.8 on 2022-06-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userinfo_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='inps_number',
            field=models.CharField(default=0, max_length=60, null=True),
        ),
    ]
