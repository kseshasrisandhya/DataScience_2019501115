from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
from scipy.stats import pearsonr

import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px
import pdfcrowd
import pdfkit


def extract_data(url_gics_sectors):
    html_content = requests.get(url_gics_sectors).text
    soup = BeautifulSoup(html_content, "lxml")
    find_table = soup.find('table', class_='wikitable sortable')
    j = 0
    full_val = []
    for link in find_table.find_all('tr'):
        j += 1
        if(j == 1):
            continue
        i = 0
        d = {}
        for ele in link.find_all('td'):
            i += 1
            if(i == 1):
                st = ele.text
                st = st[:-1]
                d['symbol'] = st
            # elif(i == 2):
            #     d['security'] = ele.text
            # elif(i == 3):
            #     d['sec_filings'] = ele.text
            elif(i == 4):
                d['gics_sector'] = ele.text
            # elif(i == 5):
            #     d['gics_sub_industry'] = ele.text
            # elif(i == 6):
            #     d['hq'] = ele.text
            # elif(i == 7):
            #     d['date'] = ele.text
            # elif(i == 8):
            #     d['cik'] = ele.text
            # elif(i == 9):
            #     d['founded'] = ele.text

        full_val.append(d)
    df = pd.DataFrame(full_val)
    # print(df)
    df.to_csv('file4.csv')
    return full_val


def top_bottom_corr():
    df_daily = pd.read_csv("daily_answer.csv")
    daily_group = df_daily.groupby(
        'Symbol')['Loss or Gain'].sum().reset_index()

    daily_top = daily_group.sort_values(by='Loss or Gain', ascending=False)
    daily_bottom = daily_group.sort_values(by='Loss or Gain')
    daily_top_val = daily_top['Loss or Gain'].tolist()[:25]
    daily_top_comp = daily_top['Symbol'].tolist()[:25]
    daily_bottom_val = daily_bottom['Loss or Gain'].tolist()[:25]
    daily_bottom_comp = daily_bottom['Symbol'].tolist()[:25]
    df_weekly = pd.read_csv("weekly_answer.csv")
    weekly_group = df_weekly.groupby(
        'Symbol')['Gain or Loss'].sum().reset_index()

    weekly_top = weekly_group.sort_values(by='Gain or Loss', ascending=False)
    weekly_bottom = weekly_group.sort_values(by='Gain or Loss')
    weekly_top_val = weekly_top['Gain or Loss'].tolist()[:25]
    weekly_top_comp = weekly_top['Symbol'].tolist()[:25]
    weekly_bottom_val = weekly_bottom['Gain or Loss'].tolist()[:25]
    weekly_bottom_comp = weekly_bottom['Symbol'].tolist()[:25]

    df_monthly = pd.read_csv("monthly_answer.csv")
    monthly_group = df_monthly.groupby(
        'Symbol')['Loss or Gain'].sum().reset_index()

    monthly_top = monthly_group.sort_values(by='Loss or Gain', ascending=False)
    monthly_bottom = monthly_group.sort_values(by='Loss or Gain')
    monthly_top_val = monthly_top['Loss or Gain'].tolist()[:25]
    monthly_top_comp = monthly_top['Symbol'].tolist()[:25]
    monthly_bottom_val = monthly_bottom['Loss or Gain'].tolist()[:25]
    monthly_bottom_comp = monthly_bottom['Symbol'].tolist()[:25]

    daily_top_dict = {}
    for i in daily_top_comp:
        temp_df = df_daily[df_daily['Symbol'] == i]
        daily_top_dict[i] = temp_df['Loss or Gain'].tolist()

    keys = list(daily_top_dict.keys())
    df_daily_top = pd.DataFrame(daily_top_dict, columns=keys)

    corrMatrix = df_daily_top.corr()
    fig1 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig1.show()
    fig1.write_html("top_25_daily.html")

    daily_bottom_dict = {}
    for i in daily_bottom_comp:
        temp_df = df_daily[df_daily['Symbol'] == i]
        daily_bottom_dict[i] = temp_df['Loss or Gain'].tolist()[:200]

    keys = list(daily_bottom_dict.keys())
    df_daily_bottom = pd.DataFrame(daily_bottom_dict, columns=keys)

    corrMatrix = df_daily_bottom.corr()
    fig2 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig2.show()
    fig2.write_html("bottom_25_daily.html")

    weekly_top_dict = {}
    for i in weekly_top_comp:
        temp_df = df_weekly[df_weekly['Symbol'] == i]
        weekly_top_dict[i] = temp_df['Gain or Loss'].tolist()[:43]

    keys = list(weekly_top_dict.keys())
    df_weekly_top = pd.DataFrame(weekly_top_dict, columns=keys)

    corrMatrix = df_weekly_top.corr()
    fig3 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig3.show()
    fig3.write_html("top_25_weekly.html")

    weekly_bottom_dict = {}
    for i in weekly_bottom_comp:
        temp_df = df_weekly[df_weekly['Symbol'] == i]
        weekly_bottom_dict[i] = temp_df['Gain or Loss'].tolist()[:86]

    keys = list(weekly_bottom_dict.keys())
    df_weekly_bottom = pd.DataFrame(weekly_bottom_dict, columns=keys)

    corrMatrix = df_weekly_bottom.corr()
    fig4 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig4.show()
    fig4.write_html("bottom_25_weekly.html")

    monthly_top_dict = {}
    for i in monthly_top_comp:
        temp_df = df_monthly[df_monthly['Symbol'] == i]
        monthly_top_dict[i] = temp_df['Loss or Gain'].tolist()

    keys = list(monthly_top_dict.keys())
    df_monthly_top = pd.DataFrame(monthly_top_dict, columns=keys)

    corrMatrix = df_monthly_top.corr()
    fig5 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig5.show()
    fig5.write_html("top_25_monthly.html")

    monthly_bottom_dict = {}
    for i in monthly_bottom_comp:
        temp_df = df_monthly[df_monthly['Symbol'] == i]
        monthly_bottom_dict[i] = temp_df['Loss or Gain'].tolist()

    keys = list(monthly_bottom_dict.keys())
    df_monthly_bottom = pd.DataFrame(monthly_bottom_dict, columns=keys)

    corrMatrix = df_monthly_bottom.corr()
    fig6 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "blue"])
    fig6.show()
    fig6.write_html("bottom_25_monthly.html")
    return daily_top_comp, daily_bottom_comp, weekly_top_comp, weekly_bottom_comp, monthly_top_comp, monthly_bottom_comp


def bar_graph_create(daily_top_comp, daily_bottom_comp, weekly_top_comp, weekly_bottom_comp, monthly_top_comp, monthly_bottom_comp):
    df_companies = pd.read_csv("file4.csv")
    gics = df_companies['gics_sector'].tolist()
    comp = df_companies['symbol'].tolist()

    dict_com = {}
    for i in range(len(gics)):
        dict_com[comp[i]] = gics[i]

    dict_count_top_daily = {}
    for j in daily_top_comp:
        if(dict_com[j] in dict_count_top_daily):
            dict_count_top_daily[dict_com[j]] += 1
        else:
            dict_count_top_daily[dict_com[j]] = 1

    dict_count_bottom_daily = {}
    for j in daily_bottom_comp:
        if(dict_com[j] in dict_count_bottom_daily):
            dict_count_bottom_daily[dict_com[j]] += 1
        else:
            dict_count_bottom_daily[dict_com[j]] = 1

    dict_count_top_weekly = {}
    for j in weekly_top_comp:
        if(dict_com[j] in dict_count_top_weekly):
            dict_count_top_weekly[dict_com[j]] += 1
        else:
            dict_count_top_weekly[dict_com[j]] = 1

    dict_count_bottom_weekly = {}
    for j in weekly_bottom_comp:
        if(dict_com[j] in dict_count_bottom_weekly):
            dict_count_bottom_weekly[dict_com[j]] += 1
        else:
            dict_count_bottom_weekly[dict_com[j]] = 1

    dict_count_top_monthly = {}
    for j in monthly_top_comp:
        if(dict_com[j] in dict_count_top_monthly):
            dict_count_top_monthly[dict_com[j]] += 1
        else:
            dict_count_top_monthly[dict_com[j]] = 1

    dict_count_bottom_monthly = {}
    for j in monthly_bottom_comp:
        if(dict_com[j] in dict_count_bottom_monthly):
            dict_count_bottom_monthly[dict_com[j]] += 1
        else:
            dict_count_bottom_monthly[dict_com[j]] = 1

    daily_top = list(dict_count_top_daily.keys())
    daily_bottom = list(dict_count_bottom_daily.keys())

    fig1 = go.Figure(data=[
        go.Bar(name='top 25', x=daily_top, y=list(
            dict_count_top_daily.values())),
        go.Bar(name='bottom 25', x=daily_bottom,
               y=list(dict_count_bottom_daily.values()))
    ])
    # Change the bar mode
    fig1.update_layout(barmode='group')
    fig1.show()
    fig1.write_html("daily top 25 and bottom 25 companies.html")

    weekly_top = list(dict_count_top_weekly.keys())
    weekly_bottom = list(dict_count_bottom_weekly.keys())

    fig2 = go.Figure(data=[
        go.Bar(name='top 25', x=weekly_top, y=list(
            dict_count_top_weekly.values())),
        go.Bar(name='bottom 25', x=weekly_bottom,
               y=list(dict_count_bottom_weekly.values()))
    ])
    # Change the bar mode
    fig2.update_layout(barmode='group')
    fig2.show()
    fig2.write_html("weekly top 25 and bottom 25 companies.html")

    monthly_top = list(dict_count_top_monthly.keys())
    monthly_bottom = list(dict_count_bottom_monthly.keys())

    fig3 = go.Figure(data=[
        go.Bar(name='top 25', x=monthly_top, y=list(
            dict_count_top_monthly.values())),
        go.Bar(name='bottom 25', x=monthly_bottom,
               y=list(dict_count_bottom_monthly.values()))
    ])
    # Change the bar mode
    fig3.update_layout(barmode='group')
    fig3.show()
    fig3.write_html("monthly top 25 and bottom 25 companies.html")


daily_top_comp, daily_bottom_comp, weekly_top_comp, weekly_bottom_comp, monthly_top_comp, monthly_bottom_comp = top_bottom_corr()
# bar_graph_create(daily_top_comp, daily_bottom_comp, weekly_top_comp,
#                  weekly_bottom_comp, monthly_top_comp, monthly_bottom_comp)


def build_data_bar_graph(full_val):

    dp_top = {}
    dp_bottom = {}
    top = [full_val[i] for i in range(len(full_val)//2)]
    bottom = [full_val[i] for i in range(len(full_val)//2, len(full_val))]
    for q in top:
        string = q['gics_sector']
        if(string in dp_top):
            dp_top[string] += 1
        else:
            dp_top[string] = 1

    for q in bottom:
        string = q['gics_sector']

        if(string in dp_bottom):
            dp_bottom[string] += 1
        else:
            dp_bottom[string] = 1

    return dp_top, dp_bottom


def bar_graph(dp_top, dp_bottom):
    dp_top = dict(
        sorted(dp_top.items(), key=lambda item: item[1], reverse=True)[:10])
    dp_bottom = dict(
        sorted(dp_bottom.items(), key=lambda item: item[1], reverse=True)[:10])

    dp_new = []
    top_new = []
    bottom_new = []
    for i in dp_top:
        if(i in dp_bottom):
            top_new.append(dp_top[i])
            bottom_new.append(dp_bottom[i])
            dp_new.append(i)

    data = []
    data.append(top_new)
    data.append(bottom_new)

    barWidth = 0.25
    fig = plt.subplots(figsize=(25, 9))
    br1 = np.arange(len(top_new))
    br2 = [x + barWidth for x in br1]

    plt.bar(br1, top_new, color='g', width=barWidth,
            edgecolor='grey', label='Top 25 companies')
    plt.bar(br2, bottom_new, color='r', width=barWidth,
            edgecolor='grey', label='Bottom 25 companies')
    plt.legend(labels=['Top 25', 'Bottom 25'])
    plt.xlabel('Sectors', fontweight='bold')
    plt.ylabel('Frequency', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(top_new))],
               dp_new)
    plt.show()


def question_4(url_gics_sectors):
    full_val = extract_data(url_gics_sectors)
    dp_top, dp_bottom = build_data_bar_graph(full_val)
    bar_graph(dp_top, dp_bottom)


# url_gics_sectors = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
# question_4(url_gics_sectors)
