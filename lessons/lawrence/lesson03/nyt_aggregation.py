from __future__ import division
import pandas as pd
import numpy

df = pd.DataFrame()
for i in range(1, 31):
    csv = pd.read_csv('nyt' + str(i) + '.csv')
    df = df.append(csv)

dfg = df[['Age','Gender','Signed_In', 'Impressions','Clicks']].groupby(['Age','Gender','Signed_In']).sum()
dfg['CTR'] = dfg.apply(lambda row: 0 if['Impressions'] == 0 else row['Clicks'] / row['Impressions'], axis = 1)
dfg.to_csv('nytimes_aggregation.csv', float_format='%.4f')
