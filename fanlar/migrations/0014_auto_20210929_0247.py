# Generated by Django 3.2.7 on 2021-09-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0013_alter_fanlar_text1_decription'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanlar',
            name='text2_decription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fanlar',
            name='text3_decription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fanlar',
            name='text4_decription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fanlar',
            name='text5_decription',
            field=models.TextField(blank=True),
        ),
    ]
