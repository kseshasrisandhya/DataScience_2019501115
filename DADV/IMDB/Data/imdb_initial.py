import pdfkit
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import plotly.express as px
import pdfcrowd


def load_title_ratings():
    print("Loading title ratings")
    df_ratings = pd.read_csv(
        'F:/Data_Visualisation/IMDB/Data/title_ratings/title.ratings.txt', sep='\s+')
    return df_ratings


def load_title_basics():
    print("Loading title basics")
    df_basics = pd.read_csv(
        'F:/Data_Visualisation/IMDB/Data/title_basics/title.basics.txt', delimiter='\t')
    return df_basics


def merge_ratings_basics_1(df_ratings, df_basics):
    df_ratings['averageRating'] = df_ratings['averageRating'].astype(float)
    samp_rating = df_ratings[df_ratings['averageRating'] > 8.0]
    samp_basics = df_basics[df_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_rating, samp_basics, on='tconst')
    samp_df.sort_values(by=['numVotes', 'averageRating'],
                        inplace=True, ascending=False)
    print("-------------------------------------------------")
    print("20 most popular movies with a rank more tham 8.0")
    print(samp_df[['originalTitle', 'numVotes', 'averageRating']][:20])


def merge_ratings_basics_2(df_ratings, df_basics):
    df_ratings['numVotes'] = df_ratings['numVotes'].astype(int)
    samp_rating = df_ratings[df_ratings['numVotes'] > 40000]
    samp_basics = df_basics[df_basics['titleType'] == 'movie']
    samp_basics = samp_basics[samp_basics['startYear'].astype(
        str).str.isdigit()]
    samp_basics['startYear'] = samp_basics['startYear'].astype(int)
    samp_basics = samp_basics[samp_basics['startYear'] >= 2000]
    samp_df = pd.merge(samp_rating, samp_basics, on='tconst')
    samp_df.sort_values(by=['averageRating'],
                        inplace=True, ascending=False)
    print("---------------------------------------------------------------")
    print("20 best rated movies released after 2000 with over 40,000 votes")
    print(samp_df[['originalTitle', 'averageRating']][:20])
    # samp_df.to_csv('top_20_popular_movies_rating_more_than_8.csv')


def avg_rank_most_popular_2000_2009(df_ratings, df_basics):
    samp_basics = df_basics[df_basics['startYear'].astype(str).str.isdigit()]
    samp_basics['startYear'] = samp_basics['startYear'].astype(int)
    samp_basics = samp_basics[(samp_basics['startYear'] >= 2000) &
                              (samp_basics['startYear'] <= 2009)]
    samp_basics = samp_basics[samp_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_basics, df_ratings, on='tconst')
    samp_df.sort_values(by=['numVotes', 'averageRating'],
                        ascending=False, inplace=True)
    mean_2000_2009 = samp_df['averageRating'][:10].mean()
    print("---------------------------------------------------------------")
    print("Average rank for the 10 most popular movies from 2000 to 2009(inclusive)", mean_2000_2009)


def year_comparison(df_ratings, df_basics):
    samp_basics = df_basics[df_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_basics, df_ratings, on='tconst')
    samp_df = samp_df[samp_df['numVotes'] >= 1000]
    samp_df = samp_df[samp_df['startYear'].astype(str).str.isdigit()]
    samp_df['startYear'] = samp_df['startYear'].astype(int)
    samp_df = samp_df[(samp_df['startYear'] >= 1900) &
                      (samp_df['startYear'] <= 2000)]
    samp = samp_df.groupby('startYear')
    y, mean_val = get_mean_array(samp)
    year, diff = max_diff_year(y, mean_val)
    print("The year in which the average rank increased the most when compared to previous year is",
          year, " and the difference is", diff)


def get_mean_array(samp):
    y = []
    mean_val = []
    for i, j in samp:
        y.append(i)
        df = j.agg({'averageRating': ['mean']})
        for k in df:
            ob = df[k].tolist()[0]
        mean_val.append(ob)
    return y, mean_val


def max_diff_year(y, mean_val):
    diff_val = []
    maxi = -900
    index = 0
    for ind in range(1, len(y)):
        diff = mean_val[ind] - mean_val[ind-1]
        diff_val.append(diff)
        if(diff > maxi):
            maxi = diff
            index = ind
    return y[index], maxi


def linear_regression_2013(df_ratings, df_basics):
    samp_basics = df_basics[df_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_basics, df_ratings, on='tconst')
    samp_df = samp_df[samp_df['numVotes'] >= 1000]
    samp_df = samp_df[samp_df['startYear'].astype(str).str.isdigit()]
    samp_df['startYear'] = samp_df['startYear'].astype(int)
    samp_df = samp_df[['startYear', 'averageRating']]
    samp = samp_df.groupby('startYear')
    y, mean_val = get_mean_array(samp)
    observed_value = 0
    index = 0
    for i in range(len(y)):
        if(y[i] == 2013):
            observed_value = mean_val[i]
            index = i
            break
    predicted_value = perform_linear_regression(y, mean_val, index)
    accuracy = ((observed_value - predicted_value[0])/predicted_value[0]) * 100
    print("The observed value for 2013 is", observed_value)
    print("The predicted value for 2013 is", predicted_value[0])
    print("Accuracy is "+str(accuracy))


def perform_linear_regression(y, mean_val, index):
    y = [y[i] for i in range(len(y)) if(i != index)]
    mean_val = [mean_val[i] for i in range(len(mean_val)) if(i != index)]
    y = np.asarray(y)
    y = y.reshape((-1, 1))
    model = LinearRegression().fit(y, mean_val)
    arr = [2013]
    arr = np.asarray(arr)
    arr = arr.reshape((-1, 1))
    predicted_value = model.predict(arr)
    return predicted_value


def correlation_analysis(df_ratings, df_basics):
    samp_basics = df_basics[df_basics['startYear'].astype(str).str.isdigit()]
    samp_basics['startYear'] = samp_basics['startYear'].astype(int)
    samp_basics = samp_basics[(samp_basics['startYear'] >= 1900) & (
        samp_basics['startYear'] < 2000)]
    samp_basics = samp_basics[samp_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_basics, df_ratings, on='tconst')
    find_correlation(samp_df)


def find_correlation(samp_df):
    corr_details = {}
    for year in range(1900, 2000):
        print("Finding correlation for", year)
        val = get_correlation(samp_df[samp_df['startYear'] == year])
        if(val != 77):
            corr_details[year] = val
            print("Correlation for year "+str(year)+"= "+str(val))
    y = []
    r = []
    for i in corr_details:
        y.append(i)
        r.append(corr_details[i])

    result = []
    for j in range(1, len(y)):
        result.append(r[j]-r[j-1])
    print(result)


def get_correlation(sample):
    if(sample.empty):
        return 77
    df = sample[['averageRating', 'numVotes']]
    rating = []
    votes = []
    for ind in df.index:
        rating.append(sample.loc[ind, ['averageRating']])
        votes.append(sample.loc[ind, ['numVotes']])
    val = scipy.stats.spearmanr(rating, votes).correlation
    return val


def calculate_aggregate(samp_df):
    d = {'averageRating': ['sum'], 'numVotes': ['sum']}
    res = samp_df.groupby('startYear').agg(d)
    # res.set_index("startYear", drop=True, inplace=True)
    # dictionary = res.to_dict(orient="index")
    index_list = list(res.index)
    rating = []
    votes = []
    correlation = []
    for ind in index_list:
        rating.append((res.loc[ind, ['averageRating']]).tolist()[0])
        votes.append((res.loc[ind, ['numVotes']].tolist()[0]))

    for i in range(len(rating)):
        r = np.array([rating[i]])
        v = np.array([votes[i]])
        print(r, v)
        correlation.append(scipy.stats.spearmanr(r, v).correlation)
    print(correlation)


def plot_bubble():
    x = np.random.rand(40)
    y = np.random.rand(40)
    z = np.random.rand(40)
    colors = np.random.rand(40)
    plt.scatter(x, y, s=z*1000, c=colors)
    plt.show()


def plot_svg(df_ratings):
    df_movie_10k_votes = df_ratings[df_ratings['numVotes'] >=
                                    10000]
    ratings = df_movie_10k_votes['averageRating'].tolist()
    votes = df_movie_10k_votes['numVotes'].tolist()
    fig = px.scatter(df_movie_10k_votes, x="numVotes", y="averageRating",
                     labels=dict(numVotes="Number of Votes",
                                 averageRating="Rank")
                     )

    fig.write_html("imdb_scatter.html")


def number_of_movies_by_year(df_basics, df_ratings):
    samp_basics = df_basics[df_basics['titleType'] == 'movie']
    samp_df = pd.merge(samp_basics, df_ratings, on='tconst')
    samp_df = samp_df[samp_df['startYear'].astype(str).str.isdigit()]
    samp_df['startYear'] = samp_df['startYear'].astype(int)
    samp_df = samp_df[(samp_df['startYear'] >= 1900)]
    res = samp_df.groupby('startYear').agg('count')
    index_list = list(res.index)
    count_movies = []
    for ind in index_list:
        count_movies.append((res.loc[ind, ['tconst']]).tolist()[0])

    fig = px.bar(x=index_list, y=count_movies)
    fig.write_html("number_of_movies_by_year.html")

    client = pdfcrowd.HtmlToPdfClient(
        'demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    client.convertFileToFile(
        'number_of_movies_by_year.html', 'number_of_movies_by_year.pdf')

    # img.seek(0)
    # with open("imdb_bargraph.html", "w") as file:
    # file.write('<div><img src="data:image/png;base64,{}"/></div>'.format(res))


df_ratings = load_title_ratings()
df_basics = load_title_basics()
df_basics.to_csv("title.basics2.csv")
df_ratings.to_csv("title.ratings2.csv")

merge_ratings_basics_1(df_ratings, df_basics)
merge_ratings_basics_2(df_ratings, df_basics)

avg_rank_most_popular_2000_2009(df_ratings, df_basics)
year_comparison(df_ratings, df_basics)
linear_regression_2013(df_ratings, df_basics)

correlation_analysis(df_ratings, df_basics)
plot_bubble()
plot_svg(df_ratings)
number_of_movies_by_year(df_basics, df_ratings)
