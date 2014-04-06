from matplotlib import pyplot as plt
import pandas as pd
from sklearn import cluster
from sklearn.metrics import silhouette_score

# Read user impressions
user_impressions = pd.read_csv('user_impressions.csv')

# Read normalized user impressions
'''
Normalize means calculating the percentage of of the impressions in each channel for each individual user since we are
interested in the impression composition rather than the absolute impression number.
Note: the normalizing was done by using execl so we can make code clearer.
'''
user_impressions_normalized = pd.read_csv('user_impressions_normalized.csv')

'''
Since k-means is a unsupervised clustering method, we don't know what is the optimal clustering number. There are total
14 different channels and we assume users will be clustered by there 'interests', so we can iterate the k from 2 to 14.
To make sure we really get the optimal clusters we will iterate k from 2 to 40
'''

# Initial the silhouette score list, set it to 0 for k = 0 and 1
slt_score_list = [0, 0]

# Note: it takes about 4 hours to finish the following for-loop on my i7 3.5G computer and uses about 8.5 GB RAM
for k in range(2, 40):
    # Get the numerical columns
    features = list(user_impressions_normalized.describe().columns)
    cls = cluster.k_means(user_impressions_normalized[features].values, k)
    slt_score = silhouette_score(user_impressions_normalized[features].values, cls[1])
    print slt_score
    # Print the number of users in each group
    for i in range(k):
        print (cls[1] == i).sum()
    # Append the silhouette score of k in the list
    slt_score_list.append(slt_score)

# Draw the silhouette score graph
plt.plot(slt_score_list, marker='o')
plt.axis([0, 42, 0, 1])
plt.show()

'''
By observe the silhouette score graph you will find that the silhouette score is the highest when k is 11, which means
we should set k to 11 to cluster the users.
Note: some times the silhouette score is the highest when k is 9. I have run it for several times and on average it
gives the highest score when k is 11
'''

# Cluster users using k = 11
features = list(user_impressions_normalized.describe().columns)
cls = cluster.k_means(user_impressions_normalized[features].values, 11)
# Assign group ID to users in the un-normalized data frame
user_impressions['group_id'] = cls[1]
features.insert(0, 'UUID')
features.append('group_id')
# Save the data we interested to CSV file
user_impressions[features].to_csv('cluster.csv', index=False)

# I used other tool to group the clustered data into groups and saved into group.csv file
