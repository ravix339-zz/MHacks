import requests
import timeit
import random
import glob
from datetime import datetime, date, timedelta
import time
import SQL_Interface
from bs4 import BeautifulSoup

#URL= 'https://www.google.com/search?q=bitcoin&tbs=cdr:1,cd_min:1/26/2017,cd_max:2/25/2017&tbm=nws&ei=UfXFWZC8EYLGjwTWyofoBA&start=00&sa=N&biw=1829&bih=899&dpr=1.75'
URL= 'https://www.google.com/search?q=bitcoin&tbs=cdr:1,cd_min:{startdate},cd_max:{stopdate}&tbm=nws&ei=UfXFWZC8EYLGjwTWyofoBA&start={searchresultnumber}&sa=N&biw=1829&bih=899&dpr=1.75'
#2010-07-18
def prog():
    start_date = date(2012, 7, 1)
    while start_date < date(2012, 12, 30):#datetime.now().date():
        print(start_date, min(start_date + timedelta(days=6), datetime.now().date()))

        with open("C:\\Users\\Ravi\\Desktop\\URLs2\\" + str(start_date) + ".txt", 'w+') as file:
            for page_number in range(3):
                response = requests.get(URL.format(startdate=start_date.strftime("%m/%d/20%y"), stopdate=min(start_date + timedelta(days=6), datetime.now().date()).strftime("%m/%d/20%y"), searchresultnumber=str(page_number*10)))
                time.sleep(30+random.random() * random.random()*100)
                soup = BeautifulSoup(response.content, "html.parser")
                col = soup.find("div", {"id": "center_col"}).findAll('a', href=True)
                for link in set([url["href"].split("&sa")[0][7:] for url in col]):
                    file.write(link+'\n')
        start_date = start_date + timedelta(days=7)
        # print(start_date,"-", min(start_date + timedelta(days=7), datetime.now().date()), ": ",len(something))
def parseFiles():
    files = glob.glob("C:\\Users\\Ravi\\Desktop\\URLs\\*.txt")
    for fileName in files:
        with open(fileName,'r') as fileRead:

            link = fileRead.readline()
            while link != '':
                link = link[:-1]
                pre = ""
                if link[:7] == "http://":
                    pre = "http://"
                    link = link[7:]
                elif link[:8] == "https://":
                    pre = "https://"
                    link = link[8:]
                if link[:4] != "www.":
                    link = "www." + link
                link = pre + link
                print("".join(fileName.split('\\')[-1].split('.')[0].split('-')), link)
                SQL_Interface.Execute("INSERT INTO WeeklyUrls (StartDate, URL) VALUES({startDate}, '{URL}')".format(startDate="".join(fileName.split('\\')[-1].split('.')[0].split('-')), URL=link))
                link = fileRead.readline()

#prog()
parseFiles()