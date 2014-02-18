import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

mammals = pd.read_csv('mammals.csv')
# Let's sort the data before doing any predictions
mammals = mammals.sort('body')
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
body = mammals[['body']].values
log_body = [[x] for x in np.log(mammals['body'].values)]
brain = mammals['brain'].values
log_brain = np.log(mammals['brain'].values)
lm.fit(body, brain)
log_lm.fit(log_body, log_brain)

print "Linear model intercept: " + str(lm.intercept_)
print "Log linear model intercept: " + str(log_lm.intercept_)
print "Linear model coefficient: " + str(lm.coef_)
print "Log linear model coefficient: " + str(log_lm.coef_)

mammals['predict'] = lm.predict(body)
mammals['log_predict'] = log_lm.predict(log_body)

# Plot the predictions
mammals_log_sort = mammals.sort('log_predict')
# Scatter the original data points (in blue)
plt.scatter(body, brain, color='blue')
# Scatter the predicted data points (in red)
plt.scatter(body, np.exp(log_lm.predict(log_body)), color='red')
plt.plot(body, mammals['predict'], np.exp(log_body), np.exp(mammals['log_predict']))
plt.show()
