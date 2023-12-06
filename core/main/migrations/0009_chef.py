# Generated by Django 5.0 on 2023-12-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_offer_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('social1', models.URLField(verbose_name='Social 1')),
                ('social2', models.URLField(verbose_name='Social 2')),
                ('social3', models.URLField(verbose_name='Social 3')),
            ],
        ),
    ]