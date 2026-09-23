# Bartlett Test (Box's M-test)
Assumption test for homoscedasticity. *Hard to pass*.

**Model**:
$$
\begin{align}
X_{1j} \sim N_{p}(\mu_{1}, \Sigma_{1}) \\
X_{1j} \sim N_{p}(\mu_{2}, \Sigma_{2})
\end{align}
$$
$\mu_{1}$, $\mu_{2}$, $\Sigma_{1}$ and $\Sigma_{2}$ are unknown.

We test the following:
$H_{0}$: $\Sigma_{1} \overset{?}{=} \Sigma_{2}$
$H_{1}$: $\Sigma_{1} \neq \Sigma_{2}$

For this, we use a [[Likelihood Ratio Test]].

**Unconstrained Model**: $\Sigma_{1}, \Sigma_{2}$ (different)
**Constrained Model**: $\Sigma_{1} = \Sigma_{2} = \Sigma$

#### Test Statistic
First, find $S_{1}$, $S_{2}$ and $S_{p}$.


$$
T_{B} = c \Big[
(n_{1} + n_{2} - 2) \log |S_{p}|
- (n_{1} - 1) \log |S_{1}|
- (n_{2} - 1) \log |S_{2}|
\Big]
\sim \chi^{2}(\mathrm{df} - \mathrm{df}_{H_{0}})
$$
$S_{p}$: $\frac{ (n_{1} - 1) S_{1} + (n_{2} - 1)S_{2} }{n_{1}+n_{2}-2}$
$\mathrm{df}$: Number of elements in $\Sigma_{1}$, $\Sigma_{2}$
$\mathrm{df}_{H_{0}}$: Number of elements in $\Sigma$

The correction factor $c$ is defines as:
$$
c = 1 - \frac{2p^{2} + 3p - 1}{6(p+1)}\left(\frac{1}{n_{1}-1} + \frac{1}{n_{2}-1} - \frac{1}{n_{1} + n_{2} - 2}\right) \approx 1\ \mathrm{usually}
$$


This is usually close to $1$, and doesn't make much of a difference. Crazy formula though...

If
$$
t_{B} > \chi^{2}\left(p \frac{p+1}{2}\right)_{\alpha} \quad \Rightarrow \quad \mathrm{reject}\ H_{0}
$$
**Rejection will happen often**, as the bartlett test is hard to pass. You may have to accept $H_{0}$ in some cases if it is just outside of a $95\%$ confidence, if that is acceptable.

---
#statistics