# Generated by Django 5.0 on 2023-12-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_about_header_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'About Content',
                'verbose_name_plural': 'About Content',
            },
        ),
        migrations.AddField(
            model_name='about',
            name='video_url',
            field=models.URLField(default=1, verbose_name='Video Url'),
            preserve_default=False,
        ),
    ]
