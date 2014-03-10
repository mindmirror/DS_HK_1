# Dimensionality Reduction

Dimensionality Reduction is a set of techniques for reducing the size (in terms of features, records, and/or bytes) of the dataset under examination. In general, the idea is to regard the dataset as a matrix and to decompose the matrix into simpler, meaningful pieces. Dimensionality reduction is frequently performed as a pre-processing
step before another learning algorithm is applied.

The number of features in our dataset can be difficult to manage, or
even misleading (eg, if the relationships are actually simpler than they
appear). For example, suppose we have a dataset with some features that are related to each other. Ideally, we would like to eliminate this redundancy and consolidate the number of variables we’re looking at. If these relationships are linear, then we can use well-established techniques like `PCA/SVD`.

### Consider this

Say we have a large room that contains `m` lights with unique light patterns and `n` cameras recording them. Using what the cameras record, how do we determine how many lights there are in the room?

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/lights.png)

_Setup of two lights and four cameras_

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/lightcapture.png)

_Comparing Data Between Light Capture Cameras_

### Curse of Dimensionality

The complexity that comes with a large number of features is due in part to the curse of dimensionality. Namely, the sample size needed to accurately estimate a random variable taking values in a dimensional feature space grows exponentially with the number of features (almost). (More precisely, the sample size grows exponentially with `l ≤ features`, the dimension of the manifold embedded in the feature space).

Most of the points in the space are “far” from each other. This illustrates the fact that local methods will break down in these
circumstances (eg, in order to collect enough neighbors for a given
point, you need to expand the radius of the neighborhood so far that
locality is not preserved).

The bottom line is that high-dimensional spaces can be problematic.

### Goals of Dimensionality Reduction

We’d like to analyze the data using the most meaningful basis (or
coordinates) possible.

More precisely: given an `n x m` matrix `X` (encoding `n` observations of a `m`-dimensional random variable), we want to find a `k`-dimensional
representation of `X ( k < m )` that (approximately) captures the
information in the original data, according to some criterion.

* reduce computational expense
* reduce susceptibility to overfitting (but regularisation is better)
* reduce noise in the dataset
* _enhance our intuition_

### Approaches to Dimensionality Reduction

There are two approaches: feature selection and feature extraction.

* *feature selection* – selecting a subset of features using an external
criterion (filter) or the learning algo accuracy itself (wrapper)
* *feature extraction* – mapping the features to a lower dimensional
space

#### Feature Selection

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/stewise.png)

_Feature selection: Removing features with highest p-values and then
refitting model (stepwise regression)_

Feature selection is important, but typically when people say
dimensionality reduction, they are referring to feature extraction.

#### Feature Extraction

The goal of feature extraction is to create a new set of coordinates
(often in lower dimension) that simplify the representation of the data.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/featureextraction.png)

### Applications of Dimensionality Reduction
* Topic models (document clustering)
* Image recognition/computer vision
* Bioinformatics (microarray analysis)
* Speech recognition
* Astronomy (spectral data analysis)
* Recommender systems

## Principal Components Analysis (PCA)

Principal component analysis is a dimension reduction technique that
can be used on a matrix of any dimensions. This procedure produces a new basis, each of whose components retain as much variance from the original data as possible. The PCA of a matrix `X` boils down to the eigenvalue decomposition of the covariance matrix of `X`.

The covariance matrix `C` of a matrix `X` is always symmetric:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/covariancematrix.png)

off-diagonal elements `C_{ij}` give the covariance between `X_i , X_j (i ≠ j)` diagonal elements `C_{ii}` give the variance of `X_i`

### EIGENVALUE DECOMPOSITION

The eigenvalue decomposition of a symmetric matrix `X` is given by:

`X = QΛQ^T`

The columns of Q are the eigenvectors of `X`, and the values in `Λ` are the associated eigenvalues of `X`. For an eigenvector `v` of `X` and its eigenvalue `λ`, we have the important relation: `Xv = λv`

The eigenvectors form a basis of the vector space on which `X` acts (eg,
they are orthogonal). Furthermore the basis elements are ordered by their eigenvalues (from largest to smallest), and these eigenvalues represent the amount of variance explained by each basis element.

This can be visualized in a scree plot, which shows the amount of variance explained by each basis vector.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/irisscree.png)

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson13/photodr.png)

_PCA and [image compression](http://glowingpython.blogspot.it/2011/07/pca-and-image-compression-with-numpy.html) with numpy_

## Kernel Methods in Pca

### Review

With support vector machines, we covered three kernels:

* linear: K(x,x’) = ![x^{T}x](http://www.sciweavers.org/tex2img.php?eq=x%5E%7BT%7Dx&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
* polynomial: ![(x^{T}x’ + 1)^{d}](http://www.sciweavers.org/tex2img.php?eq=%28x%5E%7BT%7Dx%E2%80%99%20%2B%201%29%5E%7Bd%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev)
* gaussian (rdf): ![exp(- \gamma ||x - x’||^{2} )](http://www.sciweavers.org/tex2img.php?eq=exp%28-%20%5Cgamma%20%7C%7Cx%20-%20x%E2%80%99%7C%7C%5E%7B2%7D%20%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev)

Likewise, PCA can also use kernels methods to produce new clarity
around the structure of the data. In particular, KPCA is most osten used for image de-noising and pattern recognition (or commonly novelty detection). KPCA is particularly useful for extracting nonlinear features, though like standard PCA, the interpretation is not always straightforward!

![](MLSS-2012-Fukumizu-Kernel-Methods-for-Statistical-Learning_034.png)

## Resources

- [A Tutorial on PCA](http://www.snl.salk.edu/~shlens/pca.pdf)
- [Stanford PCA Tutorial](http://ufldl.stanford.edu/wiki/index.php/PCA)
- [Aaron's PCA/3d/clustering post](http://planspace.org/2013/02/03/pca-3d-visualization-and-clustering-in-r/)

## Tutorial
* [A Tutorial on Principal Component Analysis](http://www.snl.salk.edu/~shlens/pca.pdf)
* [Dimensionality Reduction A Short Tutorial](http://www.math.uwaterloo.ca/~aghodsib/courses/f06stat890/readings/tutorial_stat890.pdf)

### Extra
* [Sample size vs. dimensionality](http://www.cbcb.umd.edu/~salzberg/docs/murthy_thesis/survey/node16.html)

### Academic
* [Dimensionality Reduction Methods](http://www.stat-d.si/mz/mz2.1/dambra.pdf)
* [A survey of dimension reduction techniques](http://www.cc.gatech.edu/~isbell/tutorials/dimred-survey.pdf)

#### Sample Size
* [Sample size determination](http://en.wikipedia.org/wiki/Sample_size_determination)
* [Optimal number of features as a function of sample size for various classiﬁcation rules](http://bioinformatics.oxfordjournals.org/content/21/8/1509.full.pdf+html)
* [Sample size and statistical power considerations in high-dimensionality data settings: a comparative study of classification algorithms](http://link.springer.com/content/pdf/10.1186%2F1471-2105-11-447.pdf)
* [Some considerations of classification for high dimension low-sample size data](http://smm.sagepub.com/content/early/2011/11/22/0962280211428387.abstract)
