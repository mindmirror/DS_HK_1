# Support Vector Machines

## Discriminative & Generative Algorithm

### Generative: P(D|C), P(C)
Deeper understanding: modeling classes. Can generate data.

![generative](http://i.stack.imgur.com/27V7I.gif)

Which is the equation you use in generative models. It has the joint probability distribution p(x, y), since p(x, y) = p(x | y) p(y), which explici tly models the actual distribution of each class. With the joint probability distribution function, given an y, you can calculate ("generate") its respective x. For this reason they are called generative models.

A generative model learns the joint probability distribution p(x,y) and a discriminative model learns the conditional probability distribution p(y|x)

### Discriminative: P(C|D)
Pragmatic: focuses on distinguishing. Can only classify

![disc](http://i.stack.imgur.com/loiUt.gif)

Which merely chooses what is the most likely class considering x. Here we have the conditional probability distribution p(y|x), which modeled the boundary between classes,

Here's a really simple example. Suppose you have the following data in the form (x,y):

    (1,0), (1,0), (2,0), (2, 1)

p(x,y) is

          y=0   y=1
         -----------
    x=1 | 1/2   0
    x=2 | 1/4   1/4

p(y|x) is

          y=0   y=1
         -----------
    x=1 | 1     0
    x=2 | 1/2   1/2

#### Classifying Methods

* Logistic Regression: Discriminative
* KNN: Generative
* Naíve Bayes: Generative
* Decision Trees: Discriminative
* SVM, a non-probabilistic maximal margin classifier ?

### Journal Articles
* [On Discriminative vs. Generative classifiers: A comparison of logistic regression and naive Bayes](http://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf)
* [Learning Generative Models via Discriminative Approaches](http://pages.ucsd.edu/~ztu/publication/cvpr07_gdl.pdf)
* [Discriminative Learning can Succeed where Generative Learning Fails](http://www.cs.columbia.edu/~rocco/Public/ipl_lss.pdf)
* [Generative or Discriminative? Getting the Best of Both Worlds](http://research.microsoft.com/en-us/um/people/cmbishop/downloads/bishop-valencia-07.pdf)
* [Discriminative, Generative and Imitative Learning (PhD Thesis)](http://www.cs.columbia.edu/~jebara/papers/jebara4.pdf)
* [Generative vs. discriminative](http://stats.stackexchange.com/questions/12421/generative-vs-discriminative)

### Video Lecture
[](http://openclassroom.stanford.edu/MainFolder/VideoPage.php?course=MachineLearning&video=06.1-NaiveBayes-GenerativeLearningAlgorithms&speed=100)

## SUPPORT VECTOR MACHINES

A binary linear classifier whose decision boundary is explicitly constructed to minimize generalization error.

* binary classifier – solves two-class problem
* linear classifier – creates linear decision boundary (in 2d)

The decision boundary derived using geometric reasoning.
In 2 dimensions, the separator is a line:

![y = ax + b => w_{1}x_{1} + w_{2}x_{2} + w_0 = 0](http://www.sciweavers.org/tex2img.php?eq=y%20%3D%20ax%20%2B%20b%20%3D%3E%20w_%7B1%7Dx_%7B1%7D%20%2B%20w_%7B2%7Dx_%7B2%7D%20%2B%20w_0%20%3D%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

In 3 dimensions, it’s a 2D plane:

![w_{1}x_{1} + w_{2}x_{2} + w_{3}x_{3} + w_0 = 0](http://www.sciweavers.org/tex2img.php?eq=w_%7B1%7Dx_%7B1%7D%20%2B%20w_%7B2%7Dx_%7B2%7D%20%2B%20w_%7B3%7Dx_%7B3%7D%20%2B%20w_0%20%3D%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

The generalization error is equated with the geometric concept of margin, which is the region along the decision boundary that is free of data points.

Margins provide the largest impact: even moving one point along the margin can completely change the decision boundary!

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/svm.png)

The goal of an SVM is to create the linear decision boundary with the largest margin. This is commonly called the maximum marginhyperplane.

Hyperplane: is just a high-dimensional generalization of a line.


## MAXIMUM MARGIN HYPERPLANES

Decision boundary (mmh) derived by the discriminant function.

![f(x) = w^{T}x+b](http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20w%5E%7BT%7Dx%2Bb&bc=White&fc=Black&im=jpg&fs=12&ff=arev)

such that w is the weight vector and b is the bias.

The weight vector determines the orientation of the decision boundary. The bias determines its translation from the origin.

![Hard Boundaries](http://i.stack.imgur.com/qt3CZ.png)
_Hard Boundaries_

The sign of f(x) determines the (binary) class label of a record x .

As we said before, SVM solves for the decision boundary that minimizes generalization error, or equivalently, that has the maximum margin.

These are the same things, because using the mmh as the decision boundary minimizes the probability that a small perturbation in the position of a point produces a classification error.

Intuitively, the wider the margin, the clearer the distinction between classes.

Selecting the mmh is a straightforward exercise in analytic geometry (we won’t go through the details here). In particular, this task reduces to the optimization of a convex objective function.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/ConvexFunction.svg/1000px-ConvexFunction.svg.png)

The black curve f(x) is a convex function of x.

This is nice because convex optimization problems are guaranteed to give global optima (and they’re easy to solve numerically too).

Notice that the margin depends only on a subset of the training data; namely, those points that are nearest to the decision boundary. These points are called the *support vectors*. The other points (far from the decision boundary) don’t affect the construction of the mmh at all!

### Decision boundaries

All of the decision boundaries we’ve seen so far have split the data perfectly; eg, the data are linearly separable, and therefore the training error is 0. We are always solving for one optimum (global, instead of the local optimum). If our data (like in previous examples) is linearly separable, the training error is 0. The optimization problem that this SVM solves is:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/hard-margin-optimisation.png)

This type of optimization problem is called a quadratic program. The result of this qp is the hard margin classifier we’ve been discussing.

## SLACK VARIABLES

Recall that in building the hard margin classifier, we assumed that our data was linearly separable (eg, that we could perfectly classify each record with a linear decision boundary).

Suppose that this was not true, or suppose that we wanted to use a larger margin at the expense of incurring some training error. This can be done using by introducing *slack variables*.

![](http://i.stack.imgur.com/npEOk.png)
_Soft Boundaries_

Slack variables `ξ` generalize the optimization problem to permit some misclassified training records (which come at a cost C ).

The resulting *soft margin classifier* is given by:

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/soft-margin-optimisation.png)

This an example of bias-variance tradeoff.

Translated, this means that sost margins create a “zone” for potential error, allowing the algorithm to potentially pick out “better” support vectors. By removing the *bias* error from the hard margin, we introduce *variance* error (and thus, generalization error) into our model.

![](http://openi.nlm.nih.gov/imgs/512/29/2547983/2547983_pcbi.1000173.g003.png)

The soft-margin optimization problem can be rewritten as the dual formulation of the optimization problem. (reached via Lagrange multipliers)

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/dual-form-soft-margin-optimisation.png)

Often, the optimization of slack variables comes between exponentially growing sequences of *C* (cost)

* Higher values of *C* = higher accuracy in model
* Lower values of *C* = training error and better generalization


## NONLINEAR SVM CLASSIFICATION

Suppose we need a more complex classifier than a linear decision boundary allows. One possibility is to add nonlinear combinations of features to the data, and then to create a linear decision boundary in the enhanced (higher-dimensional) feature space. This linear decision boundary will be mapped to a nonlinear decision boundary in the original feature space.

![hyper](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/hyper-transform.png)

Issues :

* Does not scale well: requires many high-dimensional calculations
* Leads to more complexity (both modeling complexity and computational complexity) than we want.

Let’s hang on to the logic of the previous example, namely:

* remap the feature vectors x_i into a higher-dimensional space K’
* create a linear decision boundary in K’
* back out the nonlinear decision boundary in K from the result

But if we want to save ourselves the trouble of doing a lot of additional
high-dimensional calculations, we only need recall that our optimization problem depends on the features only
through the inner product x^{T}x :

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/dual-form-soft-margin-optimisation.png)

We can replace this inner product with a more general function that has the same type of output as the inner product!

### The Kernel Trick

Nonlinear applications of SVM rely on an implicit (nonlinear) mapping Φ that sends vectors from the original feature space K into a higher-dimensional feature space K’.

Nonlinear classification in K is then obtained by creating a linear decision boundary in K’.

In practice, this involves no computations in the higher dimensional space!

![](http://i.stack.imgur.com/1gvce.png)
_non-linear SVM_

The inner product is an operation that takes two vectors and returns a real number. The fact that we we can rewrite the optimization problem in terms of the inner product means that we don’t actually have to do any calculations in the feature space K . In particular, we can easily change K to be some other space K’.

Formally, we can think of the inner product as a map that sends two vectors in the feature space K into the real line |R.
We can replace this with a generalization of the inner product called a kernel function that maps two vectors in a higher-dimensional feature space K’ into |R. The upshot is that we can use a kernel function to implicitly train our model in a higher-dimensional feature space, without incurring additional computational complexity! As long as the kernel function satisfies certain conditions ([Mercer’s theorem](http://en.wikipedia.org/wiki/Mercer's_theorem)), our conclusions above regarding the mmh continue to hold. In other words, no algorithmic changes are necessary, and all the benefits of a linear SVM are maintained.

Intuitively, the gamma parameter defines how far the influence of a single training example reaches, with low values meaning ‘far’ and high values meaning ‘close’. The C parameter trades off misclassification of training examples against simplicity of the decision surface. A low C makes the decision surface smooth, while a high C aims at classifying all training examples correctly.

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/popular-kernels.png)

![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/polunomials-kernels.png)
![](https://raw.github.com/ga-students/DS_HK_1/gh-pages/lessons/class/lesson11/gausian-kernels.png)

SVMs (and kernel methods in general) are versatile, powerful, and popular techniques that can produce accurate results for a wide array of classification problems. The main disadvantage of SVMs is the lack of intuition they produce. These models are truly black boxes!

## Extra

### Academic
* [Stanford CS229 Lecture notes on SVM](http://cs229.stanford.edu/notes/cs229-notes3.pdf)

### Video
* [Support Vector Machines](http://videolectures.net/mlss06tw_lin_svm/)
* [Deep Support Vector Machines](http://videolectures.net/roks2013_wiering_vector/)

### Packages
* [Support Vector Machines](http://scikit-learn.org/stable/modules/svm.html#svm-kernels)
* [Kernel Functions](http://scikit-learn.org/stable/modules/svm.html#svm-kernels)
* [sklearn.svm.SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [sklearn.svm.LinearSVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html)
* [sklearn.svm.SVR](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html)
* [PyML SVM Howto](http://pyml.sourceforge.net/doc/howto.pdf)


