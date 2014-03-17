import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import feature_selection, linear_model

# Create a new dataframe
base = pd.read_csv('./baseball.csv')

# Select numerical feature
base = pd.DataFrame(base, columns=["HR", "RBI", 'R', "G", "SB", "salary", 'height', 'weight', 'yearID'])

'''
Fill null values with mean of each columns: The reason I chose this
strategy was because I did not want to drop rows due to null values,
and my thought was filling in the null values with the mean of each
column would not affect the results of the regression, since it would
not add outliers to the data.
'''
baseFill = base.fillna(base.mean())

# Response
salary = baseFill['salary'].values

# Input
baseInput = baseFill[["HR", "RBI", 'R', "G", "SB", 'height', 'weight', 'yearID']].values

# Run feature analysis
features = feature_selection.univariate_selection.f_regression(baseInput, salary)

'''
F-score Results: array([ 2090.11260191,  1678.169398  ,  1353.50419942,   769.57688219,
                         88.34818387,   108.90139059,   735.57166992,  3030.35804155])

p-value results: array([  0.00000000e+000,   0.00000000e+000,   1.24250552e-287, 1.58531873e-166,
                          6.00661344e-021,   1.95464482e-025,  2.24061309e-159,   0.00000000e+000])

Based on these results we know "HR", "RBI", "R" and "yearID" are significant features. We can use
these four features for out model. Worth noting none of these are surprising: Home Runs, Runs Batted
In and Runs scored all are hugely important in helping a baseball club win games, thus a player with
more of these statistics seems reasonably like to earn a higher salary. Additionally, as Business
Insider show demonstrates
(http://www.businessinsider.com/chart-of-the-day-major-league-baseball-salaries-since-1970-2011-1)
The average salary in Major League Baseball has grown exponentially over the past 40 years as TV deals
and sponsorship agreements have driven club revenue, and athletes have gains a more prominent role
in American society.
'''

# Seperate significant features
sig = [ [a, b, c, d] for a, b, c, d in zip(baseFill['HR'].values, baseFill['RBI'].values, baseFill['R'].values, baseFill['yearID'].values)]
sig = baseFill[['HR', 'RBI', 'R', 'yearID']].values

# Use ridge regression model
ridge = linear_model.Ridge()
salaryFit = ridge.fit(sig, salary)

# Predict salary based on fit of features
salaryPredict = salaryFit.predict(sig)

# Check score of the regression fit
salaryFit.score(sig, salary)
# Result: 0.20799776836490136 This terrible.
