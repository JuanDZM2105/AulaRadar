# Generated by Django 4.2.7 on 2023-11-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRadar1', '0013_alter_universidad_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universidad',
            name='descripcion',
            field=models.CharField(max_length=2000),
        ),
    ]
