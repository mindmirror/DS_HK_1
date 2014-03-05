# K-means clustering

## Unsupervised Learning

#### Useful for

* Market Segmentation
* Social Network Analysis
* Organising Computing Clusters
* Astronomical Data Analysis

## Cluster Analysis

A cluster is a group of _similar_ data points, hence the concept of similarity is central to the definition of a cluster, and therefore to cluster analysis. Cluster analysis enhances our understanding of a dataset by dividing the data into
groups. It provides a layer of abstraction from individual data points. The goal is to extract and enhance the natural structure of the data (not to impose arbitrary structure!)

### Approach

Think of a cluster as a “potential class”; then the solution to a clustering problem is to programatically determine these classes. The real purpose of clustering is data exploration, so a solution is anything that contributes to your understanding.

## K-means clustering

A greedy learner that partitions a data set into k clusters.

* *greedy* – captures local structure (depends on initial conditions)
* *partition* – performs complete clustering (each point belongs to
exactly one cluster)

### Partitions

Each point is assigned to the cluster with the nearest centroid.

*centroid* – the mean of the data points in a cluster
  -> requires continuous (vector-like) features, though see [TopSig](http://eprints.qut.edu.au/43451/) for a binary implementation
  -> highlights iterative nature of algorithm

![](http://blog.alexbeutel.com/voronoi/v4.png)

[D3 Implementation of Voronoi tessellation](http://bl.ocks.org/mbostock/4060366)

These partitions are sometimes called _Voronoi cells_, and these maps _Voronoi diagrams_.

![](http://scikit-learn.org/stable/_images/plot_kmeans_digits_1.png)

One important point to keep in mind is that partitions are not scale-invariant! This means that the same data can yield very different clustering results depending on the scale and the units used. Therefore it’s important to think about your data representation before applying a clustering algorithm.

These graphs show two different representations of the same data:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/scale.png)


### The Basic K-means algorithm

1. Choose K initial centroids (note that K is an input)
2. For each point:
  * Find distance to each centroid
  * Assign point to nearest centroid
3. Recalculate centroid positions
4. Repeat steps 2-3 until stopping criteria met

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/kmeans.png)

[Interactive Example](http://www.math.le.ac.uk/people/ag153/homepage/KmeansKmedoids/Kmeans_Kmedoids.html)


### Properties

* K-means is algorithmically pretty efficient (time & space complexity is linear in number of records).
* It has a hard time dealing with non-[convex clusters](http://pafnuty.wordpress.com/2013/08/14/non-convex-sets-with-k-means-and-hierarchical-clustering/), or data with widely varying shapes and densities.
* Clustering binary data with K-Means [(should be avoided)](http://www-01.ibm.com/support/docview.wss?uid=swg21477401)
* Difficulties can sometimes be overcome by increasing the value of k and combining subclusters in a post-processing step.

![](https://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/images/intclusoutnonfastclus.png)

### STEP 1 – CHOOSING INITIAL CENTROIDS

How do you choose the initial centroid positions?
* Randomly (but may yield divergent behavior)
![](http://upload.wikimedia.org/wikipedia/commons/7/7c/K-means_convergence_to_a_local_minimum.png)
* Perform alternative clustering task, use resulting centroids as initial k-means centroids
* Start with global centroid, choose point at max distance, repeat (but might select outlier)

### STEP 2 – SIMILARITY MEASURES

How do you determine which centroid is the nearest?
* The “nearness” criterion is determined by the similarity/distance measure we discussed earlier. This measure makes quantitative inference possible. (Technically, by defining a similarity measure we are mapping our observations into a metric space.)
* A similarity measure must satisfy certain general conditions:
  ![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/similarity.png)

* There are a number of different similarity measures to choose from, and in general the right choice depends on the problem.
  * For data that takes values in *|R*^n , the typical choice is the [Euclidean distance](http://en.wikipedia.org/wiki/Euclidean_distance):
  ![](http://upload.wikimedia.org/math/3/e/3/3e31af0e62dd2780540f796b51a0ce4e.png)
* We can express different semantics about our data through the choice of metric. Ex: One popular metric for text mining problems (or any problem with sparse binary data) is the [Jaccard Coefficient](http://matpalm.com/resemblance/jaccard_coeff/)].
  ![](http://upload.wikimedia.org/math/1/8/6/186c7f4e83da32e889d606140fae25a0.png)
  * Applying this metric to a problem expresses the sparse nature of the data, and makes a variety of text mining techniques accessible.

The matrix whose entries D_{ij} contain the values d(x, y) for all x and y is called the distance matrix. The distance matrix contains all of the information we know about the dataset. For this reason, it’s really the choice of metric that determines the definition of a cluster.

### STEP 3 – OBJECTIVE FUNCTION

We need to recompute the positions of the centroids at each iteration of the algorithm. We do so by optimizing an objective function that tells us how “good” the clustering is. The iterative part of the algorithm (recomputing centroids and reassigning points to clusters) explicitly tries to minimize this objective function.

Ex: Using the Euclidean distance measure, one typical objective function is the sum of squared errors from each point x to its centroid c i :

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/sse.png)

Given two clusterings, we will prefer the one with the lower SSE since this means the centroids have converged to better locations (a better local optimum).

### STEP 4 – CONVERGENCE

We iterate until some stopping criteria are met; in general, suitable convergence is achieved in a small number of steps. Stopping criteria can be based on the centroids (eg, if positions change by no more than e) or on the points (eg, if no more than x% change clusters between iterations). Recall that, in general, different runs of the algorithm will converge to different local optima (centroid configurations).

## Cluster Validation

In general, k-means will converge to a solution and return a partition of k clusters, even if no natural clusters exist in the data. We will look at two validation metrics useful for partitional clustering, *cohesion* and *separation*.

### Cohesion and separation.

*Cohesion* measures clustering effectiveness within a cluster.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/cohesion.png)

*Separation* measures clustering effectiveness between clusters.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/separation.png)

We can turn these values into overall measures of clustering validity by taking a weighted sum over clusters:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/separationcohesion.png)

Here V can be cohesion, separation, or some function of both. The weights can all be set to 1 (best for k-means), or proportional to the cluster masses (the number of points they contain).

Cluster validation measures can be used to identify clusters that should be split or merged, or to identify individual points with disproportionate effect on the overall clustering.

### Silhouette Coefficient

One useful measure than combines the ideas of cohesion and separation is the [silhouette coefficient](http://pafnuty.wordpress.com/2013/02/04/interpretation-of-silhouette-plots-clustering/). For an individual point x_i , this is given by:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/silhouette.png)

The silhouette coefficient can take values between -1 and 1. In general, we want separation to be high and cohesion to be low. This corresponds to a value of SC close to +1. A negative silhouette coefficient means the cluster radius is larger than the space between clusters, and thus clusters overlap.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/silhouettegraph.png)

The silhouette coefficient for the cluster C_i is given by the average silhouette coefficient across all points in C_i :

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/silhouettegraphcluster.png)

The overall silhouette coefficient is given by the average silhouette coefficient across all points:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/silhouettegraphclustertotal.png)

### Similarity Matrix

An alternative validation scheme is given by comparing the similarity matrix with an idealized (0/1) similarity matrix that represents the same clustering configuration. This can be done either graphically or using correlations.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/similaritymatrix.png)

One useful application of cluster validation is to determine the best number of clusters for your dataset. We can do this by computing the overall SSE or SC for different values of K.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson12/silhouette.png)

To determine your level of confidence in these validation metrics, we use rely on our statistical methods, eg, by computing frequency distributions for these metrics (over several runs of the algorithm) and determining statistical significance.

Ultimately, cluster validation and clustering in general are suggestive techniques that rely on human interpretation to be meaningful.

## Resources

### Academic
* [An implementation of the relational k-means algorithm](http://arxiv.org/abs/1304.6899)

### Packages
* [SciKit Clusting](http://scikit-learn.org/stable/modules/clustering.html)
* [sklearn.cluster.KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

### Examples
* [Blogpost on Insult Detection](http://blog.kaggle.com/2012/09/26/impermium-andreas-blog/)
* [Github Code of Insult Detection Solution](https://github.com/amueller/kaggle_insults/)
* [Choosing a ML Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/)
* [KMeans IPython Notebook](http://nbviewer.ipython.org/urls/raw.github.com/temporaer/tutorial_ml_gkbionics/master/2%2520-%2520KMeans.ipynb)
* [Cloudera ML KMeans](http://blog.cloudera.com/blog/2013/03/cloudera_ml_data_science_tools/)

