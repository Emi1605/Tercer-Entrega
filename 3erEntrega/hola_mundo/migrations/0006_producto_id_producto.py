# Generated by Django 4.1.7 on 2023-04-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola_mundo', '0005_alter_producto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_Producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
