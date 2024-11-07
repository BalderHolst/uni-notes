# Covariance and Correlation
See [[lecture7.pdf#page=17|slides]].

Let $X$ and $Y$ be random variables with [[Expectation|means]] $\mu_X$ and $\mu_Y$ and standard deviations $\sigma_X$ and $\sigma_Y$. Define **covariance** between $X$ and $Y$ as
$$
\mathrm{Cov}(X, Y) = \mathbb{E}\Big( (X - \mu_{X}) (Y - \mu_{Y})  \Big)
$$
### Correlation
![[Pasted image 20241107132801.png|center|400]]

Correlation is defined by
$$
\rho = \rho_{X,Y} = \rho(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sigma_{X}\,\sigma_{Y}} \in [-1, 1]
$$
Correlation indicates the *strength of the **linear** relationship* between $X$ and $Y$.

### Properties
*Covariance* satisfies
$$
\mathrm{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)
$$

Also
$$
\begin{align}
\mathbb{V}(X+Y) &= \mathbb{V}(X) + \mathbb{V}(Y) + 2\mathrm{Cov}(X,Y) \\
\mathbb{V}(X-Y) &= \mathbb{V}(X) + \mathbb{V}(Y) - 2\mathrm{Cov}(X,Y)
\end{align}
$$

or written generally
$$
\mathbb{V}\left( 
\sum_{i}a_iX_i
\right) =
\sum_i a_i^2\mathbb{V}(X_i) + 2 \sum\sum_{i<j}a_i a_j \mathrm{Cov}(X_i, X_j)
$$

---
#statistics
