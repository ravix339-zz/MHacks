import aylien_news_api
import time
import datetime
from aylien_news_api.rest import ApiException
import sys

aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '6f988920'
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '38df9afded126bb7c295ee53e723bada'

api_instance = aylien_news_api.DefaultApi()

count = 0
week_no = 0

def fetch_new_stories(params={}):
    fetched_stories = []
    stories = None
    while stories is None or len(stories) > 0:
        try:
            response = api_instance.list_stories(**params)
        except ApiException as e:
            if e.status == 429:
                print('Usage limit are exceeded. Wating for 60 seconds...')
                time.sleep(60)
                continue
        stories = response.stories
        params['cursor'] = response.next_page_cursor
        fetched_stories += stories
        # print("Fetched %d stories. Total story count so far: %d" %
        #       (len(stories), len(fetched_stories)))
        global count, week_no
        count += len(fetched_stories)
        print("Week no: %d, %s\nTotal count so far: %d\n" % (week_no, startDate, count))
    return fetched_stories

opts = {
  'title' : 'bitcoin',
  'language': ['en'],
  'published_at_start': '2015-11-24T00:00:00Z',
  'published_at_end': '2015-12-01T00:00:00Z',
  'cursor': '*',
  'per_page': 100
}

day = datetime.timedelta(1, 0, 0, 0, 0, 0)
week = datetime.timedelta(6, 0, 0, 0, 0, 0)
startDate = datetime.date(2015, 11, 24)
endDate = startDate + week
finalDate = datetime.date(2017, 9, 24)

def resetTimer():
    global week, startDate, endDate, finalDate
    week = datetime.timedelta(6, 0, 0, 0, 0, 0)
    startDate = datetime.date(2015, 11, 24)
    endDate = startDate + week
    finalDate = datetime.date(2017, 9, 24)

def hasNext():
    return endDate < finalDate

def dtToUtc(dt):
    return str(dt.year).zfill(4) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)

def getNextWeek():
    global opts, startDate, week, endDate
    articles = []
    if endDate < finalDate:
        opts = {
            'text': 'bitcoin',
            'language': ['en'],
            'published_at_start': dtToUtc(startDate) + 'T00:00:00Z',
            'published_at_end': dtToUtc(endDate) + 'T00:00:00Z',
            'source_links_in_count_min': 8000,
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
        week_no += 1
        w = getNextWeek()
        with open("D:\\Code\\Python\\Text\\" + str(startDate) + ".txt", 'wb+') as file:
            for i in w:
                file.write((str(i[1])+"\r\n\r\n\r\n\r\n\r\n").encode('utf-8'))