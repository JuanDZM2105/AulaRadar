# Generated by Django 4.2.4 on 2023-10-30 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainRadar', '0003_remove_universidad_id_universidad_id_unico'),
    ]

    operations = [
        migrations.CreateModel(
            name='programa_academicos',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=2000)),
                ('id_unico1', models.IntegerField(primary_key=True, serialize=False)),
                ('id_universidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainRadar.universidad')),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=2000)),
                ('precio', models.FloatField()),
                ('id_unico2', models.IntegerField(primary_key=True, serialize=False)),
                ('id_programa_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainRadar.programa_academicos')),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('descripcion', models.CharField(max_length=2000)),
                ('id_unico3', models.IntegerField(primary_key=True, serialize=False)),
                ('id_curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainRadar.curso')),
                ('id_programa_academico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainRadar.programa_academicos')),
                ('id_universidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainRadar.universidad')),
            ],
        ),
    ]