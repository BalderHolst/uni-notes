# z-transformation

When we sample a signal, be may get poles repeated up and down the imaginary axis. The z-transformation solves this by *wrapping the imaginary axis around the unit circle* of the z-plane.

$$ X(z) = \mathcal{Z}\{x(t)\} = \sum_{n=0}^{\infty} x(n)z^{-n}  $$
$X(z)$ converges (is stable) if $|x| < 1$.

Zero points in the center only alter the phase, not the amplitude.
### Transfer Function
$$H(z) = \frac{Y(z)}{X(z)}$$
$X(z)$: Input sequence
$Y(z)$: Output sequence

**We cannot create a z-plane without a sample rate**.

![[Pasted image 20231012084315.png|400]]

#### Standard Transfer Functions
##### 1. Order
$$H(z) = \frac{Y(z)}{X(z)} = \frac{a_{0} + a_{1}z^{-1}}{1+b_{1}z^{-1}} = \frac{a_{0}z + a_{1}}{z + b_{1}}$$

>[!tip]- Nice Rules
>![[Pasted image 20231012085739.png]]
>![[Pasted image 20231012092152.png]]

>[!example]- Relation to [[Laplace Transformation]]
>![[lektion 7 - Digitale realisationsstrukturer.pdf#page=24]]

### Poles and Stability
Poles **within** the unit circle -> **stable system**
Poles **outside** the unit circle -> **unstable system**

### Relation to [[Laplace Transformation]]

$$
\begin{cases}
\mathcal{L}\{x(t)\} = \sum_{n=0}^{\infty} x(n)e^{-snT} \s s = \sigma + j\omega \\ 
\mathcal{Z}\{x(t)\} = \sum_{n=0}^{\infty} x(n)z^{-n} 
\end{cases}
\s\Rightarrow\s
s = e^{sT} = e^{\frac{\sigma}{f_{s}}} \cdot e^{2\pi}
$$

### The Real Axis
The real axis in the $z$-domain is mapped to the z-plane's real axis from $0$ to $\infty$. The negative part is mapped to the range $[0, 1]$.

### Inverse z-transform
See [[Lektion 5 - Introduktion til z-transformation.pdf#page=81|slides]].

**Make sure that the system is stable before converting back**

>[!example]-
>$$
>Y(z) = \frac{z}{(z-0.5)(z-0.25)}
>$$
>
>$$
>\frac{Y(z)}{z} = \frac{k_{1}}{z-0.5} + \frac{k_{2}}{z-0.25}
>$$
>Now we find $k_{1}$: let $z=p_{1} = 0.5$ (pole one).
>$$\frac{Y(z)}{z} \cdot (z-0.5) = k_{1} + k_{2}\frac{z-0.5}{z-0.25}$$
>
>$$
>\frac{\frac{z}{\cancel{(z-0.5)}(z-0.25)} \cdot \cancel{(z-0.5)}}{z} = \frac{\frac{z}{z-0.25}}{z} = k_{1}
>$$
>Substitute $z = 0.5$
>$$
>k_{1} = \frac{\frac{0.5}{0.5-0.25}}{0.5} = 4
>$$

[[Partialbrøker]]

### Foldningssum
See [[lektion 7 - Digitale realisationsstrukturer.pdf#page=10|slides]].

$h$-funktionen "spejles" med akse i $n$ ganges med $x$-funktionen.
$$y(n) = x(n) \times h(n) = \sum_{m=0}^{n}x(m) \cdot h(n - m)$$

---
#signalprocessing
