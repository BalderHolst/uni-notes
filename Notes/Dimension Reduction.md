---
created: 2026-11-04
tags:
  - statistics
---

# Dimension Reduction
We want to compress statistical data $X$ to have less dimensions.

We use the sample covariance in place of the real covariance
$$
\hat{\Sigma} = S = \frac{1}{n-1}\sum_{j=1}^{n}(X_{j} - \bar{X})(X_{j} - \bar{X})^{T}
$$
We to [[Eigendecomposition|eigen value decomposition]] on $S$ as in [[Principal Component Analysis|PCA]].
$$
S = \sum_{i=1}^{p} \hat{\lambda}_{i} \hat{e}_{i} \hat{e}_{i}^{T}
$$
### Truncation
We only keep some $PS$s ([[Principal Component Analysis|principal components]]).
$$
\mathrm{keep}\ \set{ \mathrm{PC}_{1}, \mathrm{PC}_{2}, \dots \mathrm{PC}_{r}}
$$
$r$: Number of components to keep

##### How to choose r
1. Using "Variance explained"
$$
\frac{\sum_{i=1}^{r} \hat{\lambda}_{i}}{\sum_{i=1}^{p} \hat{\lambda}_{i}} \sim 80\%\ \mathrm{to}\ 90\%
$$
2. Pareto Plot
![[Pasted image 20261104133329.png|300]]

3. Above average
$$
\mathrm{keep\ if}\ \hat{\lambda}_{i} \geq \bar{\lambda}
$$

### Interpretation of PCs
Use PCA *loadings*.
