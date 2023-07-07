from .models import News



def store_hacker_news(**kwargs):
    News.objects.create(**kwargs, is_hacker_news=True)