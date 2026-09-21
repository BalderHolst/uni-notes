# Optimal Filter and Convolution
See [[Lessons/Semester 7/ssp/Lektion 4 slides.pdf|slides]].

$$
\underset{\mathrm{Desired\ Signal}}{Y(n)}
\rightarrow \underset{\mathrm{Bluring\ Filter}}{G(f)}
\rightarrow+
\underset{\mathrm{Noise}}{W(n)}
\underset{}{\rightarrow}
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
\b
\vec{h}_\mathrm{opt} = R_{xx}^{-1} \bullet \vec{r}_{xy}
$$

> [!warning] Downsides
> Requres stationary conditions!


---
#statistical-signal-processing