import pandas as pd
from sklearn import tree, metrics

lemon_train = pd.read_csv('lemon_training.csv')
lemon_test = pd.read_csv('lemon_test.csv')

train_features = list(lemon_train.describe().columns)
test_features = list(lemon_test.describe().columns)
lemon_train = lemon_train[train_features].dropna(axis=0)
lemon_test = lemon_test[test_features].dropna(axis=0)

train_features.remove('RefId')
train_features.remove('IsBadBuy')
train_features.remove('BYRNO')
train_features.remove('VNZIP1')

test_features.remove('RefId')
test_features.remove('BYRNO')
test_features.remove('VNZIP1')

train_x = lemon_train[train_features].values
train_y = lemon_train.IsBadBuy.values
test_x = lemon_test[test_features].values

clf = tree.DecisionTreeClassifier().fit(train_x, train_y)
pred_y = clf.predict(test_x)
#print "Hit: %d" % (test_y == pred_y).sum()
#print "Mis: %d" % (test_y != pred_y).sum()
#print metrics.classification_report(test_y, pred_y)
submission = pd.DataFrame({'RefId': lemon_test.RefId, 'prediction': pred_y})
submission.to_csv('submission.csv', index=False)