# Generated by Django 4.2.2 on 2023-07-07 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import news_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.CharField(default=news_app.models.generate_id, max_length=256, primary_key=True, serialize=False)),
                ('news_id', models.BigIntegerField(null=True)),
                ('descendants', models.BigIntegerField(null=True)),
                ('kids', models.JSONField(default=list, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField(null=True)),
                ('time', models.BigIntegerField(default=1688741615.293118, null=True)),
                ('news_type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=256)),
                ('is_hacker_news', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
