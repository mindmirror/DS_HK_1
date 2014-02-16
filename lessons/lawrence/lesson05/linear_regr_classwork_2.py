"""
Using your aggregate data compiled from nytimes1-30.csv, write a python script that determines the best model predicting
CTR based off of age and gender. Since gender is not actually numeric (it is binary), investigate ways to vectorize this
feature. Clue: you may want two features now instead of one.
"""

import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean
from sklearn import linear_model

nyt = pd.read_csv('nyagg.csv')
regr = linear_model.LinearRegression()
age_gender = [[row['Age'], row['Gender']] for index, row in nyt.iterrows()]
ctr = nyt['Ctr'].values
regr.fit(age_gender, ctr)

print regr.coef_
print mean((regr.predict(age_gender) - ctr) ** 2)
print regr.score(age_gender, ctr)
plt.plot(age_gender, regr.predict(age_gender), color='blue', linewidth=3)
plt.show()
