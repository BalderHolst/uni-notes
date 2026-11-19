---
created: 2026-11-19
tags:
  - machine-learning
---

# Gaussian Mixture Models
A "better" [[K-means Algorithm]] that uses [[Notes/Multivariate Normal Distribution (MVN)||MVN]]s to classify data. This means that it is more robost to clusters of different sizes and "squished" clusters.

$$
p(x) = \sum_{k=1}^{K} \pi_{k}\ \mathcal{N}(x | \mu_{k}, \Sigma_{k})
$$
Respontibilities (belonging)
$$
r_{ik} =
\frac{
\pi_{k}
}{
}
$$


## Procedure
The algorithm is divided into three steps. Steps 2 and 3 are repeated until the log-likelihood

##### 1) Initialize Step
**NOTE**: This is sensitive to the initialization of $\mu_{k}$. Just like in [[K-means Algorithm|K-means]], we either run it multiple times or use the same logic as the [[K-means++ Algorithm]].

$$
\begin{align}
\pi_{k} &= 1 / k \\
\mu_{k} &= \mathrm{random\ datapoints} \\
\Sigma_{k} &= \mathrm{covariance\ of\ the\ dataset}
\end{align}
$$
$k$: Numbe of clusters


##### 2) E - Expectation Step
- Calculate responsibilities $r_{ik}$ for every point.

##### 3) M - Maximization Step

$$
\begin{align}
\pi_{k} &= \frac{N_{k}}{n},\quad N_{k} = \sum_{i=1}^{n}r_{ik} \\
\mu_{k} &= 1 / N_{k} \sum_{i=1}^{n} r_{ik} x_{i} \\
\Sigma_{k} &= 1 / N_{k} \sum_{i=1}^{n} r_{ik}(x_{i} - \mu_{k})(x_{i} - \mu_{k})^{T}
\end{align}
$$
Finally, we calculate log likelihood to check our fit
$$
l = \sum_{i=1}^{n} \log(p(x_{i}))
$$
In reality, this is only calculated for *support vectors*.
