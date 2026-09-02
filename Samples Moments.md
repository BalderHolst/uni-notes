# Samples Moments
We try to estimate the population mean and variance from the sampled population.

See [[Multivariate Data Sets]].

##### Sample Mean
$$
\hat{\mu}_{(p\times 1)} = \frac{1}{n} \sum_{j=1}^{n}x_{j} = \bar{X}
$$
$\bar{X}$: Average Sample
$n$: Number of samples
$p$: Dimensions of each sample
$x_j$: Single sample vector

It is an unbiased estimate:
$$
E[\hat{\mu}] = \mu \Rightarrow \mathrm{unbiased}
$$

##### Sample Covariance Matrix
$$
\hat{\Sigma}_{p\times p} = S_{p\times p} = \frac{1}{n-1} \sum_{j=1}^{n} (x_{j} - \bar{X})(x_{j} - \bar{X})^{T}
$$
Note that we use $\bar{X}$ in place of the true mean $\mu$. Doing this loses us a [[Degrees of Freedom|degree of freedom]], we therefore divide by $n-1$.

##### Generalized Sample Variance
Further simplification of the variance. We simplify the covariance to a single scalar value $|S|$.
$$
|S| = \mathrm{det}(S) = \frac{s_{ij}}{\sqrt{s_{i}^{2}}\sqrt{s_{j}^{2}}}
$$

##### Sample Correlation Matrix
$$
\hat{\rho} = R =
\begin{bmatrix}
1      & r_{12} & \cdots & r_{1p} \\
r_{12} & 1      & \cdots & r_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
r_{1p} & r_{2p} & \cdots & 1
\end{bmatrix}
$$


---
#multivariate-statistics