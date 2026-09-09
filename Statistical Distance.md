# Statistical (Mahalanobis) Distance
A measure of "how rare" a sample is.

Distance from a sample to $\mu$, taking the distribution into account. Samples more standard deviations away form $\mu$, will have a hight statistical distance, even if the euclidian distance is the samme.

Squared statistical distance:
$$
X \sim \mathcal{N}_{p}(\mu,\Sigma) \quad\Rightarrow\quad d_{M}^{2}(x, \mu) := (x-\mu)^{T} \Sigma^{-1}(x_{\mu)} \sim \mathcal{X}^{2}(p)
$$

### Model Check
A model can be checked by making sure the statistical distance of a dataset follows the $\mathcal{X}^2$ distibution.

### Confidence Regions

> [!warning] What?
> *Always* say for **what** the confidence region is for.

$\alpha$: What fraction of the data is included in the region.

$$
\mathcal{X}^{2}(p) = \mathrm{chi2inv}(1-\alpha, p)
$$

### Outlier Detection



---
#multivariate-statistics 