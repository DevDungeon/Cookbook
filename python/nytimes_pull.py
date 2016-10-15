# My API key '08055747ba414b80b6b5f454cf41064e'
import requests
import json
import time

MY_API_KEY = 'xxxx11234789012347891023478xxxxx'

def get_articles(api_key, category):
    for i in range(0, 5):
        url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
        url += '?/api-key=%s&fq=news_desk:("%s")&page=%s' % (api_key, category, i)
        print(url)
        response = requests.get(url)
        print(response.headers)
        time.sleep(1)
        print(response.text)
        data = json.loads(response.text)
        print(data)
        for meta in data['response']['meta']:
            print(meta)

        for result in data['response']['docs']:
            print(result)

get_articles(MY_API_KEY, "Sports")
get_articles(MY_API_KEY, "Arts")

