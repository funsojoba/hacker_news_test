from celery import shared_task

from news_app.models import News


@shared_task(name="task.fetch_data_and_populate_db")
def fetch_data_and_populate_db():
    API_URL = "https://hacker-news.firebaseio.com/v0/"
    response = requests.get(API_URL + 'topstories.json')
    if response.status_code == 200:
        id_list = response.json()[:100]  # Get the first 100 IDs
        for id in id_list:
            # Make the second API call for each ID
            data_response = requests.get(API_URL + f'item/{id}.json?print=pretty')
            if data_response.status_code == 200:
                data = data_response.json()
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
                #TODO: log this
                print(f"Error retrieving data for ID: {id}")
