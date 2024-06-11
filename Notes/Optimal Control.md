# Optimal Control
See [[Lecture 11 - Integral Control.pdf#page=18|slides]].

Placing poles to optimize a cost function.

$$
\mathcal{J} = \int_{0}^{\infty} x^{T}Qx + u^{T}Ru\, \mathrm{dt}
$$
$Q$: "Price" of signal. [[Positive semi-definite matrix]].
$R$: "Price" of input. [[Positive definite matrix]]

If $Q$ is zero, no performance is specified, and the input $u$ becomes zero as the system does not need to reach its reference.

$Q$ is usualy on the form
$$
Q = C^{T}MC
$$
$C$: From [[State Space Models|state space model]].
$M$: A diagonal matrix specifying the weight of each signal.

#### Bryson's Rule
$$
\begin{align}
Q_{ii} &= \frac{1}{x_{\mathrm{max},i}^{2}} \\
R_{jj} &= \frac{1}{u_{\mathrm{max},j}^{2}}
\end{align}
$$


---
#controlsystems