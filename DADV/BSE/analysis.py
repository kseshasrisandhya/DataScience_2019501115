import plotly.graph_objs as go
import plotly.io as pio
from scipy.stats import pearsonr
from numpy.random import seed
from numpy.random import randn
import csv
import pandas as pd
import pickle
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px
import pdfcrowd
import pdfkit

with open('companies.pickle', 'rb') as handle:
    dict_companies = pickle.load(handle)


def last_5_year_closing_price():
    df = pd.read_csv('company_share_details.csv')
    df_close_price = df[['Date', 'Close Price', 'company']]
    df_close_price.to_csv('last_5_year_close.csv')


def transform_data():
    df = pd.read_csv('company_share_details.csv')
    date_list = df['Date'].tolist()
    month_list = []
    day_list = []
    year_list = []
    for i in range(len(date_list)):
        day, month, year = date_list[i].split('-')
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
    df['year'] = year_list
    df['month'] = month_list
    df['day'] = day_list
    return df


def gain_last_month():
    last_month_first_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '1')]
    last_month_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_month_first_day[['Close Price', 'company', 'Date']]
    df2 = last_month_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_month = []
    gain_month = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_month.append(i[0])
        gain_month.append(i[1])
    return company_month, gain_month


def gain_last_3_months():
    last_3_months_first_day = df[(df['year'] == '2021') & (
        df['month'] == 'January') & (df['day'] == '1')]
    last_3_months_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_3_months_first_day[['Close Price', 'company', 'Date']]
    df2 = last_3_months_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_3_months = []
    gain_3_months = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_3_months.append(i[0])
        gain_3_months.append(i[1])
    return company_3_months, gain_3_months


def gain_last_6_months():
    last_6_months_first_day = df[(df['year'] == '2020') & (
        df['month'] == 'October') & (df['day'] == '1')]
    last_6_months_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_6_months_first_day[['Close Price', 'company', 'Date']]
    df2 = last_6_months_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_6_months = []
    gain_6_months = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_6_months.append(i[0])
        gain_6_months.append(i[1])
    return company_6_months, gain_6_months


def gain_last_year():
    last_year_first_day = df[(df['year'] == '2020') & (
        df['month'] == 'March') & (df['day'] == '2')]
    last_year_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_year_first_day[['Close Price', 'company', 'Date']]
    df2 = last_year_last_day[['Close Price', 'company', 'Date']]
    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_year = []
    gain_year = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_year.append(i[0])
        gain_year.append(i[1])
    return company_year, gain_year


def gain_last_2_years():
    last_2_years_first_day = df[(df['year'] == '2019') & (
        df['month'] == 'March') & (df['day'] == '1')]
    last_2_years_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_2_years_first_day[['Close Price', 'company', 'Date']]
    df2 = last_2_years_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_2_years = []
    gain_2_years = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_2_years.append(i[0])
        gain_2_years.append(i[1])
    return company_2_years, gain_2_years


def gain_last_3_years():
    last_3_years_first_day = df[(df['year'] == '2018') & (
        df['month'] == 'March') & (df['day'] == '1')]
    last_3_years_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_3_years_first_day[['Close Price', 'company', 'Date']]
    df2 = last_3_years_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_3_years = []
    gain_3_years = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_3_years.append(i[0])
        gain_3_years.append(i[1])
    return company_3_years, gain_3_years


def gain_last_5_years():
    last_5_years_first_day = df[(df['year'] == '2016') & (
        df['month'] == 'April') & (df['day'] == '5')]
    last_5_years_last_day = df[(df['year'] == '2021') & (
        df['month'] == 'March') & (df['day'] == '31')]
    df1 = last_5_years_first_day[['Close Price', 'company', 'Date']]
    df2 = last_5_years_last_day[['Close Price', 'company', 'Date']]

    company_list = df1['company'].tolist()
    dict_value = {}
    for company in company_list:
        first_day = df1[df1['company'] == company]['Close Price'].tolist()[0]
        last_day = df2[df2['company'] == company]['Close Price'].tolist()
        if(last_day == []):
            continue
        else:
            last_day = last_day[0]
            gain = (last_day / first_day) - 1
            dict_value[company] = gain
    company_5_years = []
    gain_5_years = []
    for i in sorted(dict_value.items(), key=lambda item: item[1], reverse=True)[:10]:
        company_5_years.append(i[0])
        gain_5_years.append(i[1])
    return company_5_years, gain_5_years


def correlation_ICICI():
    # company with most correlation with ICICI = 500271
    # correlation with ICICI = 0.96836
    company_name = 'ICICI BANK LTD.'
    company_code = ''
    for i in dict_companies:
        if(company_name == dict_companies[i]):
            company_code = i
            break

    df_icici = df[(df['company'] == int(company_code)) & (
        df['year'] == '2021') & (df['month'] == 'March')]['Close Price']
    icici_list = df_icici.tolist()
    dict_correlation = {}
    for i in dict_companies:
        print(i)
        df_comp = df[(df['company'] == int(i)) & (
            df['year'] == '2021') & (df['month'] == 'March')]['Close Price']
        other_company_list = df_comp.tolist()
        if(other_company_list != [] and len(other_company_list) >= 15):
            corr, _ = pearsonr(icici_list[:15], other_company_list[:15])
            dict_correlation[i] = corr
    for i in sorted(dict_correlation.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(i)


def correlation_30_companies(df):
    company_list = [500003, 500008, 500009, 500010, 500012, 500013, 500014,
                    500016, 500020, 500023, 500027, 500028, 500031, 500032, 500033, 500034,
                    500038, 500039, 500040, 500041, 500042, 500043, 500048, 500049, 500052,
                    500055, 500060, 500067, 500125, 500126]

    company_names = [dict_companies[str(i)] for i in company_list]
    dict_30 = {}

    for i in company_list:
        df_comp = df[(df['company'] == int(i)) & (
            df['year'] == '2021') & (df['month'] == 'March')]['Close Price']
        dict_30[i] = df_comp.tolist()[:15]

    keys = list(dict_30.keys())
    df_30 = pd.DataFrame(dict_30, columns=keys)
    corrMatrix = df_30.corr()
    fig1 = px.imshow(corrMatrix, color_continuous_scale=[
        "red", "green"])
    fig1.show()
    fig1.write_html("correlation_30_companies.html")

    # img.seek(0)
    # with open("imdb_bargraph.html", "w") as file:
    # file.write('<div><img src="data:image/png;base64,{}"/></div>'.format(res))
    mat = []
    for i in dict_30:
        count = 0
        for j in dict_30[i]:
            single = []
            count += 1
            single.append(dict_companies[str(i)])
            single.append(count)
            single.append(j)
            mat.append(single)

    df5 = pd.DataFrame(mat, columns=['company', 'day', 'stock_price'])
    fig2 = px.line(df5, x="day", y="stock_price", color='company')
    fig2.show()
    fig2.write_html("closing_stock_price.html")

    # img.seek(0)
    # with open("imdb_bargraph.html", "w") as file:
    # file.write('<div><img src="data:image/png;base64,{}"/></div>'.format(res))

    client = pdfcrowd.HtmlToPdfClient(
        'demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    client.convertFileToFile(
        "closing_stock_price.html", "closing_stock_price.pdf")

    client.convertFileToFile(
        "correlation_30_companies.html", "correlation_30_companies.pdf")


df = transform_data()
# correlation_ICICI()
correlation_30_companies(df)

company_month, gain_month = gain_last_month()
company_3_months, gain_3_months = gain_last_3_months()
company_6_months, gain_6_months = gain_last_6_months()

company_year, gain_year = gain_last_year()

company_2_years, gain_2_years = gain_last_2_years()
company_3_years, gain_3_years = gain_last_3_years()
company_5_years, gain_5_years = gain_last_5_years()


print("Top 10 companies last month gain")
for i in range(len(company_month)):
    print(dict_companies[str(company_month[i])], gain_month[i])
print()

print("Top 10 companies last 3 months gain")
for i in range(len(company_3_months)):
    print(dict_companies[str(company_3_months[i])], gain_3_months[i])
print()

print("Top 10 companies last 6 months gain")
for i in range(len(company_6_months)):
    print(dict_companies[str(company_6_months[i])], gain_6_months[i])
print()

print("Top 10 companies last year gain")
for i in range(len(company_year)):
    print(dict_companies[str(company_year[i])], gain_year[i])
print()

print("Top 10 companies last 2 years gain")
for i in range(len(company_2_years)):
    print(dict_companies[str(company_2_years[i])], gain_2_years[i])
print()

print("Top 10 companies last 3 years gain")
for i in range(len(company_3_years)):
    print(dict_companies[str(company_3_years[i])], gain_3_years[i])
print()

print("Top 10 companies last 5 years gain")
for i in range(len(company_5_years)):
    print(dict_companies[str(company_5_years[i])], gain_5_years[i])

company_code = 500271
val = 0.96836
for i in dict_companies:
    if(company_code == int(i)):
        company = dict_companies[i]
        break
print("The company which is mostly correlated with ICICI Bank is " +
      company+" with a correlation of "+str(val))
