# Generated by Django 2.2.16 on 2021-10-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20211018_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(blank=True, default='без жанра', max_length=256, verbose_name='Название'),
        ),
    ]
