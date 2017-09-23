import aylien_news_api
import time
import datetime
from aylien_news_api.rest import ApiException

def fetch_new_stories(params={}):
    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '8a0e6374'
    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'a1ba885d7d7d4e160b16d9f5c1fd551a'
    api_instance = aylien_news_api.DefaultApi()

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
        # print("Fetched %d stories. Total story count so far: %d" %
        #       (len(stories), len(fetched_stories)))
    return fetched_stories


# MY CODE BEGINS HERE

opts = {
  'title' : 'bitcoin',
  'language': ['en'],
  'published_at_start': '2015-11-22T00:00:00Z',
  'published_at_end': '2015-11-29T00:00:00Z',
  'cursor': '*',
  'per_page': 100
}

startDate = datetime.date(2015, 11, 22)
week = datetime.timedelta(7, 0, 0, 0, 0, 0)
endDate = startDate + week
finalDate = datetime.date(2017, 9, 24)

day = datetime.timedelta(1, 0, 0, 0, 0, 0)

def resetTimer():
    global startDate
    global week
    global endDate
    global finalDate
    startDate = datetime.date(2015, 11, 22)
    week = datetime.timedelta(7, 0, 0, 0, 0, 0)
    endDate = startDate + week
    finalDate = datetime.date(2016, 1, 1)

def hasNext():
    return endDate < finalDate

def dtToUtc(dt):
    return str(dt.year).zfill(4) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)

def getNextWeek():
    global opts
    global startDate
    global week
    global endDate
    articles = []
    if endDate <= finalDate:
        # del opts['published_at_start']
        # del opts['published_at_end']
        # opts['published_at_start'] = dtToUtc(startDate) + 'T00:00:00Z'
        # opts['published_at_end'] = dtToUtc(endDate) + 'T00:00:00Z'
        opts = {
            'title': 'bitcoin',
            'language': ['en'],
            'published_at_start': dtToUtc(startDate) + 'T00:00:00Z',
            'published_at_end': dtToUtc(endDate) + 'T00:00:00Z',
            'cursor': '*',
            'per_page': 100
        }
        stories = fetch_new_stories(opts)
        for story in stories:
            articles.append((dtToUtc(startDate), story.title + "\n\n" + story.body))
    startDate = endDate + day
    endDate = startDate + week
    return articles


resetTimer()
while hasNext():
    w = getNextWeek()
    for i in w:
        print(i)
    print("\n\n")