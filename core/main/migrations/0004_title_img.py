# Generated by Django 5.0 on 2023-12-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
