# Generated by Django 4.2.7 on 2023-11-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRadar1', '0011_universidad_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidad',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mainRadar1/imagenes/'),
        ),
    ]
