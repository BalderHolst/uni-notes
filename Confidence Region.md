# Confidence Region
See [[Lessons/Semester 7/statistics/Lektion 3 slides.pdf#page=3|slides]].

![[Pasted image 20260916132231.png|300]]

$$
T^{2} = (\bar{x} - \mu)^{T} \left(\frac{S}{n}\right)^{-1} (\bar{x} - \mu) \leq \frac{p(n-1)}{n-p} F(p, n-p)_\alpha
$$
$\mu$: Multidimensional variable!
$\bar{x}$: Multidimensional average
$S$: Sample Covariance
$p$: Dimensions
$n$: Sample Count
$\alpha$: Level of significance
$F$: Fisher distribution

#### Multiple 1D Confidence Intervals
To get an idea of confidence intervals in multidimensional cases, where the confidence region is unplottable, we can use a simple 1D confidence interval for each variable.

##### Naive Approach (Marginal CI's)
$$
\left[\bar{x_{i}} \pm t(n-1)_{ \alpha / 2 } \sqrt{\frac{S_{ii}}{n}}\right]
\quad i=1,\dots,p
$$
This is *to optimistic*; The CI is *too narrow*.

**Explaination**:
1D: $\mathbf{P}(\mu \in I_{\mu)} = 1-\alpha$
pD: $\mathbf{P}(\mu \in I_{\mu_{1}, \dots, \mu_{n})} \approx \mathbf{P}((1-\alpha)^{p} < 1 - \alpha)$

*Intuition*: We are less confiedent if multiple statements have to be true.

##### Bonferroni CI's
Choose $\alpha_{B} \overset{\mathrm{def}}{=} \frac{\alpha}{p}$, and use this instead of $\alpha$. It compensates for 


---
#multivariate-statistics