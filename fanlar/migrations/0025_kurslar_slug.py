# Generated by Django 4.0.1 on 2022-01-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanlar', '0024_kurslar_section_delete_fanlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurslar',
            name='slug',
            field=models.SlugField(blank=True, max_length=125, null=True, unique=True),
        ),
    ]
