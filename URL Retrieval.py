import requests
import timeit
import random
from datetime import datetime, date, timedelta
import time
from bs4 import BeautifulSoup

#URL= 'https://www.google.com/search?q=bitcoin&tbs=cdr:1,cd_min:1/26/2017,cd_max:2/25/2017&tbm=nws&ei=UfXFWZC8EYLGjwTWyofoBA&start=00&sa=N&biw=1829&bih=899&dpr=1.75'
URL= 'https://www.google.com/search?q=bitcoin&tbs=cdr:1,cd_min:{startdate},cd_max:{stopdate}&tbm=nws&ei=UfXFWZC8EYLGjwTWyofoBA&start={searchresultnumber}&sa=N&biw=1829&bih=899&dpr=1.75'
#2010-07-18
def prog():
    start_date = date(2017, 7, 18)
    while start_date < datetime.now().date():
        print(start_date, min(start_date + timedelta(days=7), datetime.now().date()))
        for page_number in range(3):
            response = requests.get(URL.format(startdate=start_date.strftime("%m/%d/20%y"), stopdate=min(start_date + timedelta(days=7), datetime.now().date()).strftime("%m/%d/20%y"), searchresultnumber=str(page_number*10)))
            #print(URL.format(startdate=start_date.strftime("%m/%d/20%y"), stopdate=min(start_date + timedelta(days=7), datetime.now().date()).strftime("%m/%d/20%y"), searchresultnumber=str(page_number*10)))
            #print(response.content)
            #print(page_number)
            #print(URL.format(startdate=start_date.strftime("%m/%d/20%y"), stopdate=min(start_date + timedelta(days=7), datetime.now().date()).strftime("%m/%d/20%y"), searchresultnumber=str(page_number*10)))
            time.sleep(30+random.random() * random.random()*100)
            soup = BeautifulSoup(response.content, "html.parser")
            col = soup.find("div", {"id": "center_col"}).findAll('a', href=True)
            for link in set([url["href"].split("&sa")[0][7:] for url in col]):
                print(link)
        start_date = start_date + timedelta(days=8)
        # print(start_date,"-", min(start_date + timedelta(days=7), datetime.now().date()), ": ",len(something))
print(timeit.timeit(prog()))