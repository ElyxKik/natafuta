# Generated by Django 5.0.3 on 2024-03-24 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0003_avis_nombre_recherche'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='nombre_recherche',
        ),
    ]