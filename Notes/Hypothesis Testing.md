# Hypothesis Testing
Most useful for *comparing*.

Test if an alternative hypothesis is worth accepting or rejecting as opposed to the currently accepted hypothesis.

$H_{0}$: Null hypothesis; currently accepted hypothesis
$H_{1}$: Alternative hypothesis

---

### Multivariate

Model: $\set{ X_{1}, \dots, X_{n} }$ ([[iid]]).
$$
X_{j} \sim N_{p}(\underset{\mathrm{unknown}}{\mu,\ \Sigma})
$$
We do a model check to verify our model.

$H_{0}$: $\mu \overset{?}{=} \mu_{0}$
$H_{1}$: $\mu \neq \mu_{0}$

We use **estimators** of the model parameters.

*Mean* is estimated as an averate:
$$
\hat{\mu} = \bar{X} = \frac{1}{n}\sum_{j=1}^{n} x_{j} \sim N_{p}\left(\mu, \frac{\Sigma}{n}\right)
$$
*Covariance*:
$$
\hat{\Sigma} = S = \frac{1}{n-1} \sum_{j=1}^{n}(x_{j} - \bar{x})(x_{j} - \bar{x})^{T}
$$
#### Test Statistic
1D:
$$
t = \frac{\bar{x}-\mu_{0}}{S / \sqrt{n}} \sim t(n-1) 
\quad \overset{\mathrm{equivalently}}{\rightarrow} \quad
t^{2} = \frac{(\bar{x} - \mu_{0})^{2}}{\frac{S^{-2}}{n}} \sim F(1, n-1)
$$
pD (Hotelling):
$$
T^{2}_{(1 \times 1)} = (\bar{X} - \mu_{0})^{T} \left(\frac{S}{n}\right)^{-1} (\bar{X} - \mu_{0}) \sim \frac{p(n-1)}{n-p}F(p, n-p)
$$
$F$: [[Fisher Distribution]]

#### Test
Calculate the test-statistic $T^{2}_{0}$ by using estimates and $H_{0}$.

If $T_{2}$ is *big*, we *reject* the hypothesis.

We use an $\alpha$ value (level of significance) to determine if $T^{2}$ should be reject. Usually set to **5%**. This means that we have a 5% chance of rejecting $H_{0}$, even if it was true.

Matlab function to accomplish this:
```matlab
finv(1 - alpha, p, n-p)
```
This calculates: $F(p, n-p)_{\alpha}$.

We **reject** if $T^{2} > \frac{p(n-1)}{n-p} f(p, n-p)_{\alpha}$.

#### P-value
> *"You can think of it as a rareness indicator"*
> \- Claus

We can also calculate the p-value to se how much we reject the hypothesis.

$$
\begin{align}
p_\mathrm{value} &= \mathbf{P}\left[ F(p, n-p) > \frac{n-p}{p(n-1)} t_{0}^{2}\right] \\
&= 1 - \mathrm{fcdf}\left(\frac{n-p}{p(n-1)}, t_{0}^{2}, p,n-p\right)
\quad \leftarrow \quad \mathrm{for\ calculating}
\end{align}
$$
$\mu$: Multidimensional variable!
$\bar{x}$: Multidimensional average
$S$: Sample Covariance
$p$: Dimensions
$n$: Sample Count
$\alpha$: Level of significance
$F$: Fisher distribution

---

#### Tests
- [[Wald Test]]
- [[Log-likelihood Test]]
- [[Score Test]]

#### Error Types

**Type I Error ($\alpha$)**
Rejecting the null hypothesis ($H_0$) when it is actually true. Represents a "false positive".

**Type II Error ($\beta$)**
Failing to reject the null hypothesis ($H_0$) when it is actually false. Represents a "false negative."

$$
\beta =
\begin{cases}
\mathbf{P}(Z \leq p_\mathrm{upper}) - \mathbf{P}(Z \leq p_\mathrm{lower}) \\
\mathbf{P}(Z \leq p)
\end{cases}
$$
$Z$: [[Z-distribution|Z distributed]] random variable
$p$: [[P-value]]. One or two depending on the type of test (single/double sided)


---
#statistics