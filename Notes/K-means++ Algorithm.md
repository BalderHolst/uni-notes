---
created: 2026-11-12
tags:
  - machine-learning
---

# K-means++ Algorithm

Same as [[K-means Algorithm]], but we add an iterative process for choosing $k$. 

##### 1. Initialize
Randomly initialize the first cluster
Calculate the squared distance to all points from the cluster

When initiailizing new clusters, the distance to previous cluster are used as weights, so that points further away from initialized clusters are weighted higher.
$$
w_{i} = \frac{1}{||c - x_{i}||^{2}}
$$
$w_{i}$: Weight of point $i$
$c$: Center of the closed cluster center
$x_{i}$: Position of point $i$

##### 2. Run K-means
Run the usual [[K-means Algorithm]].



