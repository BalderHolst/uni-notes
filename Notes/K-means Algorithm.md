---
created: 2026-11-12
tags:
  - machine-learning
---

# K-means Algorithm

![[Pasted image 20261112130538.png|450]]

1. Assume $k$ amount of clusters/centers and initialize their positions at randomly selected points from the dataset.
2. Assign points to clusters with *squared distance*
3. Calculate new center and *update each cluster position*. Assign again after.


#### Cost Function
Here, we are minimizing *inertia*:
$$
J(c, \mu) = \sum_{i=1}^{k} || x_{i} - \mu_{c} ||^{2}
$$
$i$: Index of the data

Assign cluster belogning for each cluster.
$$
c_{i} \leftarrow \mathrm{argmin}_{k} ||x_{i} - \mu_{k} ||^{2}
$$
$k$: Cluster
$\mu_{k}$: Cluster mean

Update:
$$
\mu_{k} \leftarrow \frac{1}{c_{k}} \sum_{i\in c_{k}} x_{i}
$$

#### Choosing k
- Elbow method
- Silhouette score
$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$
$s(i)$: Silhouette score for point $i$
$a(i)$: Average distance the the other points withing the cluster
$b(i)$: Distance to the center of the neighboring cluster

This can be used to create a $k$ vs. score plot that peaks at the correct $k$.


### Tackling Local Minima

- Run multiple times and pick the one with lowest inertia.
- Use [[K-means++ Algorithm]]