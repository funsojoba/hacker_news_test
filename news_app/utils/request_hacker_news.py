import requests


class HackerNewsManager:
    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    @classmethod
    def list_news_id(cls):

        url = BASE_URL + "/topstories.json"

        payload = "{}"
        response = requests.request("GET", url, data=payload)

        return response

    @classmethod
    def list_news(cls):
        news_id = cls.list_news_id()

        results = []
        for news_id in news_ids:
            url = BASE_URL + f"/item/{news_id}.json?print=pretty"
            payload = {}
            response = requests.request("GET", url, data=payload)

            News.objects.create(
                
            )
            results.append(response.json())