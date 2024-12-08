# Wald Test
Test how extreme a sample is

$$
t_{W} = \frac{(\hat{\theta} - \theta_{0})^{2}}{\mathcal{I}(\theta_{0})^{-1}} \sim \mathcal{X}^{2}(1) \quad\Leftrightarrow\quad s_{W} = \frac{\hat{\sigma} - \sigma_{0}}{\sigma^{0}} \sim Z
$$
$\hat{\theta}$: Sample
$\theta_{0}$: Sample mean according to the null hypothesis
$\mathcal{I}(\sigma_{0})$: [[Fisher Information]]
$\mathcal{X}^{2}(1)$: [[X2 Distribution]] with $1$ degree of freedom. This changes with the number of parameters you are testing.
$Z$: [[Z-distribution]]

#### Approximate Wald Test
$$
t_{W} = \frac{(\hat{\theta} - \theta_{0})^{2}}{\mathcal{I}(\hat{\theta})^{-1}} \sim \mathcal{X}^{2}(1)
$$

---

### More Concrete Example
Consider
$$
H_{0}: \; \theta = \theta_{0} \quad\mathrm{versus}\quad H_{1}:\; \theta \neq \theta_{0}
$$
assuming that $\theta_{0}$ is asymptotically normal:
$$
\frac{\widehat{\theta} - \theta }{\widehat{\mathrm{se}}} \rightsquigarrow \mathcal{N}(0, 1)
$$
**TEST**: Reject $H_{0}$ when $|W| > z_{\alpha/2}$ where
$$
W =  \frac{\widehat{\theta} - \theta }{\widehat{\mathrm{se}}}
$$

---
#statistics