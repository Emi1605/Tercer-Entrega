# Generated by Django 4.1.7 on 2023-04-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0006_producto_id_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='condicion',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
