# Generated by Django 3.2.7 on 2021-09-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0005_auto_20210915_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanlar',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
