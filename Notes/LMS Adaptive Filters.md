---
created: 2026-11-02
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 11 slides.pdf]]"
  - "[[LMS algorithm and performance.pdf]]"
  - "[[LMS tutorial  (slides).pdf]]"
  - "[[Kuo & Lee - Real-time DSP, LMS chapter  (from textbook).pdf]]"
  - "[[Fleury - Response of LTI systems to Random Inputs  (tutorial).pdf]]"
  - "[[MATLAB documentation LMS.pdf]]"
  - "[[Wiki - LMS adaptive filter.pdf]]"
---
# LMS Adaptive Filters
A [[Notes/FIR Filtre|FIR filter]] with non-constant parameters. The Least Means Squared (LMS) algorithm changes these weights to minimize the error.


![[Pasted image 20261102082234.png|400]]

$x(n)$: Filter input signal
$d(n)$: "desired" / reference signal
$w(n)$: [[Notes/FIR Filtre|FIR Filter]] coefficients (change over time!)
$e(n)$: Error signal
$L$: Number of "tabs" in the FIR filter (could be around 20 - 40)

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

> [!example]- LMS Algorithm Implementation
> ![[Lessons/Semester 7/ssp/Lektion 11 slides.pdf#page=6]]

### Performance of LMS

#### 1. Stability / Convergence
We can *never* guarantee that we will ensure that we can converge, as the cost "landscape" is always changing. However, it will converge under stationary conditions IFF
$$
0 < \mu < \frac{2}{\lambda_{\max}}
$$
$\lambda$: Eigen values for $R_{xx}$.

Though this is not possible to calculate very often. We can do this instead:
$$
\lambda_{\max} \leq \sum_{i=0}^{L} \lambda_{i} = \mathrm{trace}(R_{xx}) = Lr_{xx}(0) = LP_{x}(n)
$$
Now we have a more practical way to estimate the max step size
$$
0 < \mu < \frac{2}{LP_{x}(n)}
$$
where signal power $P_{x}(n)$ can be estimates as.
$$
\hat{P}_{x}(n) = \frac{1}{K}\sum_{k=n - (K-1)}^{k=n}x^{2}(k)
$$
We could start by trying a stepsize of $\mu = \frac{1}{10} \cdot  \frac{2}{LP_{x}(n)}$.

#### 2. Convergence Speed
Time constant for $\lambda_{i}$ for $R_{xx}$
$$
\tau \approxeq \frac{1}{\mu \lambda_{i}}, \quad i=1,\dots,L
$$
The dominant time constant is the one with the largest $\lambda_{i}$.

We define the stepsize as
$$
u = \alpha \frac{2}{\lambda_{\max}}, \quad 0 < \alpha < 1
$$
$\alpha$: Closeness to the maximal step size

$$
\tau_{\max} = \frac{1}{2\alpha} \frac{\lambda_{\max}}{\lambda_{\min}}
$$

Here we can see that the eigenvalue "spead" should be minimized to minimize $\tau_{\max}$ and make the filter converge faster. White noise will result in a small spread.

### Normalized LMS - Time Varying Step Size
Now the $\mu(t)$ is time varying.

$$
\mu(n) = \frac{\beta}{L\hat{P}_{x}}, \quad 0 < \beta < 2
$$