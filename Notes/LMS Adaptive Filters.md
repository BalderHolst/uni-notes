---
created: 2026-11-02
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 11 slides.pdf]]"
  - "[[LMS algorithm and performance.pdf]]"
---

# LMS Adaptive Filters
A [[Notes/FIR Filtre|FIR filter]] with non-constant parameters. The Least Means Squared (LMS) algorithm changes these weights to minimize the error.


![[Pasted image 20261102082234.png|400]]

$x(n)$: Filter input signal
$d(n)$: "desired" / reference signal
$w(n)$: [[Notes/FIR Filtre|FIR Filter]] coefficients (change over time!)
$e(n)$: Error signal
$L$: Number of "tabs" in the FIR filter

Usually we use **white noise** as the filter input $x(n)$, as this will "trigger" all frequencies in the system.

> [!example]- LMS for system identification
> Using an LMS filter for system identification
> ![[Pasted image 20261102082631.png]]

### Calculating Optimal Filter Coefficients
See [[Lessons/Semester 7/ssp/Lektion 11 slides.pdf#page=4|slide]].

Same solution as in the [[Weiner Filter]]:
$$
w(n) = R_{xx}^{-1}(n) \cdot r_{dx}(n)
$$
This usually requires [[WSS]], but here we would simply recalcuate the coefficients very often to update the filter. However, this becomes quite a heavy algorithm.

Instead we estimate $R_{xx}$ with the sample means instead of ensemble means.
$$
\hat{R}_{xx}(n) = c \sum_{k=0}^{n}x(k)x^{T}(k)
$$
$r_{dx}(n)$ is also estimated as sample means
$$
\hat{r}_{dx}(n) = c \sum_{k=0}^{n}d(k)x(n)
$$
This ***will not be optimal***, but we save a matrix inversion which is $O(n^{L})$.

### Search for Optimal Filter Coefficients
**Steepest Decent Algorithm**: We iterate toward the unique minimum of the cost funcion.

Because $R_{xx}$ is symmetric and contains the same elements on either side og the diagonal, the MSE cost will be an eliptic parabola with *one single global minimum*.

$$
\begin{align}
w(n+1) &= w(n) - \frac{\mu}{2} \vec{\nabla}\xi \\
&= w(n) - u \big[
R_{xx}(n) w(n) - r_{dx}(n)
\big]
\end{align}
$$
$\vec{\nabla}\xi$: Gradient of the cost function
$\mu$: Stepsize

We will still have to estimate $R_{xx}(n)$, but is now $O(n^{2})$. Still not great, but better.

### Dismiss the Expectation Operator

We modify the cost function:
$$
\xi(n) = \mathbb{E}(e^{2}(n)) \to \xi(n) = e^{2}(n)
$$
The new gradient is then
$$
\begin{align}
\vec{\nabla}\xi(n) &= 2e(n)\ \vec{\nabla}e(n) \\
&= 2\ e(n)\ (-x(n))
\end{align}
$$
And the weights can be updated as
$$
w(n+1) = w(n) + \mu\ e(n)\ x(n)
$$
This is called the Least (Mean) Square / LMS algorithm.