import datetime
import uuid
from datetime import timezone

from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField
from django.core.validators import URLValidator
from django.db import models

dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()


def generate_id():
    return uuid.uuid4().hex

class News(models.Model):
    id = models.CharField(max_length=256, default=generate_id, primary_key=True)
    news_id = models.BigIntegerField(null=True)
    descendants = models.BigIntegerField(null=True)
    kids = models.JSONField(null=True, default=list)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=256)
    text = models.TextField(null=True)
    time = models.BigIntegerField(null=True, default=utc_timestamp)
    news_type = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    by = models.CharField(max_length=256)

    is_hacker_news = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
