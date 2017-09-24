import json
import datetime


def dtToUtc(dt):
    return str(dt.year).zfill(4) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)


def get_next_week(day):
    return day + datetime.timedelta(weeks=1)

price_in_file = 'data/bitcoin_price_data.json'
delta_price_file = 'data/bitcoin_weekly_data.json'

with open(price_in_file) as json_data:
    json_data = json.load(json_data)

weekly_data = {}
i = 0
start_date = datetime.date(2010, 7, 18)
next_date = get_next_week(start_date)
while next_date < datetime.date.today():
    start_price = json_data['bpi'][str(start_date)]
    end_price = json_data['bpi'][str(next_date)]
    weekly_data[dtToUtc(next_date)] = {'Delta Price': end_price - start_price}
    weekly_data[dtToUtc(next_date)].update({'Final Price': end_price})
    i = i + 1
    start_date = next_date
    next_date = get_next_week(start_date)

print('Ended on ' + str(next_date))
with open(delta_price_file, 'w') as out_file:
    json.dump(weekly_data, out_file)
