# from bs4 import BeautifulSoup
# import requests
# import pandas
# import io
# import csv
# import gzip

# url = "https://datasets.imdbws.com/"

# response = requests.get(url)
# soup = BeautifulSoup(response.text,"html.parser")

# urlsList = []
# for link in soup.find_all('a'):
#     urlsList.append(link.get('href'))

# nameBasics = urlsList[1]
# titleAkas = urlsList[2]
# titleBasics = urlsList[3]
# titleCrew = urlsList[4]
# titleEpisode = urlsList[5]
# titlePrincipals = urlsList[6]
# titleRatings = urlsList[7]

# titleRatingsResponse = requests.get(titleRatings)
# bytes_io = io.BytesIO(titleRatingsResponse.content)
# with gzip.open(bytes_io, 'rt') as read_file:
#     df = pandas.read_csv(read_file,delimiter='\t')
# df_rating = df[df['averageRating'] > 8.0]
# df_rating = df_rating.sort_values(by=['numVotes','averageRating'], ascending = False)
# # print(df_rating.head(20))
# titleConstList = df_rating['tconst'].head(20).tolist()
# print(titleConstList)
# #*********************************
# titleBasicsResponse = requests.get(titleBasics)
# bytes_io_basics = io.BytesIO(titleBasicsResponse.content)
# data = pandas.read_csv(bytes_io_basics, delimiter="\t", compression='gzip', chunksize=50000, error_bad_lines=False)
# output = []
# for chunk in data:
#     variable1 = chunk[chunk.tconst.isin(titleConstList)]
#     if not variable1.empty and len(output) == 0:
#         output.append(variable1)
#     elif not variable1.empty:
#         output[0] = pandas.concat([output[0], variable1], axis=0)
#         # output = pandas.concat([output, variable], axis=0)
# print(output[0])
# print("*****************************************")
# #**********************************
# df_votes = df[df['numVotes'] > 40000]
# df_votes = df_votes.sort_values(by=['numVotes','averageRating'], ascending = False)
# votesList = df_votes.tconst.tolist()
# titleBasicsResponse = requests.get(titleBasics)
# bytes_io_basics = io.BytesIO(titleBasicsResponse.content)
# data = pandas.read_csv(bytes_io_basics, delimiter="\t", compression='gzip', chunksize=50000, error_bad_lines=False)
# out = []
# for chunk in data:
#     chunk['startYear'] = pandas.to_numeric(chunk['startYear'], errors="coerce")
#     variable = chunk[(chunk.tconst.isin(votesList)) & (chunk.startYear >= 2000)]
#     if not variable.empty and len(out) == 0:
#         out.append(variable)
#     elif not variable.empty:
#         out[0] = pandas.concat([out[0], variable], axis=0)
#         # output = pandas.concat([output, variable], axis=0)
# bestVotesList = df_votes.tconst.head(50).tolist()
# print(bestVotesList)
# bestMovies = out[0]
# bestMovies = bestMovies[bestMovies.tconst.isin(bestVotesList)]
# print(bestMovies.head(20))

import template
t = template.Template("<html>{{ myvalue }}</html>")
print(t.generate(myvalue="XXX"))


def add(x, y):
    return x + y


template.execute(add=add)

# The template
{{add(1, 2)}}
