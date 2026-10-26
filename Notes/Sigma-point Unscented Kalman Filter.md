---
created: 2026-10-26
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 7 slides.pdf]]"
  - "[[Agenda STATSIG lecture 07.pdf]]"
  - "[[demo UT.pdf]]"
  - "[[UT slides.pdf]]"
  - "[[UKF algorithm.pdf]]"
---

# Sigma-point ("Unscented") Kalman Filter
Kalman filter that accounts for non-linearities on the system by using distribution representitive "sigma-points", to estimate the input distributions transformed by the non-linear system. This leads to better results than the [[Extended Kalman Filter]] because it is a **3rd order approximation**, as opposed to the 1st order approximation in the EKF.


*Non-linear* system:
$$
\begin{align}
x_{k+1} &= f(x_{k}, u_{k}) + w_{k}, &w_{k} \sim N(0, Q_{k}) \\
y_{k} &= h(x_{k}) + v_{k}, &v_{k} \sim N(0, R_{k}) \\
\end{align}
$$
$x_{k}$: State vector a current current time step
$y_{k}$: Output at current time step
$w$: Process noise
$v$: Observation noise

## Sigma Points - Unscented Transform
See [[UT slides.pdf|UT slides]].

We choose sigma points that describe the state distribution through the non-linearities. To get a good estimate for the states in the non-linear system.

![[Pasted image 20261026085813.png|400]]

We define $2n$ $x$-sigma points:
$$
x^{(i)} = \bar{x} + \tilde{x}^{(i)}, i=1,\dots, 2n
$$
Offsets are defined as
$$
\begin{cases}
\tilde{x}^{(i)} &= \sqrt{nP_{x}} |_{i\mathrm{'th\ col}} \\
\tilde{x}^{(n+i)} &= -\sqrt{nP_{x}} |_{i\mathrm{'th\ col}}
\end{cases}
\quad i=1,\dots, n
$$
$P_{x}$: Covariance matrix

Chosen so the sample mean is the real mean, and the sample covariance matrix is the true covariance matrix.

We now take them through the non-linearity $f(x, u)$.

$$
\begin{align}
y^{(i)} &= f(x^{(i)}), &i=1,\dots,2n\\
w^{(i)} &= \frac{1}{2n}, &i=1,\dots,2n \\
\end{align}
$$

**Estimate**:
$$
\begin{align}
\hat{\bar{y}} &= \sum_{i=1}^{2n}w^{(i)} y^{(i)} \\
\hat{P_{y}} &= \sum_{i=1} w^{(i)} (y^{(i)} - \hat{\bar{y}})(y^{(i)} - \hat{\bar{y}})^{T}
\end{align}
$$
We now have $2n$ $y$-sigma points!

> [!example]- UT Transformation Demo
>![[demo UT.pdf]]

## Algorithm
![[UKF algorithm.pdf]]