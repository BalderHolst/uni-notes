# Multivariate Normal Distribution (MVN)

## 1D
$$
X \sim N(\mu, \sigma^2)
$$
where
$$
\begin{align}
E[X] &= \mu \\
V[X] &= \sigma^{2}
\end{align}
$$

PDF:
$$
f(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{\frac{1}{2} \frac{x-\mu}{\sigma}}, \;\;x\in\mathbb{R}
$$


## PD
$$
X =
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{p} \\
\end{bmatrix}, \quad X_{(p\times 1)} \sim N_{p}(\mu, \Sigma)
$$
**PDF**
$$
exponent = - \frac{1}{2} (x - \mu)^T \Sigma^{-1}
$$


---
#multivariate-statistics 