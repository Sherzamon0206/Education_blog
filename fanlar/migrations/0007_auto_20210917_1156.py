# Generated by Django 3.2.7 on 2021-09-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0006_alter_fanlar_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanlar',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='oqituvchilar',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='yangiliklar',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
