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


def analyse_daily():
    df_daily = pd.read_csv("daily_answer.csv")
    daily_group = df_daily.groupby(
        'Symbol')['Loss or Gain'].sum().reset_index()

    daily_top = daily_group.sort_values(by='Loss or Gain', ascending=False)
    daily_bottom = daily_group.sort_values(by='Loss or Gain')
    daily_top_val = daily_top['Loss or Gain'].tolist()[:25]
    daily_top_comp = daily_top['Symbol'].tolist()[:25]
    daily_bottom_val = daily_bottom['Loss or Gain'].tolist()[:25]
    daily_bottom_comp = daily_bottom['Symbol'].tolist()[:25]

    daily_dict = {}
    for i in daily_top_comp:
        temp_df = df_daily[df_daily['Symbol'] == i]
        daily_dict[i] = temp_df['Loss or Gain'].tolist()[:200]
    for i in daily_bottom_comp:
        temp_df = df_daily[df_daily['Symbol'] == i]
        daily_dict[i] = temp_df['Loss or Gain'].tolist()[:200]

    keys = list(daily_dict.keys())
    df_daily = pd.DataFrame(daily_dict, columns=keys)

    print("The top companies(daily) are " +
          daily_top_comp[0]+" and "+daily_top_comp[1])
    daily_top_company1 = daily_top_comp[0]
    daily_top_company2 = daily_top_comp[1]

    res = df_daily.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[daily_top_company1][:2].index.tolist()
    neg_corr_top1 = neg_corr[0]
    neg_corr_top2 = neg_corr[1]

    val1 = daily_dict[daily_top_company1][1:]
    val2 = daily_dict[daily_top_company2][1:]
    val3 = daily_dict[neg_corr_top1][1:]
    val4 = daily_dict[neg_corr_top2][1:]

    df_top_daily = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 200)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([daily_top_company1] * 199)
    comp.extend([daily_top_company2] * 199)
    comp.extend([neg_corr_top1] * 199)
    comp.extend([neg_corr_top2] * 199)

    df_top_daily['profit or loss'] = value
    df_top_daily['company'] = comp
    df_top_daily['days'] = days

    fig1 = px.line(df_top_daily, x="days", y="profit or loss", color='company')
    fig1.write_html("top2_daily_negative_corr.html")

    print("The bottom companies(daily) are " +
          daily_bottom_comp[0]+" and "+daily_bottom_comp[1])
    daily_bottom_company1 = daily_bottom_comp[0]
    daily_bottom_company2 = daily_bottom_comp[1]

    res = df_daily.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[daily_bottom_company1][:2].index.tolist()
    neg_corr_bottom1 = neg_corr[0]
    neg_corr_bottom2 = neg_corr[1]

    val1 = daily_dict[daily_bottom_company1][1:]
    val2 = daily_dict[daily_bottom_company2][1:]
    val3 = daily_dict[neg_corr_bottom1][1:]
    val4 = daily_dict[neg_corr_bottom2][1:]

    df_bottom_daily = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 200)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([daily_bottom_company1] * 199)
    comp.extend([daily_bottom_company2] * 199)
    comp.extend([neg_corr_bottom1] * 199)
    comp.extend([neg_corr_bottom2] * 199)

    df_bottom_daily['profit or loss'] = value
    df_bottom_daily['company'] = comp
    df_bottom_daily['days'] = days

    fig2 = px.line(df_bottom_daily, x="days",
                   y="profit or loss", color='company')
    fig2.write_html("bottom2_daily_negative_corr.html")

    client = pdfcrowd.HtmlToPdfClient(
        'demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    client.convertFileToFile(
        "bottom2_daily_negative_corr.html", "bottom2_daily_negative_corr.pdf")

    client.convertFileToFile(
        "top2_daily_negative_corr.html", "top2_daily_negative_corr.pdf")


def analyse_weekly():
    df_weekly = pd.read_csv("weekly_answer.csv")
    weekly_group = df_weekly.groupby(
        'Symbol')['Loss or Gain'].sum().reset_index()

    weekly_top = weekly_group.sort_values(by='Loss or Gain', ascending=False)
    weekly_bottom = weekly_group.sort_values(by='Loss or Gain')
    weekly_top_val = weekly_top['Loss or Gain'].tolist()[:25]
    weekly_top_comp = weekly_top['Symbol'].tolist()[:25]
    weekly_bottom_val = weekly_bottom['Loss or Gain'].tolist()[:25]
    weekly_bottom_comp = weekly_bottom['Symbol'].tolist()[:25]

    weekly_dict = {}
    for i in weekly_top_comp:
        temp_df = df_weekly[df_weekly['Symbol'] == i]
        weekly_dict[i] = temp_df['Loss or Gain'].tolist()[:43]
    for i in weekly_bottom_comp:
        temp_df = df_weekly[df_weekly['Symbol'] == i]
        weekly_dict[i] = temp_df['Loss or Gain'].tolist()[:43]

    keys = list(weekly_dict.keys())
    df_weekly = pd.DataFrame(weekly_dict, columns=keys)

    print("The top companies(weekly) are " +
          weekly_top_comp[0]+" and "+weekly_top_comp[1])
    weekly_top_company1 = weekly_top_comp[0]
    weekly_top_company2 = weekly_top_comp[1]

    res = df_weekly.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[weekly_top_company1][:2].index.tolist()
    neg_corr_top1 = neg_corr[0]
    neg_corr_top2 = neg_corr[1]

    val1 = weekly_dict[weekly_top_company1][1:]
    val2 = weekly_dict[weekly_top_company2][1:]
    val3 = weekly_dict[neg_corr_top1][1:]
    val4 = weekly_dict[neg_corr_top2][1:]

    df_top_weekly = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 43)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([weekly_top_company1] * 42)
    comp.extend([weekly_top_company2] * 42)
    comp.extend([neg_corr_top1] * 42)
    comp.extend([neg_corr_top2] * 42)

    df_top_weekly['profit or loss'] = value
    df_top_weekly['company'] = comp
    df_top_weekly['days'] = days

    fig3 = px.line(df_top_weekly, x="days",
                   y="profit or loss", color='company')
    fig3.write_html("top2_weekly_negative_corr.html")

    print("The bottom companies(weekly) are " +
          weekly_bottom_comp[0]+" and "+weekly_bottom_comp[1])
    weekly_bottom_company1 = weekly_bottom_comp[0]
    weekly_bottom_company2 = weekly_bottom_comp[1]

    res = df_weekly.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[weekly_bottom_company1][:2].index.tolist()
    neg_corr_bottom1 = neg_corr[0]
    neg_corr_bottom2 = neg_corr[1]

    val1 = weekly_dict[weekly_bottom_company1][1:]
    val2 = weekly_dict[weekly_bottom_company2][1:]
    val3 = weekly_dict[neg_corr_bottom1][1:]
    val4 = weekly_dict[neg_corr_bottom2][1:]

    df_bottom_weekly = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 43)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([weekly_bottom_company1] * 42)
    comp.extend([weekly_bottom_company2] * 42)
    comp.extend([neg_corr_bottom1] * 42)
    comp.extend([neg_corr_bottom2] * 42)

    df_bottom_weekly['profit or loss'] = value
    df_bottom_weekly['company'] = comp
    df_bottom_weekly['days'] = days

    fig4 = px.line(df_bottom_weekly, x="days",
                   y="profit or loss", color='company')
    fig4.write_html("bottom2_weekly_negative_corr.html")

    client = pdfcrowd.HtmlToPdfClient(
        'demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    client.convertFileToFile(
        "bottom2_weekly_negative_corr.html", "bottom2_weekly_negative_corr.pdf")

    client.convertFileToFile(
        "top2_weekly_negative_corr.html", "top2_weekly_negative_corr.pdf")


def analyse_monthly():
    df_monthly = pd.read_csv("monthly_answer.csv")
    monthly_group = df_monthly.groupby(
        'Symbol')['Loss or Gain'].sum().reset_index()

    monthly_top = monthly_group.sort_values(by='Loss or Gain', ascending=False)
    monthly_bottom = monthly_group.sort_values(by='Loss or Gain')
    monthly_top_val = monthly_top['Loss or Gain'].tolist()[:25]
    monthly_top_comp = monthly_top['Symbol'].tolist()[:25]
    monthly_bottom_val = monthly_bottom['Loss or Gain'].tolist()[:25]
    monthly_bottom_comp = monthly_bottom['Symbol'].tolist()[:25]

    monthly_dict = {}
    for i in monthly_top_comp:
        temp_df = df_monthly[df_monthly['Symbol'] == i]
        monthly_dict[i] = temp_df['Loss or Gain'].tolist()[:49]
    for i in monthly_bottom_comp:
        temp_df = df_monthly[df_monthly['Symbol'] == i]
        monthly_dict[i] = temp_df['Loss or Gain'].tolist()[:49]

    keys = list(monthly_dict.keys())
    df_monthly = pd.DataFrame(monthly_dict, columns=keys)

    print("The top companies(monthly) are " +
          monthly_top_comp[0]+" and "+monthly_top_comp[1])
    monthly_top_company1 = monthly_top_comp[0]
    monthly_top_company2 = monthly_top_comp[1]

    res = df_monthly.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[monthly_top_company1][:2].index.tolist()
    neg_corr_top1 = neg_corr[0]
    neg_corr_top2 = neg_corr[1]

    val1 = monthly_dict[monthly_top_company1][1:]
    val2 = monthly_dict[monthly_top_company2][1:]
    val3 = monthly_dict[neg_corr_top1][1:]
    val4 = monthly_dict[neg_corr_top2][1:]

    df_top_monthly = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 49)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([monthly_top_company1] * 48)
    comp.extend([monthly_top_company2] * 48)
    comp.extend([neg_corr_top1] * 48)
    comp.extend([neg_corr_top2] * 48)

    df_top_monthly['profit or loss'] = value
    df_top_monthly['company'] = comp
    df_top_monthly['days'] = days

    fig5 = px.line(df_top_monthly, x="days",
                   y="profit or loss", color='company')
    fig5.write_html("top2_monthly_negative_corr.html")

    print("The bottom companies(monthly) are " +
          monthly_bottom_comp[0]+" and "+monthly_bottom_comp[1])
    monthly_bottom_company1 = monthly_bottom_comp[0]
    monthly_bottom_company2 = monthly_bottom_comp[1]

    res = df_monthly.corr().unstack().sort_values().drop_duplicates()
    neg_corr = res[monthly_bottom_company1][:2].index.tolist()
    neg_corr_bottom1 = neg_corr[0]
    neg_corr_bottom2 = neg_corr[1]

    val1 = monthly_dict[monthly_bottom_company1][1:]
    val2 = monthly_dict[monthly_bottom_company2][1:]
    val3 = monthly_dict[neg_corr_bottom1][1:]
    val4 = monthly_dict[neg_corr_bottom2][1:]

    df_bottom_monthly = pd.DataFrame()
    value = []
    value.extend(val1)
    value.extend(val2)
    value.extend(val3)
    value.extend(val4)

    days = []
    mul = [i for i in range(1, 49)]
    for i in range(4):
        days.extend(mul)

    comp = []
    comp.extend([monthly_bottom_company1] * 48)
    comp.extend([monthly_bottom_company2] * 48)
    comp.extend([neg_corr_bottom1] * 48)
    comp.extend([neg_corr_bottom2] * 48)

    df_bottom_monthly['profit or loss'] = value
    df_bottom_monthly['company'] = comp
    df_bottom_monthly['days'] = days

    fig6 = px.line(df_bottom_monthly, x="days",
                   y="profit or loss", color='company')
    fig6.write_html("bottom2_monthly_negative_corr.html")

    # img.seek(0)
    # with open("imdb_bargraph.html", "w") as file:
    # file.write('<div><img src="data:image/png;base64,{}"/></div>'.format(res))

    client = pdfcrowd.HtmlToPdfClient(
        'demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    client.convertFileToFile(
        "bottom2_monthly_negative_corr.html", "bottom2_monthly_negative_corr.pdf")

    client.convertFileToFile(
        "top2_monthly_negative_corr.html", "top2_monthly_negative_corr.pdf")


analyse_daily()
analyse_weekly()
analyse_monthly()
