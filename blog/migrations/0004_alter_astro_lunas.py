# Generated by Django 3.2.25 on 2025-06-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_astro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astro',
            name='lunas',
            field=models.FloatField(),
        ),
    ]
