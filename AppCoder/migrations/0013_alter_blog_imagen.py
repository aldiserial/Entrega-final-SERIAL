# Generated by Django 4.1.7 on 2023-04-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='AppCoder'),
        ),
    ]
