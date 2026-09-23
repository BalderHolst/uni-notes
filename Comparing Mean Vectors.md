# Comparing Mean Vectors
See [[Lessons/Semester 7/statistics/Lektion 4 slides.pdf|slides]].

Two ways:
- [[#Paired Test|Paired Comparison]] (*Best*, but not always possible)
- Non-paired (Always possible)

## Paired Test
High *power* (ability to reject a hyposthesis if I should). Simple.

All observations come in *pairs*.
$$
(X_{1j}, X_{2j})\quad j= 1, \dots, n
$$
Both are [[Multivariate Normal Distribution|MVN]].
$$
\begin{align}
X_{1j} \sim N_{p}(\mu_{1}, \Sigma_{1}) \\
X_{2j} \sim N_{p}(\mu_{2}, \Sigma_{2})
\end{align}
$$
Their difference is then
$$
D_{j} = X_{1j} - X_{2j} \sim N_{p}\big(\underbracket{\mu_{1} - \mu_{2}, \Sigma_{0}}_\mathrm{unknown}\big)
$$
$H_{0}$: $\mu_{1} - \mu_{2} \overset{?}{=} \delta_{0}$ (most often $\delta_{0} = 0$)
$H_{1}$: $\mu_{1} - \mu_{2} \overset{?}{\neq} \delta_{0}$

$\delta_{0}$: Hypothesised difference

> [!info] Proving a new method is better!
> To show a new method is better, we would hypothiesize $\delta_{0} = 0$ and then hopefully reject it.
> Of course, we have to make sure your new mean is better and not worse.


**Estimates**:

$$
\hat{\mu}_{1} - \hat{\mu}_{2} = \bar{D} = \frac{1}{n} \sum_{j=1}^{n}D_{j} \sim N_{p}\left(\mu_{1} - \mu_{2}, \frac{\Sigma_{D}}{n}\right)
$$

$$
\underset{(p \times p)}{\hat{\Sigma}_{D}} = S_{D} = \frac{1}{n-1} \sum (D_{j}-\bar{D})(D_{j} - \bar{D})^{T}
$$

**Test Statistic**:
$$
T^{2} = [\bar{D} - (\mu_{1} - \mu_{2})]^{T} \left(\frac{S_{D}}{n}\right)^{-1}[\bar{D} - (\mu_{1} - \mu_{2})]
$$
$$
t_{0}^{2} = [\bar{D} - \delta_{0}]^{T} \left(\frac{S_{D}}{n}\right)^{-1}[\bar{D} - \delta_{0}] \sim \frac{p(n-1)}{n-p} F(p, n-p)
$$

If
$$
t_{0}^{2} > 
\frac{p(n-1)}{n-p} F(p, n-p)_{\alpha}
\quad

\quad
$$

We can now draw a [[Confidence Region|confidence region]], or do [[Multiple 1D Confidence Intervals|confidence intervals]]. All for $\delta_{0}$.

If the confidence region contains $0$, we confirm $\delta_{0} = 0$.

#### Bonferroni
$$
\left[\bar{D}_{j} \pm t(n-1)_{\alpha / 2p} \cdot \sqrt{\frac{S_{D,jj}}{n}}\right]
$$

---

## Non-paired test
Observations are *not in pairs*. Random samples from multiple populations. **Populations are independent**. Number of samples can be different.

$$
\begin{align}
X_{1j} \sim N_{p}(\mu_{1}, \Sigma_{1}), \quad j = 1,\dots,n_{1} \\
X_{2j} \sim N_{p}(\mu_{2}, \Sigma_{2}), \quad j = 2,\dots,n_{2}
\end{align}
$$
Best if $n_{1} \approx n_{2}$. This is a *balanced* dataset.

Same hypothesis as in [[#paired Test]]

$H_{0}$: $\mu_{1} - \mu_{2} \overset{?}{=} \delta_{0}$ (most often $\delta_{0} = 0$)
$H_{1}$: $\mu_{1} - \mu_{2} \overset{?}{\neq} \delta_{0}$

---
#statistics