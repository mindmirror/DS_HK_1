"""
Compare this practice to making two separate models based on Gender, with Age as your one feature predicting CTR. How
are your results different? Which results would you be more confident in presenting to your manager? Why's that?
"""

import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean
from sklearn import linear_model

nyt = pd.read_csv('nyagg.csv')
nyt_gender_0 = nyt[nyt['Gender'] == 0]
age_gender_0 = [[x] for x in nyt_gender_0['Age'].values]
ctr_gender_0 = nyt_gender_0['Ctr'].values

nyt_gender_1 = nyt[nyt['Gender'] == 1]
age_gender_1 = [[x] for x in nyt_gender_1['Age'].values]
ctr_gender_1 = nyt_gender_1['Ctr'].values

regr_gender_0 = linear_model.LinearRegression()
regr_gender_0.fit(age_gender_0, ctr_gender_0)
print regr_gender_0.coef_
print regr_gender_0.score(age_gender_0, ctr_gender_0)
regr_gender_1 = linear_model.LinearRegression()
regr_gender_1.fit(age_gender_1, ctr_gender_1)
print regr_gender_1.coef_
print regr_gender_1.score(age_gender_1, ctr_gender_1)

# Plot different gender in different color
plt.scatter(age_gender_0, ctr_gender_0, color='red')
plt.plot(age_gender_0, regr_gender_0.predict(age_gender_0), color='red', linewidth=3)
plt.scatter(age_gender_1, ctr_gender_1, color='blue')
plt.plot(age_gender_1, regr_gender_1.predict(age_gender_1), color='blue', linewidth=3)
plt.show()

