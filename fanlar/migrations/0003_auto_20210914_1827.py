# Generated by Django 3.2.7 on 2021-09-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0002_auto_20210914_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanlar',
            name='bolim5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='fanlar',
            name='text5',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]