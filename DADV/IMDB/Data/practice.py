import pandas as pd
# data_1 = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 
#                 'Age': [21, 19, 20, 18], 
#                 'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 
#                 'Percentage': [88, 92, 95, 70]} 
  

# df_1 = pd.DataFrame(data_1, columns = ['Name', 'Age', 'Stream', 'Percentage'])

# data_2 = {'Name': ['Ankit', 'Aishwarya'], 
#                 'Score': [91, 99], 
#                 'Rank': [2, 1]
#         } 
  

# df_2 = pd.DataFrame(data_2, columns = ['Name', 'Score', 'Rank'])
# data = pd.merge(df_1,df_2,on='Name')

# data_1 = {'Name': ['Ankit', 'Amit', 'Ankit', 'Priyanka','Ankit'], 
#                 'Age': [21, 19, 20, 18,34], 
#                 'Stream': ['Math', 'Commerce', 'Arts', 'Biology','History'], 
#                 'Percentage': [88, 92, 95, 70,23]}
# df_1 = pd.DataFrame(data_1, columns = ['Name', 'Age', 'Stream', 'Percentage'])
# print(df_1.groupby('Name'))

import scipy.stats
a = 1
b = 2
print(scipy.stats.spearmanr(a,b).correlation)