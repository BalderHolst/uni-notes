---
created: 2026-11-25
tags:
  - "#multivariate-statistics"
slides:
  - "[[Lecture Material/Semester 7/statistics/Clustering algorithms.pdf]]"
---

# Clustering
Split an unlabeled dataset into $k$ disjoint clusters based on some "distance" between observations.

- [[Hierarchical Clustering]]

#### Standarize Data
We use the z-score standardization
$$
x_{ji} \to z_{ji} = \frac{
x_{ji} - \bar{x}_{i}
}{
\sqrt{S_{i}^{2}}
}
$$
#### Distance Metric
Grouping is based on a distance metric. This can be any distance metric.

$$
d(x,y)
$$
Here, we *cannot* use the [[Statistical Distance (Mahalanobis)]] as it requires a covariance matrix. We don't have that information only the overall covariance matrix could be calculated, but it does not represent our data well.

##### m-norm distance
This is one distance function we could use
$$
d(x,y) = \left[ \sum_{i=1}^{p} |x_{i} - y_{i}|^{m} \right]^{1 / m}
$$
$m = 2$: Euclidian distance
$m = 1$: Manhatten distance

#### Linkage Method
Distance between clusters. Here are multiple definitions.