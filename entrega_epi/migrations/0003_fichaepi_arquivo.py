# Generated by Django 5.1.4 on 2025-01-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega_epi', '0002_fichaepi'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichaepi',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='fichas_epis/'),
        ),
    ]
