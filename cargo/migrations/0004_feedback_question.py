# Generated by Django 4.2.1 on 2023-07-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0003_alter_calculatordata_deliveryprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('comment', models.TextField()),
                ('pic', models.ImageField(default='hello1', upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=50)),
                ('answer', models.TextField()),
            ],
        ),
    ]