---
created: 2026-11-25
tags:
  - multivariate-statistics
---

# Hierarchical Clustering
We create a distance matric that contains the distance between all points
$$
D_{n} =
\begin{bmatrix}
0 & d_{12} & d_{13} & \cdots & d_{1n} \\
d_{12} & 0 & d_{13} & \cdots & d_{2n} \\
d_{13} & d_{23} & 0 & \cdots & d_{3n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
d_{1n} & d_{2n} & d_{3n} & \cdots & 0 \\
\end{bmatrix}
$$

This algorithm is *heavy*
$$
O(n^{3})
$$

### Steps
1. Find smallest entry
2. Combine these into a cluster, and create new entries into the $D$ matrix that corresponts to the *cluster*. Distances from and to this entry, uses a [[Linkage Method]] to calculate distances to other clusters.
3. Back to first step until we only have the amount of desired clusters.


$D_1$: Is one cluster with all observations.

This can be visualized in a dendrogram:

![[Pasted image 20261125125023.png]]


