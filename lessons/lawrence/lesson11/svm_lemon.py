from pandas import DataFrame, read_csv

l_train = read_csv('lemon_training.csv')
features = list(l_train.describe().columns)
l_train = l_train[features].dropna(axis=0)

features.remove('RefId')
features.remove('IsBadBuy')
features.remove('BYRNO')
features.remove('VNZIP1')

train_x = lemon_train[features].values
train_y = lemon_train.IsBadBuy.values
