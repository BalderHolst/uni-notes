# Delta Method
Given a sequence of [[Random Variables]] $X_{1}, X_{2}, \dots, X_{n}$. If a function $g$ can be defined, the distribution converges as follows.

$$
\sqrt{n}(g(x_{n}) -g(\mu)) \;\xrightarrow{d}\; \mathcal{N}(0, ( (g'(\mu))^{2} \cdot \sigma^{2}))
$$

### Examples

##### Problem 1.
What is the asymptotic limit of $\sqrt{n}(\bar{X}_{n}^{2} - \mu^{2})$?

Here we can now look for the $g$ function
$$
\sqrt{n}(\bar{X}_{n}^{2} - \underbracket{\mu^{2}}_{g(\mu)}) \quad \Rightarrow \quad g(\mu) = \mu^{2}
$$
By the delta method, the limit approaches as follows
$$
\sqrt{n}(\bar{X}_{n}^{2} - \mu^{2})
\xrightarrow{d}
\mathcal{N}(0, \sigma^{2} \cdot (\underbracket{2\mu}_{g'(\mu)})^{2})
=
\mathcal{N}(0, 4\sigma^{2}\mu^{2})
$$
This could also be written as an approximate distribution
$$
\sqrt{n}(\bar{X}_{n}^{2} - \mu^{2})
\;\overset{a}{\sim}\;
\mathcal{N}(0, 4\sigma^{2}\mu^{2})
$$

##### Problem 2.
Given $X_{1}, X_{2}, \dots, X_{n}$ from $\mathcal{N}(\mu, 1)$ and $\bar{X}_{n} = \frac{1}{n} \sum_{i=1}^{n} x__{i}$ 

---
#statistics