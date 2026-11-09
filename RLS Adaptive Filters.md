---
created: 2026-11-09
tags: []
---

# RLS Adaptive Filters

RLS is a faster and *more complex* alternative to the [[LMS Adaptive Filters|LMS]] algorithm. It also changes [[Notes/FIR Filtre|FIR Filter]] coefficients to drive a filter error to zero.

### 1) Weiner Hopf
In RLS we try to estimate the optimal filter weights using [[Weiner Filter|Weiner Hopf]] in a recursive manner. This reduces the time complexity of calculating the otherwise expensive calculation to find the optimal filter cofficients:
$$
w(n) = R^{-1}_{xx} \cdot r_{dx}(n)
$$
$R_{xx}$: Correlation matrix
$r_{dx}$: Crosscorrelation vector


### 2) Approximations
Ensemble Mean
$$
\underset{\small (L \times L)}{R_{xx}(\bullet)} = \mathbb{E}[x(n) \cdot x(n^{T})]
$$
Sample 
$$
\begin{align}
\underset{\small (L \times L)}{R_{xx}(n)} &= \sum_{k=0}^{n} x(k) \cdot x(k)^{T} \\
\hat{R}_{xx}(n) &= \mathbb{E}[d(n) \cdot x(n)]A \\
\hat{r}_{dx}(n) &= \sum_{k=1}^{n} d(k)\ x(k)
\end{align}
$$


### 3) Limit Memory
Now RLS has infinite memory

We usually limit this with a "forgetting factor" $\alpha$ where $0 \ll \alpha < 1$.

This creates a window equivalent to
$$
N_{eq} = \sum_{k=0}^{\infty}\alpha^{k} = \frac{1}{1-\alpha}
$$
### 4) Cost function
We define a cost function that includes the forgetting factor, to that the filter is able to adapt to newer samples more strongly.
$$
\xi(n) = \sum_{k=0}^{n} \alpha^{n-k} e^{2}(k)
$$
$e^{2}(k)$: Squared error
$\alpha$: Forgetting factor

### 5) Recursive Estimates
$$
\begin{align}
\hat{R}_{xx} &= \alpha \underbrace{\hat{R}_{xx}(n-1)}_\mathrm{recursive} + x(n)\ x(n)^{T} \\
\hat{r}_{dx} &= \alpha \underbrace{\hat{r_{dx}(n-1)}}_\mathrm{recursive} + d(n)\ x(n)
\end{align}
$$
### 6) Recursive Filter Coefficients

$$
\hat{R_{xx}}
$$