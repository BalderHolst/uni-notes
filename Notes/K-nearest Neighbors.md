---
created: 2026-10-08
tags:
  - machine-learning
links:
  - https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/
---
# K-nearest Neighbors
 
To classify a point, find the $K$ nearest neighbors, the class of the point, is the class of the magority of its neighbors. In case of ties, choose randomly.

No training required!

![[Pasted image 20261008123400.png]]

A larger $K$ *smooths* out the seperation line.

Features are $\set{x_{1}, x_{2}, \dots}$.

### Euclidian Distance
$$
d = \sqrt{\Delta x_{1}^{2} + \Delta x_{2}^{2}}
$$
**PROBLEM**: If parameters are not on the same scale, the parameter with smaller spread, will be percived as smaller using euclidian distance.

#### Z-score Standardization
We normalize the parameters using their standard deviation.

$$
\begin{align}
x_{1}' = \frac{x_{1} - \mu_{1}}{\delta_{1}} \\
x_{2}' = \frac{x_{2} - \mu_{2}}{\delta_{2}}
\end{align}
$$

Mean and standard deviation should **only be calculated on the *training data***.

### Minkovski Family

##### Manhatten (City Block) Distance
$p=1$
$$
d = |\Delta x_{1} | + | \Delta x_{2} |
$$

##### Euclidian Distance
$p=2$
$$
d = \sqrt{\Delta x_{1}^{2} +  \Delta x_{2}^{2}}
$$

##### Chebyshev
$p=\infty$
$$
d = \underset{i=1}{\overset{u}{\mathrm{max}}} | \Delta x_{i} |
$$


##### Mahalanobis Distance
No standardization needed!

See [[Statistical Distance (Mahalanobis)|note]].

$$
d = \sqrt{\Delta x^{T} C^{-1} \Delta x}
$$
##### Others
- Cosine
- Hamming
- Jaccared
- Gower