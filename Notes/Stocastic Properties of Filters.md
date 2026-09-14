# Stocastic Properties of Filters

### Linear-filtering of Random Signals
We assume that we know the filter.

$$
X(t) \rightarrow \underbracket{H(w)}_\mathrm{filter} \rightarrow Y(t)
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

$$
R_{yy} = h(z) * h(-\tau) * R_{xx}(\tau)
$$
$$
S_{yy} = \underbracket{|H(w)|^{2}}_\mathrm{Power\ Gain} \cdot S_{xx}(w)
$$

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
##### PSD
$$
S_{xy}(w) = H(w) \cdot S_{xx}(w)
$$
For system identification:
1. Feed the filter with white noise (contains all frequencies)
2. Estimate the plat filter with
$$
\hat{H}(w) = \frac{\hat{S}_{xy}(w)}{\sigma_{x}^{2}}
$$


---
#statistical-signal-processing
