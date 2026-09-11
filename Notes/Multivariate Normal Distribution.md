# Multivariate Normal Distribution (MVN)
See [[Lektion 2 slides.pdf#page=2|slides]].

[[Notes/Normal Distribution|Normal distribution]] in multiple ($p$) dimensions.

$$
X =
\begin{bmatrix}
X_{1} \\
X_{2} \\
\vdots \\
X_{p} \\
\end{bmatrix}, \quad X_{(p\times 1)} \sim N_{p}(\mu, \Sigma)
$$

$$
\begin{align}
E[X] &= \mu \\
\mathrm{Cov}[X] &= \Sigma
\end{align}
$$

**PDF**
$$
f_{X}(x)= (2\pi)^{-p}{2}\; |\Sigma|^{-\frac{1}{2}} \; \mathrm{exp}({- \frac{1}{2} (x - \mu)^T \Sigma^{-1}})
$$

> [!example]- 1D Normal Distribution
> $$
> X \sim N(\mu, \sigma^2)
> $$
> where
> $$
> \begin{align}
> E[X] &= \mu \\
> V[X] &= \sigma^{2}
> \end{align}
> $$
> 
> PDF:
> $$
> f(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{\frac{1}{2} \frac{x-\mu}{\sigma}}, \;\;x\in\mathbb{R}
> $$


---
#multivariate-statistics 
