# Generated by Django 5.0 on 2023-12-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_title_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='text1',
            field=models.TextField(blank=True, verbose_name='Text 1'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text2',
            field=models.TextField(blank=True, verbose_name='Text 2'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text3',
            field=models.TextField(blank=True, verbose_name='Text 3'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text4',
            field=models.TextField(blank=True, verbose_name='Text 4'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text5',
            field=models.TextField(blank=True, verbose_name='Text 5'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text6',
            field=models.TextField(blank=True, verbose_name='Text 6'),
        ),
        migrations.AlterField(
            model_name='title',
            name='text7',
            field=models.TextField(blank=True, verbose_name='Text 7'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title1',
            field=models.CharField(max_length=50, verbose_name='Title 1'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title2',
            field=models.CharField(max_length=50, verbose_name='Title 2'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title3',
            field=models.CharField(max_length=50, verbose_name='Title 3'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title4',
            field=models.CharField(max_length=50, verbose_name='Title 4'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title5',
            field=models.CharField(max_length=50, verbose_name='Title 5'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title6',
            field=models.CharField(max_length=50, verbose_name='Title 6'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title7',
            field=models.CharField(max_length=50, verbose_name='Title 7'),
        ),
    ]