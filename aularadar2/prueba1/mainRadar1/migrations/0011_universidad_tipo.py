# Generated by Django 4.2.7 on 2023-11-23 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRadar1', '0010_programa_academicos_precio_medio'),
    ]

    operations = [
        migrations.AddField(
            model_name='universidad',
            name='tipo',
            field=models.CharField(choices=[('publico', 'Público'), ('privado', 'Privado')], default='publico', max_length=10),
        ),
    ]
