# Generated by Django 3.0.3 on 2020-07-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_booking_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='approved',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('A', 'Accepted'), ('R', 'Rejected'), ('P', 'Pending')], default='P', max_length=1),
        ),
    ]
