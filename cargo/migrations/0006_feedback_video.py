# Generated by Django 4.2.1 on 2023-09-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0005_chinapicture_moscowpicture_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]