# Variance
"Spread" of a distribution.

Let $X$ be a random variable with mean $\mu$. The **variance** of $X$ is defined as
$$
\sigma^{2} = \mathbb{E}(X-\mu)^{2} = \int (x - \mu)^{2}\, dF(x)
$$
Can also be written as
$$
\sigma^{2} = \sigma_{X}^{2} = \mathbb{V}(X) = \mathbb{V}X
$$
*assuming that the [[Expectation|expectation]] exists*.

#### Standard Deviation
$$
\mathrm{sd}(X) = \sigma = \sigma_{X} = \sqrt{\mathbb{V}(X)}
$$

#### Properties

Squared random variable
$$
\mathbb{V}(X) = \mathbb{E}(X^{2}) - \mu^{2}
$$

If $a$ and $b$ are constants, then
$$
\mathbb{V}(aX+b) = a^{2}\mathbb{V}(X)
$$
Independent and scaled random variables
$$
\mathbb{V}\left( \sum_{i=1}^{n} a_{i}X_{i} \right) = \sum_{i=1}^{n} a_{i}^{2} \mathbb{V}(X_{i})
$$


---
#statistics
