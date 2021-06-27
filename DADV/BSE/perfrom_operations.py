import pandas as pd
import os

path = 'F:/Data_Visualisation/BSE/company_details'


big_list = []
count = 0
for ele in os.listdir(path):

    company_file = path + '/' + ele
    if((os.path.getsize(company_file)/1024) < 15):
        continue
    else:
        count += 1
        df = pd.read_csv(company_file, index_col=None, header=0)
        df['company'] = ele[:-4]
        big_list.append(df)

frame = pd.concat(big_list, axis=0, ignore_index=True)
frame.to_csv('company_share_details.csv')
