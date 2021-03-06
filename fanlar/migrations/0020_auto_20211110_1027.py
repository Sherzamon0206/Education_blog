# Generated by Django 3.2.4 on 2021-11-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0019_auto_20211105_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageDerector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derector_photo', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('derector_name', models.CharField(blank=True, max_length=255, null=True)),
                ('derector_body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutPagePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutPageVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='media/video/')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='derector_body',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='derector_name',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='derector_photo',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='video_file',
        ),
    ]
