# Generated by Django 3.0.3 on 2020-07-07 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.IntegerField(default=0)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('vehicle_number', models.CharField(default='0000000', max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], max_length=10)),
                ('current_location', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_available', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('passengers', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.Driver')),
            ],
        ),
    ]
