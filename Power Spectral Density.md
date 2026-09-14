# Power Spectral Density (PSD)
See [[Lessons/Semester 7/ssp/Lektion 2 slides.pdf#page=3|slides]].

Power pr. bandwidth (interval of frequenzy)

### Power Spectral Density Function
$$
\begin{align}
S_{xx}(w) &= \mathcal{F} \{ R_{xx}(\tau) \} \\
&= \int_{-\infty}^{\infty} R_{xx}(\tau) e^{-jw\tau} \quad \left[\frac{v^{2}}{Hz}\right]
\end{align}
$$
$\tau$: Lag ($t_{2} - t_{1}$)

### Auto-correlation function
$$
\begin{align}
R_{xx} &= \mathcal{F}^{-1} \{ S_{xx}(w) \} \\
&= \frac{1}{\pi} \int_{-\infty}^{\infty} e^{jw\tau} dw
\end{align}
$$

$$
R_{xx}(\tau) = E[x(\tau)x(t + \tau)] \\
$$

$$
R_{xx}(0) = E[x^{2}(t)] = \mathrm{total\ power} = \frac{1}{2\pi} \int_{-\infty}^{\infty} S_{xx}(w)\ dw \quad [V^{2}]
$$


> *"To get a power i need to integrate over an inverval"*
> \- Claus

Same idea as a PDF function.

Power in $[w_{1}, w_{2}]$:
$$
2 \frac{1}{2\pi} \int_{w_{1}}^{w_{2}} S_{xx}(w)\ dw \quad [V^{2}]
$$


---
#statistical-signal-processing