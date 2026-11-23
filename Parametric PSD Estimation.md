---
created: 2026-11-23
tags:
  - multivariate-statistics
slides:
  - "[[Lecture Material/Semester 7/ssp/Lektion 9 slides.pdf]]"
  - "[[Overview over methods for Spectral Estimation.pdf]]"
  - "[[Model-based (parametric) spectral estimation.pdf]]"
---

# Parametric (model-based) PSD Estimation

Much better than [[Non-paramtric PSD Estimation#Welch's Method|Welch's Method]] for short signals / few samples.

We assume that our samples were genereated with zero-mean white noise, through an unknown filter.

We estimate filter coefficients.
$$
\hat{H}(z)
$$
to get the PSD estimate
$$
\hat{P}_{x} = P_{e}|\hat{H}(f)|^{2} = \sigma_{e}^{2}|\hat{H}(f)|^{2}
$$

### System Types

##### 1) Autoregressive (AR)
$p$ poles, no zeros. Infinite impulse response (best for peaks).
$$
H(z) = \frac{b_{0}}{1 + \sum_{k=1}^{p} a_{k}z^{-k}}
$$
1. $N$ samples of $x(n)$
2. Estimate correlation function
$$
\hat{r}_{x}(\tau) = \frac{1}{N} \sum_{n=0}^{N-1} x(n)x(n+\tau)
$$
3. Assume $p$
4. Calculate coefficients
$$
\hat{r}_{x}(\tau)\ \to\ \hat{b}_{0},\ \set{\hat{a}_{k}}_{k=1,\dots,p}
$$

> [!seealso]- How do find coefficients
> ![[Lecture Material/Semester 7/ssp/Lektion 9 slides.pdf#page=4]]

5. $\hat{H}(z)$
6. $\hat{P}_{x}(f) = |\hat{H}(f)|^{2}$


##### 2) Moving Average (MA)
No poles, $q$ zeros (more smooth spectra).

##### 3) Autoregressive Moving Average
$p$ poles, $q$ zeros. Most general, but *complicated mathematically*.

### System Order
Must be assumed/iterated.

