# Wald Test
Test how extreme a sample is

$$
t_{W} = \frac{(\hat{\theta} - \theta_{0})^{2}}{\mathcal{I}(\theta_{0})^{-1}} \sim \mathcal{X}^{2}(1)
$$
$\hat{\theta}$: Sample
$\theta_{0}$: Sample mean according to the null hypothesis
$\mathcal{I}(\sigma_{0})$: Information matrix
$\mathcal{X}^{2}(1)$: [[X2 Distribution]] with $1$ degree of freedom. This changes with the number of parameters you are testing.

#### Approximate Wald Test
$$
t_{W} = \frac{(\hat{\theta} - \theta_{0})^{2}}{\mathcal{I}(\hat{\theta})^{-1}} \sim \mathcal{X}^{2}(1)
$$


---
#statistics