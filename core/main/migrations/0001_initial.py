# Generated by Django 5.0 on 2023-12-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title', models.CharField(max_length=60, verbose_name='Document Title')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo')),
                ('path1', models.CharField(max_length=40, verbose_name='Path 1')),
                ('path2', models.CharField(max_length=40, verbose_name='Path 2')),
                ('path3', models.CharField(max_length=40, verbose_name='Path 3')),
                ('path4', models.CharField(max_length=40, verbose_name='Path 4')),
                ('path5', models.CharField(max_length=40, verbose_name='Path 5')),
                ('path6', models.CharField(max_length=40, verbose_name='Path 6')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
    ]
