# Generated by Django 4.1.1 on 2022-12-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linea_pedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='linea_pedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
