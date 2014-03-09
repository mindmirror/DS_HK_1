import pandas as pd
from sklearn import linear_model, feature_selection

logm = linear_model.LogisticRegression()

def good(x):
    if x > 4.3:
        return 1
    else:
        return 0

url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'

beer = pd.read_csv(url, delimiter="\t")
beer = beer.dropna()
beer['Good'] = beer['WR'].apply(good)

input = beer[['Reviews', 'ABV']].values
good = beer['Good'].values

logm.fit(input, good)
print logm.score(input, good)

# Prediction with beer type
beer_types = ['Ale', 'Stout', 'IPA', 'Lager']
for t in beer_types:
    beer[t] = beer['Type'].str.contains(t) * 1

select = ['Reviews', 'ABV', 'Ale', 'Stout', 'IPA', 'Lager']
input = beer[select].values
logm.fit(input, good)
print logm.score(input, good)
