# Stocastic Properties of Filters

### Linear-filtering of Random Signals
We assume that we know the filter.

$$
X(t) \rightarrow \mathrm{filter} \rightarrow Y(t)
$$
We can now find the following properties of $X$: $\mu_x$, $R_{xx}$, $S_{xx}$ and $P_x$.

and for $Y(t)$

$$
\begin{align}
\mu_{y} &= E[Y(t)] = E \left[ \int h(m) X(t-m)\ dm \right] \\
&= \int h(m)\ \underbrace{E[X(t-m)]}_{\mu_{x}}\ dm \\
&= \mu_{x} \cdot \int h(t)\ dt
\end{align}
$$
$m$: Convolution dummy variable.

$R_{yy}$
$S_{yy}$
$P_y$

For their correlaiton:

$$
\begin{align}
R_{xy}(\mu) &= E[x(t) Y(t+\tau)] \\
&= E\Big[X(t) \underbrace{\int h(m) X(t + \tau - m)}_{h(t) * X(X(t + \tau))}\ dm \Big] \\
&= \int h(m) \underbrace{E\Big[X(t) X(t + \tau - m)\Big]}_{R_{xx}(\tau - m)}\ dm \\
&= \int h(m) R_{xx}(\tau-m)\ dm \\
&= h(z) * R_{xx}(\tau)
\end{align}
$$
$*$: Convolution

$$
\begin{align}
R_{yx}(\tau) &= R_{xy}(-\tau) \\
&= h(-\tau) * R_{xx}
\end{align}
$$



---
#statistical-signal-processing
