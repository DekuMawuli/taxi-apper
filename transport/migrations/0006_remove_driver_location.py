# Generated by Django 3.0.3 on 2020-07-08 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0005_auto_20200708_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='location',
        ),
    ]
