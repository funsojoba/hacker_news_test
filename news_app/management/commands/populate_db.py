from django.core.management.base import BaseCommand
import requests

from news_app.models import News

API_URL = "https://hacker-news.firebaseio.com/v0/"

class Command(BaseCommand):
    help = 'Populates the database with data from API calls'

    def handle(self, *args, **options):
        # Make the first API call to get the list of IDs
        response = requests.get(API_URL + 'topstories.json')
        if response.status_code == 200:
            id_list = response.json()[:50]  # Get the first 50 IDs
            for id in id_list:
                # Make the second API call for each ID
                data_response = requests.get(API_URL + f'item/{id}.json?print=pretty')
                if data_response.status_code == 200:
                    data = data_response.json()
                    self.stdout.write(f"Writing : {id} to database")
                    news = News(
                        title=data.get('title'),
                        text=data.get('text'),
                        kids=data.get('kids'),
                        time=data.get('time'),
                        news_id=data.get('id'),
                        by=data.get('by'),
                        score=data.get('score'),
                        news_type=data.get('type'),
                        descendants=data.get('descendants'),
                        is_hacker_news=True,
                        url=data.get('url')
                    )
                    news.save()
                else:
                    self.stdout.write(f"Error retrieving data for ID: {id}")
        else:
            self.stdout.write("Error retrieving ID list from the first API call")
