# Decision Trees

## Characteristics

* Non-parametric: no parameters, no distribution assumptions
* Hierarchical: consists of a sequence of questions which yield a class label when applied to any record
* Variable Size: Any boolean functions can be represented
* Deterministic: For the same set of features the tree will assign the same label
* Discrete and Continuous Parameters:
  * Binning and Threshold

## Node

A decision tree represented using a configuration of nodes and edges. More concretely, as a multiway tree, which is a type of (directed
acyclic) graph. In a decision tree, the nodes represent questions (test conditions) and the edges are the answers to these questions.

* *Root*
* *Leaf*
* *Edge*

## Representation

![Hypertriangles](http://artnectar.com/wp-content/uploads/HLIC/2a198afc1ee92002b5fee8534a68c6d7.jpg)

* Can you learn a frontier between continous variables?
  * Axis-parallel frontiers
  * Sparse matrices

![Decision Boundaries](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F937fb312-ff72-457e-8eb0-df2ad5564074.wmv%2Fslide_0031_full.jpg)

* Can you learn a boolean function?
  * Truth tables

![Booleans](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F937fb312-ff72-457e-8eb0-df2ad5564074.wmv%2Fslide_0046_full.jpg)

## Growing Decision Trees

Hunt’s is a greedy recursive algorithm that leads to a local optimum. It builds a decision tree by recursively partitioning
records into smaller & smaller subsets.

* greedy – algorithm makes locally optimal decision at each step
* recursive – splits task into subtasks, solves each the same way
* local optimum – solution for a given neighborhood of points

The partitioning decision is made at each node according to a metric
called purity. A partition is 100% pure when all of its records belong to a single
class. Let Dt be the set of training records that reach a node t. The general recursive procedure is defined as below:

* If Dt contains records that belong the same class yt, then t is a leaf node labeled as yt
* If Dt is an empty set, then t is a leaf node labeled by the default class, yd
* If Dt contains records that belong to more than one class, use an attribute test to split the data into smaller subsets.

It recursively applies the procedure to each subset until all the records in the subset belong to the same class. The Hunt's algirithm assumes that each combination of attribute sets has a unique class label during the procedure. If all the records associated with Dt have identical attribute values except for the class label, then it is not possible to split these records any future. In this case, the node is decalred a leaf node with the same class label as the majority class of training records associated with this node.

## Partitions

* *Binary attributes* : leads to two-way split test condition.
* *Nominal attributes* : the test condition can be expressed into multiway split on each distinct values, or two-way split by grouping the attribute values into two subsets.
* *Ordinal attributes* : can also produce binary or multiway splits as long as the grouing does not violate the order property of the attribute values.
* *Continuous attributes* : The test condition can be expressed as a comparsion test with two outcomes, or a range query. Or we can discretize the continous value into nominal attribute and then perform two-way or multi-way split.

## Optimization functions

[Objective Fuction](https://www.courses.psu.edu/for/for466w_mem14/Ch11/HTML/Sec1/ch11sec1_ObjFn.htm)

![](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0140_full.jpg)

* Misclassification Error: Accuracy & Error Rate

![](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0003_full.jpg)

![Why it may not always work](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0020_full.jpg)

* Information Gain : Gini Index & Entropy

]([https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0040_full.jpg)

![](https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0056_full.jpg)

![Mutual Information & Information Gain]https://d396qusza40orc.cloudfront.net/machlearning/slides%2F176b8e40-9645-4def-adab-15bdc7d8737b.wmv%2Fslide_0102_full.jpg
_Mutual Information & Information Gain_


## Dealing with missing values

* Imputing during training
  * Most frequent one in the dataset
  * Most frequent in its class
  * Fractional Examples, proportional to the real distirbution

* Imputing during testing
  * Voting by fractional leafs

 ![Unknown Attributes](https://d396qusza40orc.cloudfront.net/machlearning/slides%2Fec7e512b-a28b-4e44-96fa-9c4cb9b98f78.wmv%2Fslide_0002_full.jpg)

### Tree algorithms: ID3, C4.5, C5.0 and CART

What are all the various decision tree algorithms and how do they differ from each other? Scikit-learn uses an optimised version of the CART algorithm.

* ID3 (Iterative Dichotomiser 3) was developed in 1986 by Ross Quinlan. The algorithm creates a multiway tree, finding for each node (i.e. in a greedy manner) the categorical feature that will yield the largest information gain for categorical targets. Trees are grown to their maximum size and then a pruning step is usually applied to improve the ability of the tree to generalise to unseen data.

* C4.5 is the successor to ID3 and removed the restriction that features must be categorical by dynamically defining a discrete attribute (based on numerical variables) that partitions the continuous attribute value into a discrete set of intervals. C4.5 converts the trained trees (i.e. the output of the ID3 algorithm) into sets of if-then rules. These accuracy of each rule is then evaluated to determine the order in which they should be applied. Pruning is done by removing a rule’s precondition if the accuracy of the rule improves without it.

* C5.0 is Quinlan’s latest version release under a proprietary license. It uses less memory and builds smaller rulesets than C4.5 while being more accurate.

* CART (Classification and Regression Trees) is very similar to C4.5, but it differs in that it supports numerical target variables (regression) and does not compute rule sets. CART constructs binary trees using the feature and threshold that yield the largest information gain at each node.

## Pruning

![overfitting](http://www.eecs.wsu.edu/~cook/dm/lectures/l4/img27.gif)
_overfitting_

After building the decision tree, a tree-prunning step can be performed to reduce the size of decision tree. Decision trees that are too large are susceptible to a phenomenon known as overfitting. Pruning helps by trimming the branches of the initail tree in a way that improves the generalization capability of the decision tree.

Pruning involves checking pairs of nodes that have a common parent to see if merging them would increase the entropy by less than a specified threshold. If so, the leaves are merged into a single node with all the possible outcomes. This helps avoid overfitting and stops the tree from making predictions that are more confident than what can really be gleaned from the data.

* Pre-pruning, significance testing
* Penalise complexity to performance measure
* Post-pruning, effective but expensive. For small data-sets it takes away too many records from training, in big data sets it becomes exponentially expensive.

![Reduced Error Pruning](https://d396qusza40orc.cloudfront.net/machlearning/slides%2Ffc1fbb75-aa9e-4de6-8d28-10ff4fb47aca.wmv%2Fslide_0046_full.jpg)
## Confusion Matrices

## Precision and Recall

![](http://uberpython.wordpress.com/2012/01/01/precision-recall-sensitivity-and-specificity/)

## Extra Reading
* [Basic Evaluation Measures for Classifier Performance](http://webdocs.cs.ualberta.ca/~eisner/measures.html)

## Examples

[Multivariate_Analysis](http://nbviewer.ipython.org/github/piti118/babar_python_tutorial/blob/master/notebooks/03_Multivariate_Analysis.ipynb)
