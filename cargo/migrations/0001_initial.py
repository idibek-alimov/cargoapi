# Generated by Django 4.2.1 on 2023-05-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('number', models.CharField(blank=True, max_length=50)),
                ('productType', models.CharField(blank=True, max_length=50)),
                ('productName', models.CharField(blank=True, max_length=50)),
                ('quantity', models.IntegerField()),
                ('mass', models.IntegerField()),
                ('deliveryMethod', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('insurance', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True)),
                ('deliveryPrice', models.IntegerField(default=0)),
                ('deliveryTime', models.IntegerField(default=0)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('number', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField()),
                ('deliveryMethod', models.CharField(blank=True, default='Авто', max_length=50)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
