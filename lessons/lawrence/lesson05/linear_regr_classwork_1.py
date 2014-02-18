"""
Go through the same steps, but this time generate a new model use the log of
brain and body, which we know generated a much better distribution and cleaner
set of data. Compare the results to the original model. Remember that exp() can
be used to "normalize" our "logged" values. Note: Make sure you start a new
linear regression object!
"""

import pandas as pd
import matplotlib.pyplot as plt
from numpy import log, exp, mean
from sklearn import linear_model

mammals = pd.read_csv('mammals.csv')
mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])

linear_regr = linear_model.LinearRegression()
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
linear_regr.fit(body, brain)

log_regr = linear_model.LinearRegression()
log_body = [[x] for x in mammals['log_body'].values]
log_brain = log(mammals['brain'].values)
log_regr.fit(log_body, log_brain)

print "Log body and brian linear coefficient: " + str(log_regr.coef_)
print "Sum of squared residuals: " + str(mean((log_regr.predict(log_body) - log_brain) ** 2))
print "R^2: " + str(log_regr.score(log_body, log_brain))

plt.scatter(body, brain)
plt.plot(body, linear_regr.predict(body), color='blue', linewidth=3)
mammals = mammals.sort('body')
sorted_log_body = [[x] for x in mammals['log_body'].values]
# Convert the log linear model back to normal by exponent
plt.plot(exp(sorted_log_body), exp(log_regr.predict(sorted_log_body)), color='red', linewidth=3)
plt.show()
