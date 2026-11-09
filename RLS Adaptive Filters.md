---
created: 2026-11-09
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 12 slides.pdf]]"
  - "[[Wiki - RLS adaptive filter.pdf]]"
  - "[[RLS tutorial  (slides).pdf]]"
  - "[[RLS algorithm and performance.pdf]]"
---

# RLS Adaptive Filters

RLS is a faster and *more complex* alternative to the [[LMS Adaptive Filters|LMS]] algorithm. It also changes [[Notes/FIR Filtre|FIR Filter]] coefficients to drive a filter error to zero.

![[Pasted image 20261109093216.png|400]]

$x(n)$: Filter input signal
$d(n)$: "desired" / reference signal
$w(n)$: [[Notes/FIR Filtre|FIR Filter]] coefficients (change over time!)
$e(n)$: Error signal
$L$: Number of "tabs" in the FIR filter (could be around 20 - 40)

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
\hat{R}_{xx}(n) &= \mathbb{E}[d(n) \cdot x(n)] \\
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
\begin{align}
\hat{R}_{xx}\ w(n) &= \alpha\ \hat{R}_{xx}(n-1)w(n-1) + d(n)x(n) \\
\hat{R}_{xx}\ w(n) &= (\hat{R}_{xx}(n) - x(n) x(n)^{T}) - w(n-1) + d(n) x(n) \\
w(n) &= w(n-1) + \hat{R}_{xx}^{-1}(n)\ x(n) \underbrace{\big[ d(n) - x(n)^{T} w(n-1) \big]}_{e(n)} \\
w(n) &= w(n-1) + \hat{R}_{xx}^{-1}(n)\ x(n)\ e(n)
\end{align}
$$

### 7) Recursive Matrix Inversion
Using Shermann-Morrison inversion equation
$$
(A + uv^{T})^{-1} = A^{-1} - \frac{A^{-1} uv^{T} A^{-1}}{1 + v^{T} A^{-1} u}
$$
Here the variables are
$$
\begin{align}
A &\to \alpha \hat{R}_{xx}(n-1) \\
uv^{T} &\to x(n) x(n)^{T}
\end{align}
$$
Which gives us
$$
\hat{R}_{xx}^{-1}(n) = \frac{1}{\alpha} \hat{R}_{xx}^{-1}(n-1) 
=
\frac{
\frac{1}{\alpha} \hat{R}_{xx}^{-1}(n-1)\ x(n)x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)
}{
\alpha\ x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)\ x(n)
}
$$
Which can be simplified as
$$
\hat{R}_{xx}^{-1}(n) = 
\left[
\hat{R}_{xx}^{-1}(n-1) -
\frac{
\hat{R}_{xx}^{-1}(n-1)\ x(n)x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)
}{
\alpha\ x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)\ x(n)
}
\right]
$$

### 8) Finally RLS Algorithm!
$$
w(n) = w(n-1) + 
\frac{1}{\alpha}
\left[
\hat{R}_{xx}^{-1}(n-1) -
\frac{
\hat{R}_{xx}^{-1}(n-1)\ x(n)x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)
}{
\alpha\ x(n)^{T}\ \hat{R}_{xx}^{-1}(n-1)\ x(n)
}
\right] x(n)\ e(n)
$$

## Algorithm from Slides

![[Lessons/Semester 7/ssp/Lektion 12 slides.pdf#page=6|Lektion 12 slides]]