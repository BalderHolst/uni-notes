# Statistical (Mahalanobis) Distance
A measure of "how rare" a sample is.

Distance from a sample to $\mu$, taking the distribution into account. Samples more standard deviations away form $\mu$, will have a hight statistical distance, even if the euclidian distance is the samme.

Squared statistical distance:
$$
X \sim \mathcal{N}_{p}(\mu,\Sigma) \quad\Rightarrow\quad d_{M}^{2}(x, \mu) := (x-\mu)^{T} \Sigma^{-1}(x_{\mu)} \sim \mathcal{X}^{2}(p)
$$

### Model Check

> [!tip] Any Dimension!
> This works in *any number of dimensions*!!

A model can be checked by making sure the statistical distance of a dataset follows the $\mathcal{X}^2(p)$ distibution.

We can use a qq-plot to compare a sampled distribution to the $\mathcal{X}^{2}(p)$ distribution.

### Confidence Regions

> [!warning] What?
> *Always* say for **what** the confidence region is for.

$\alpha$: What fraction of the data is included in the region.

To calculate where to make the "cut" on a MVN, calculate $\mathcal{X}^{2}(p)_{\alpha}$:

$$
\mathcal{X}^{2}(p)_{\alpha} = \mathrm{chi2inv}(1-\alpha, p)
$$

### Outlier Detection



---
#multivariate-statistics 