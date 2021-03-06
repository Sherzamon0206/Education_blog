# Generated by Django 3.2.7 on 2021-09-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0004_oqituvchilar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('summary', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='media/video/')),
            ],
        ),
        migrations.AlterField(
            model_name='fanlar',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='fanlar',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='media/video/'),
        ),
    ]
