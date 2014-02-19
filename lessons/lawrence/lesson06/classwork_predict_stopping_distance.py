import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# Predict the stopping distance based on the speed and stopping distance data points
cars = pd.read_csv('cars1920.csv')
cars = cars.sort('speed')

# 1. Try the linear model first, see how does it fit
lm = linear_model.LinearRegression()
speed = cars[['speed']].values
dist = cars['dist'].values
lm.fit(speed,dist)
print "Linear model coefficient: " + str(lm.coef_)
print "Linear model score: " + str(lm.score(speed, dist))

# 2. See how does the log linear model fit
log_lm = linear_model.LinearRegression()
log_speed = [[x] for x in np.log(cars['speed'].values)]
log_dist = np.log(cars['dist'])
log_lm.fit(log_speed, log_dist)
print "Log linear model coefficient: " + str(log_lm.coef_)
print "Log linear model score: " + str(log_lm.score(log_speed, log_dist))

# 3. Lastly, try the polynomial model
ridge = linear_model.Ridge()
cars['speed_squared'] = cars['speed'] ** 2
speed_squared = [[x, y] for x,y in zip(cars['speed'].values, cars['speed_squared'].values)]
ridge.fit(speed_squared, dist)
print "Ridge regression model coefficient: " + str(ridge.coef_)
print "Ridge regression model score: " + str(ridge.score(speed_squared, dist))

# Plot the predictions
plt.scatter(speed, dist, color='black')
plt.plot(speed, lm.predict(speed), color='blue')
plt.plot(np.exp(log_speed), np.exp(log_lm.predict(log_speed)), color='green')
plt.plot(speed, ridge.predict(speed_squared), color='red')
plt.show()

"""
Since the log linear model have the highest SSE, it fits the data best, which means the car stopping distance increases
expoentially as the speed increases.
"""
