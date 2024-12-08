# Delta Method
Given a sequence of [[Random Variables]] $X_{1}, X_{2}, \dots, X_{n}$. If a function $g$ can be defined, the distribution converges as follows.

$$
\sqrt{n}(g(X_{n}) -g(\mu)) \;\xrightarrow{d}\; \mathcal{N}(0, ( (g'(\mu))^{2} \cdot \sigma^{2}))
$$

also
$$
\widehat{\mathrm{se}}(g(\hat{\theta}))=|g'(\hat{\theta})| \cdot \widehat{\mathrm{se}}(\hat{\theta}),
$$

We can then construct a confidence interval like so:
$$
C_{n} = \Big[\;
g(\hat{\theta}) - z_{\alpha / 2}\, \widehat{\mathrm{se}}(g(\hat{\theta})), \;\;
g(\hat{\theta}) + z_{\alpha / 2}\, \widehat{\mathrm{se}}(g(\hat{\theta}))
\;\Big]
$$


---
### Examples

##### Problem 1.
What is the asymptotic limit of $\sqrt{n}(\bar{X}_{n}^{2} - \mu^{2})$?

Here we can now look for the $g$ function
$$
\sqrt{n}(\underbracket{\bar{X}_{n}^{2}}_{g(X_{n})} - \underbracket{\mu^{2}}_{g(\mu)}) \quad \Rightarrow \quad g(\mu) = \mu^{2}
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
Given $X_{1}, X_{2}, \dots, X_{n}$ from $\mathcal{N}(\mu, 1)$ and $\bar{X}_{n} = \frac{1}{n} \sum_{i=1}^{n} x_{i}$ and $\mu \neq 0$. What is the asymptotic limit of $\sqrt{n}\left( \frac{1}{\bar{X}_{n}} - \frac{1}{\mu^2} \right)$?

By the delta method, find $g(\mu)$.
$$
\sqrt{n}\ \bigg(
\underbracket{\frac{1}{\bar{X}_{n}}}_{g(X_{n})} - \underbracket{\frac{1}{\mu^2}}_{g(\mu)}
\bigg)
$$
let $g(\mu) = \frac{1}{\mu^{2}}$.
$$
g(\mu) = \frac{1}{\mu^{2}} = \mu^{-2}
\quad\Rightarrow\quad
g'(\mu) = -2\mu^{-3} = \frac{-2}{\mu^3}
$$

Here, $\mu$ has to be *non-zero*, as given in the problem.

---
#statistics