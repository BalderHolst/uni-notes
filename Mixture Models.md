# Mixture Models
Distributions that can be modelled as a mix of other distributions. See [[lecture14.pdf#page=7|slides]].
$$
P(\mathbf{x}) = \sum_{i=1}^{k} \;
\underbrace{P(C=i)}_{\mathrm{Mixture\ Weight}} \;
\underbrace{P(\mathbf{x}|C=i)}_{\mathrm{Distribution}}
$$
$C$: Component

Gausian Mixture Model (GMM)
$$
P(\mathbf{x}) = \sum_{i=1}^{k} P(C=i)\ \mathcal{N}(\mathbf{x}|\mu_{i}, \mathbf{\Sigma}_{i})
$$

**Likelihood**
$$
P(x_{1}, \dots, x_{N}| \theta) = \prod_{n=1}^{N} \left(
\sum_{i=1}^{K} P(C_{n}^{i} = 1 | \pi) P(x_{n} | C_{n}^{i} = 1, \theta_{i})
\right)
$$

**Log-likelihood**
$$
\mathcal{L}(\theta| x_{1}, \dots, x_{N}) = \sum_{n=1}^{N} \log \left\{
\sum_{i=1}^{K} \;\underbrace{P(C_{n}^{i} = 1 | \pi)}_\mathrm{Mixture\; Weights} \; P(x_{n} | C_{n}^{i} = 1, \theta_{i})
\right\}
$$
$\theta_{i}$: The parameters for the distribution. That is $\theta_{i} = (\mu_{i}, \sigma_{i}^2)$ for a Gausian.
$\pi$: Mixture model proportions


---
#intelligent-systems