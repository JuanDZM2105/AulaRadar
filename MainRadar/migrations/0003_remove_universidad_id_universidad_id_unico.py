# Generated by Django 4.2.4 on 2023-10-27 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainRadar', '0002_rename_universidades_universidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universidad',
            name='id',
        ),
        migrations.AddField(
            model_name='universidad',
            name='id_unico',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
