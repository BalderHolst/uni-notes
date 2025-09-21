# Exponential Distribution
Can model things like lifetimes of electronic components.

![[Exponential-Distribution.png|center|300]]

$$
X \sim \mathrm{Exp}(\beta)
$$

Probability Density Function (pdf):
$$
f(x) = \frac{1}{\beta} e^{{-x}/{\beta}}, \quad x > 0
$$
Cumulative Density Function (cdf):
$$
F(x) = 1 - \exp\left(-\frac{x}{\beta}\right)
$$
#### Memorylessness
The current waiting time is independent to the previous 
waiting time.
$$
\mathbf{P}(X > t + s|X > t) = \mathbf{P}(X > s)
$$

---
#statistics #distribution