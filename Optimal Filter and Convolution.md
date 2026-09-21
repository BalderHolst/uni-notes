# Optimal Filter and Convolution
See [[Lessons/Semester 7/ssp/Lektion 4 slides.pdf|slides]].

$$
\underset{\mathrm{Desired\ Signal}}{Y(n)}
\rightarrow \underset{\mathrm{Bluring\ Filter}}{G(f)}
\rightarrow+
\underset{\mathrm{Noise}}{W(n)}
\rightarrow
\underset{\mathrm{Wiener\ Filter}}{H(f)} \rightarrow
\underset{\mathrm{Estimate}}{\hat{Y}(n)}
$$

**Assumptions**:
$G(f)$ is *known*. $W(n)$ and $Y(n)$ are WSS.

## Finding the Optimal Filter
We define a cost function to minimize $H(f)$ and $h(n)$:
$$
\mathrm{MSE} = E \Big[ (Y(n) - \hat{Y}(n))^{2} \Big]
$$
#### FIR Weiner Filter
See [[Notes/FIR Filtre|FIR Filtre]].

$G = 1$.

$$
\hat{Y}(n) = \sum_{m=-M_{1}}^{M_{2}} h(m)X(n-m)
$$
$n$: Sample number
$$
\begin{cases}
-M_{1} &= 0 \quad\Rightarrow\quad \text{Causal Filter} \\
-M_{1} &< 0 \quad\Rightarrow\quad \text{Non-causal Filter}
\end{cases}
$$

Cost Function
$$
\mathrm{MSE} = E \Big[
Y(n) - \sum_{-M_{1}}^{M_{2}}(h(m)X(n-m)^{2})
\Big]
$$




---
#statistical-signal-processing