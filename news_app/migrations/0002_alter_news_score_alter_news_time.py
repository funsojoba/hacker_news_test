# Generated by Django 4.2.2 on 2023-07-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.BigIntegerField(default=1688741824.385154, null=True),
        ),
    ]