# Generated by Django 5.1.4 on 2025-01-06 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0001_initial'),
        ('entrega_epi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaEPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_geracao', models.DateField(auto_now_add=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fichas_epi', to='colaboradores.colaborador')),
            ],
        ),
    ]
