# Generated by Django 4.1.7 on 2023-03-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_envio_alter_clientes_email_alter_producto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(),
        ),
    ]