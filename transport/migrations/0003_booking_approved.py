# Generated by Django 3.0.3 on 2020-07-08 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_auto_20200707_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
