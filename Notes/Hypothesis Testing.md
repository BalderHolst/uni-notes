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
Calculate the test-statistic $T^{2}$ and determine


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