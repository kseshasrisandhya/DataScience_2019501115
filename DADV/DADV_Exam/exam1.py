import requests
import pandas as pd
from bs4 import BeautifulSoup
import io
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url_sp = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url_sp)
soup = BeautifulSoup(response.text, "html.parser")

find_header = soup.find_all('th')
list_of_headers = []
for x in find_header:
    list_of_headers.append(x.get_text(strip=True))
list_of_headers = list_of_headers[0:9]

d = soup.find('table')

table_row_data = []

for row in d.find_all('tr'):
    s = []
    for td in row.find_all('td'):
        s.append(td.get_text(strip=True))
    table_row_data.append(s)

table_row_data.pop(0)

df = pd.DataFrame(table_row_data, columns=list_of_headers)

symbol = df['Symbol']
period1 = "1483228800"
period2 = "1609545600"


def extract_value(value_list):
    sample_genre = []
    for i in list_of_top_songs:
        print(i['song'])
        sp = copy.deepcopy(i)
        sp['genre_list'] = ''
        url = "https://en.wikipedia.org/" + i['song_url']
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        find_table = soup.find('table', class_="infobox vevent")
        if(find_table != None):
            gen = ''
            for link in find_table.find_all('tr'):
                for ele in link.find_all('td'):
                    sample = str(ele)
                    if("category hlist" in sample):
                        gen = ele.text
            # print("----------------")
            genre_list = get_genre_list(gen)
            # print(genre_list)
            # print(type(genre_list))
            sp['genre_list'] = genre_list
            sample_genre.append(sp)
    return sample_genre


def monthly_daily():
    month_close = []
    daily_close = []
    df_monthly = pd.read_csv("monthly.csv")
    df_daily = pd.read_csv("daily.csv")
    close_monthly = df_monthly['Close'].tolist()
    month_close.append(
        ((close_monthly[0]+close_monthly[1]+close_monthly[2])/3)*100)
    for i in range(1, len(close_monthly)):
        month_close.append(
            ((close_monthly[i] - close_monthly[i-1])/close_monthly[i-1])*100)

    close_daily = df_daily['Close'].tolist()
    daily_close.append(
        ((close_daily[0]+close_daily[1]+close_daily[2])/3)*100)
    for i in range(1, len(close_daily)):
        daily_close.append(
            ((close_daily[i] - close_daily[i-1])/close_daily[i-1])*100)

    df_monthly['Loss or Gain'] = month_close
    df_daily['Loss or Gain'] = daily_close

    df_monthly.to_csv('monthly_answer.csv')
    df_daily.to_csv('daily_answer.csv')


def scrape(l):
    #mo - month
    #wk - week
    #d - day
    link = "https://query1.finance.yahoo.com/v7/finance/download/"+l+"?period1=" + \
        period1+"&period2="+period2+"&interval=1wk&events=history&includeAdjustedClose=true"
    response = requests.get(link)
    bytes_format = io.BytesIO(response.content)
    df = pd.read_csv(bytes_format)
    df['Symbol'] = l
    return df


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    pool_object = Pool(30)
    df_list = pool_object.map(scrape, symbol)
    pool_object.close()
    for ele in df_list:
        if len(ele.columns) > 3:
            close = ele['Close'].tolist()
            percentage_cal = []
            for i in range(1, len(close)):
                percentage_cal.append(((close[i]-close[i-1])/close[i-1])*100)
            percentage_cal.insert(
                0, ((percentage_cal[0]+percentage_cal[1]+percentage_cal[2])/3)*100)
            ele['Gain or Loss'] = percentage_cal
    table = pd.concat(df_list).reset_index(drop=True)
    table.to_csv('Weekly_answer.csv')
