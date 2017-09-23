import aylien_news_api
import time
from aylien_news_api.rest import ApiException
from pprint import pprint

def fetch_new_stories(params={}):
    fetched_stories = []
    stories = None
    while stories is None or len(stories) > 0:
        try:
            response = api_instance.list_stories(**params)
        except ApiException as e:
            if (e.status == 429):
                print('Usage limit are exceeded. Wating for 60 seconds...')
                time.sleep(60)
                continue
        stories = response.stories
        params['cursor'] = response.next_page_cursor
        fetched_stories += stories
        print("Fetched %d stories. Total story count so far: %d" %
              (len(stories), len(fetched_stories)))
    return fetched_stories

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '8a0e6374'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'a1ba885d7d7d4e160b16d9f5c1fd551a'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


params = {
  'title' : 'bitcoin',
  'language': ['en'],
  'published_at_start': 'NOW-5HOUR',
  'published_at_end': 'NOW',
  'cursor': '*',
  'per_page': 100
}
count = 1
stories = fetch_new_stories(params)
print("\n\n")

for story in stories:
        print(story.id)
        print(story.title)
        print(story.body)