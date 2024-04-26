# Optimal Control
Placing poles to optimize a cost function.

$$
\mathcal{J} = \int_{0}^{\infty} x^{T}Qx + u^{T}Ru\, \mathrm{dt}
$$
$Q$: "Price" of signal. [[Positive semi-definite matrix]].
$R$: "Price" of input. [[Positive definite matrix]]

If $Q$ is zero, no performance is specified, and the input $u$ becomes zero as the system does not need to reach its reference.

#### Example
$$
Q = C^{T}
$$

---
#controlsystems