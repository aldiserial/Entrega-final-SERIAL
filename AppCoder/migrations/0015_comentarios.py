# Generated by Django 4.1.7 on 2023-04-06 06:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0014_alter_blog_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.blog')),
            ],
        ),
    ]
