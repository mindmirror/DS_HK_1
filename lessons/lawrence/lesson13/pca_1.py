from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets, feature_selection
from sklearn.decomposition import PCA

# Load iris data
iris = datasets.load_iris()
iris_data = iris.data[:, :4]
iris_data_transposed = iris_data.T
row_means = [np.mean(i) for i in iris_data_transposed]
iris_data_transposed_scaled = np.array([iris_data_transposed[i] - row_means[i] for i in range(4)])

# Build PCA model
pca = PCA()
pca.fit(iris_data_transposed_scaled)
variance = pca.explained_variance_ratio_
print variance
readable_variance = variance * (1/variance[0])
print readable_variance
plt.plot(range(4), readable_variance)
plt.show()

