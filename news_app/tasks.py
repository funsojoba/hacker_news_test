from celery import shared_task

from news_app.models import News

@shared_task
def fetch_data_and_populate_db():
    pass
