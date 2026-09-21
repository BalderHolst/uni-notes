# Weiner Filter
See [[Lessons/Semester 7/ssp/Lektion 4 slides.pdf|slides]].

$$
\underset{\mathrm{Desired\ Signal}}{Y(n)}
\rightarrow \underset{\mathrm{Bluring\ Filter}}{G(f)}
\rightarrow+
\underset{\mathrm{Noise}}{W(n)}
\rightarrow
\underset{\mathrm{Observed\ Signal}}{X(n)}
\rightarrow
\underset{\mathrm{Wiener\ Filter}}{H(f)} \rightarrow
\underset{\mathrm{Estimate}}{\hat{Y}(n)}
$$

**Assumptions**:
$G(f)$ is *known* or estimated from a datasheet. $W(n)$ and $Y(n)$ are WSS which means that $R_{ww}$ and $R_{yy}$ are known.

> [!warning] Downsides
> Requres stationary conditions! In a changing enviornment, it has to be constantly recalculated.

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

Cost Function:
$$
\mathrm{MSE} = E \Big[
Y(n) - \sum_{-M_{1}}^{M_{2}}(h(m)X(n-m)^{2})
\Big]
$$
To find the optimal filter
$$
\begin{align}
\frac{\partial \mathrm{MSE}}{\partial h(j)} &= 0, \quad j = -M_{1}, \dots, M_{2} \\
\Rightarrow R_{xy}(j) &= \sum_{-M_{1}}^{M_{2}} h(m)R_{xx}(j-m)
\end{align}
$$
We can put this on a matrix form:
$$
\underset{(M_{1}+M_{2}+1 \times 1)}{
\begin{bmatrix}
R_{xy}(-M_{1}) \\
\vdots \\
R_{xy}(M_{2})
\end{bmatrix}
}

=

\underset{(M_{1} + M_{2} + 1) \times (M_{1} + M_{2} + 1)}{
\begin{bmatrix}
R_{xx}(0) & R_{xx}(1) & \cdots & R_{xx}(M_{1} + M_{2}) \\
R_{xx}(1) & \ddots & \ddots & \vdots \\
\vdots  & \ddots & \ddots & R_{xx}(1) \\
R_{xx}(M_{1} + M_{2}) & \cdots & \cdots & R_{xx}(0)
\end{bmatrix}
}

\underset{(M_{1} + M_{2} + 1) \times 1}{
\begin{bmatrix}
h(-M_{1}) \\
\vdots \\
h(M_{2}) \\
\end{bmatrix}
}
$$

$$
\begin{align}
\vec{h}_\mathrm{opt} &= R_{xx}^{-1} \cdot \vec{r}_{xy}
\end{align}
$$


#### IIR Weiner Filter
See [[IIR Filters]] and [[Lessons/Semester 7/ssp/Lektion 4 slides.pdf#page=4|slides]].
$$
\hat{Y}(n) = \sum_{-\infty}^{\infty} h(m)X(n-m)
$$

$$
H(f) = \frac{S_{xy}(f)}{S_{xx}(f)}
$$

> [!tip] Intuition
> For high signal-to-noise ratios (SNR) $H(f) \approx 1$, so we keep the signal. And the oppossite for low SNRs.

#### Deconvolution
See [[Lessons/Semester 7/ssp/Lektion 4 slides.pdf#page=5|slide]].

We try to reverse the effects of $G(f)$ and remove noise *at the same time*.

---
#statistical-signal-processing