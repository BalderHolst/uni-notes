# Sample Mean and Variance
[[Expectation|Mean]] and [[Variance|variance]] of a sampled random variable. See [[lecture7.pdf#page=16|slides]].

$$
\bar{X}_{n} = \frac{1}{n} \sum_{i=1}^{n}X_{i}
\quad \quad
S^{2}_{n} = \frac{1}{n-1} \sum_{i=1}^{n}(X_{i} - \bar{X_{n}})^{2}
$$
$n$: Number of samples

Let $X_{1}, \dots, X_n$ be [[IID]] and let $\mu = \mathbb{E}(X_i)$  and $\sigma^{2} = \mathbb{V}(X_{i})$. Then
$$
\mathbb{E}(\bar{X}_{n}) = \mu,
\quad
\mathbb{V}(\bar{X}_{n}) = \frac{\sigma^{2}}{n} \quad \mathrm{and} \quad \mathbb{E}(S^{2}_{n}) = \sigma^{2}
$$

#### Standard Mean Error
$$
\mathrm{se} = \frac{\sigma}{\sqrt{n}} = \sqrt{\mathbb{V}(\bar{X}_{n})}
$$

---
#statistics