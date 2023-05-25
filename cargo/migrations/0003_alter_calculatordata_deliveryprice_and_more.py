# Generated by Django 4.2.1 on 2023-05-21 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_alter_calculatordata_deliveryprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculatordata',
            name='deliveryPrice',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='calculatordata',
            name='mass',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
    ]
