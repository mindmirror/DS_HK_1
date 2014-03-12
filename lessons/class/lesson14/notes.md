## Ensemble methods

Ensemble methods are learning algorithms that construct a set of classfiers and then classify new data points by taking a (weighted) vote of their predictions. They are methods of improving classification accuracy by aggregating predictions over several base classifiers. Ensembles are osten much more accurate than the base classifiers that compose them.

In order for an ensemble classifier to outperform a single base classifier (bc), two conditions must be met. The bc’s must be:
1. *accurate*: they must outperform random guessing ~ _low bias_
1. *diverse*: their misclassifications must occur on different training examples ~ _uncorrelated_

Ideally, the base classifiers would also be *unstable* to variations in the training set ~ _high variance_

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/ensemble.png)

## Problems In Classification

In any supervised learning task, our goal is to make predictions of the
true classification function `f` by learning the classifier `h`.
There are three main problems that can prevent this:

#### Statistical problem

If the amount of training data available is small, the base classifier
will have difficulty converging to `h` . An ensemble classifier can mitigate this problem by “averaging out” base classifier predictions to improve convergence.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/statistical.png)

The true function `f` is best approximated as an average of the base classifiers.

#### Computational problem

Even with sufficient training data, it may still be computationally
difficult to find the best classifier h. For example, if our base classifier is a decision tree, an exhaustive search of the hypothesis space of all possible classifiers is extremely complex (NP-complete).

Recall that this is why we used a heuristic algorithm (greedy search).

An ensemble composed of several BC’s with different starting points can provide a better approximation to f than any individual BC.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/computational.png)

The true function `f` is often best approximated by using several starting points to explore the hypothesis space.

#### Representational problem

Sometimes `f` cannot be expressed in terms of our hypothesis at all. To illustrate this, suppose we use a decision tree as our base classifier. A decision tree works by forming a rectilinear partition of the feature space.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/rectilinear.png)

But what if `f` is a diagonal line? Then it cannot be represented by finitely many rectilinear segments, and therefore the true decision boundary cannot be obtained by a decision tree classifier. However, it may be still be possible to approximate f or even to expand the space of representable functions using ensemble methods.

An ensemble of decision trees can approximate a diagonal decision boundary.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/approximation.png)

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/representational.png)

nsemble classifiers can be effective even if the true decision boundary lies outside the hypothesis space.

### Creating an Ensemble Prediction

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson14/approximation.png)

There are several ways to generate base classifiers?
* manipulating the training set
* manipulating the learning algorithm itself
* manipulating the output labels

## Manipulating the training set

These technique works especially well for unstable learning algorithms|algorithms whose output classifier undergoes major changes in response to small changes in the training data. Decision-tree, neural network, and rule learning algorithms are all unstable. Linear regression, nearest neighbor, and linear threshold algorithms are generally very stable.

### Bagging

Bagging (bootstrap aggregating) is a method that involves manipulating the training set by *resampling*. We learn `k` base classifiers on `k` different samples of training data. These samples are independently created by resampling the training data using uniform weights (eg, a *uniform sampling distribution*).

* Each training sample is the same size as the original training set.
* Resampling means that some training records may appear in a sample more than once, or even not at all.

The final prediction is made by taking a majority vote across bc’s.

Bagging reduces the variance in our generalization error by aggregating multiple base classifiers together (provided they satisfy our earlier requirements).

If the base classifier is stable, then the ensemble error is primarily due to bc bias, and bagging may not be effective. Since each sample of training data is equally likely, bagging is not very susceptible to overfitting with noisy data.

## sklearn.ensemble.BaggingClassifier

When random subsets of the dataset are drawn as _random subsets of the samples_, then this algorithm is known as *Pasting*. If samples are _drawn with replacement_, then the method is known as *Bagging*. When random subsets of the dataset are drawn as _random subsets of the features_, then the method is known as *Random Subspaces*. Finally, when base estimators are built on _subsets of both samples and features_, then the method is known as *Random Patches*.

```python
ensemble = BaggingClassifier(base_estimator=DecisionTreeClassifier(),
                                     bootstrap=True,
                                     bootstrap_features=False).fit(X_train, y_train)
```

## Boosting

Boosting is an iterative procedure that adaptively changes the sampling distribution of training records at each iteration. The first iteration uses uniform weights (like bagging). In subsequent iterations, the weights are adjusted to emphasize records that were misclassified in previous iterations. The final prediction is constructed by a weighted vote (where the weights for a bc depends on its training error).

The bc’s focus more and more closely on records that are difficultto classify as the sequence of iterations progresses. Thus the bc’s are faced with progressively more difficult learning problems.

Like in bagging, sampling is done with replacement, and as a result some records may not appear in a given training sample. These omitted records will likely be misclassified, and given greater weight in subsequent iterations once the sampling distribution is updated. So even if a record is lest out at one stage, it will be emphasized later.

Updating the sampling distribution and forming an ensemble prediction leads to a nonlinear combination of the base classifiers. By explicitly trying to optimize the weighted ensemble vote, boosting attacks the representation problem head-on.

## Random Forests

A random forest is an ensemble of decision trees where each base classifier is grown using a random effect. One way to do this is to randomly choose one of the top `k` features to split each node. For a small number of features, we can also create linear combinations of features and select splits from the enhanced feature set (Forest-RC). Or, we can select splitting features completely at random (Forest-RI).

Random forests are about as accurate as AdaBoost, more robust to noise, and can also have better runtime than other ensemble methods (since the feature space is reduced in some cases).

```python
from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

X, y = make_blobs(n_samples=10000, n_features=10, centers=100,
     random_state=0)

## DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=None, min_samples_split=1,
       random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean()

## RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10, max_depth=None,
     min_samples_split=1, random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean()

## ExtraTreesClassifier
clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,
    min_samples_split=1, random_state=0)
scores = cross_val_score(clf, X, y)
scores.mean() > 0.999
```

The main parameters to adjust when using these methods is `n_estimators` and `max_features`. The former is the number of trees in the forest. The larger the better, but also the longer it will take to compute. The latter is the size of the random subsets of features to consider when splitting a node. The lower the greater the reduction of variance, but also the greater the increase in bias. Empirical good default values are `max_features=n_features` for regression problems, and `max_features=sqrt(n_features)` for classification tasks (where `n_features` is the number of features in the data). The best results are also usually reached when setting `max_depth=None` in combination with `min_samples_split=1` (i.e., when fully developing the trees).

### Example Use Cases

* Wisdom of Crowds
* IBM’s WATSON
* Nate Silver’s election models
* Kaggle competitions


## Resources
- [Random Forests in Python](http://blog.yhathq.com/posts/random-forests-in-python.html)
- [Random Forests for Kaggle](http://www.kaggle.com/c/titanic-gettingStarted/details/getting-started-with-random-forests)
- [Random Forests and Performance Metrics](http://citizennet.com/blog/2012/11/10/random-forests-ensembles-and-performance-metrics/)

## Academic
* [Ensemble Methods in Machine Learning](http://www.ensemblemethods.com/documents/EnsembleMethodsInMachineLearning.pdf)

## Modules
* [sklearn.ensemble.BaggingClassifier](http://scikit-learn.org/dev/modules/generated/sklearn.ensemble.BaggingClassifier.html)
