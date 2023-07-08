from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CORE.settings')

app = Celery('CORE')


app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-update-database-every-5-minutes": {
        "task": "task.fetch_data_and_populate_db",
        "schedule": crontab(minute="*/5"),
    }
}