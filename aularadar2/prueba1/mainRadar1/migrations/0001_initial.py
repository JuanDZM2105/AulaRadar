# Generated by Django 4.2.4 on 2023-11-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='universidad',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('id_unico', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
