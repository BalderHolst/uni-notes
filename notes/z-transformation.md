# z-transformation

$$z = e^{j\omega T}$$

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

### Lookup Tables
![[Pasted image 20231012085739.png|center|450]]
![[Pasted image 20231012092152.png|center|450]]

#### Standard Transfer Functions
##### 1. Order
$$H(z) = \frac{Y(z)}{X(z)} = \frac{a_{0} + a_{1}z^{-1}}{1+b_{1}z^{-1}} = \frac{a_{0}z + a_{1}}{z + b_{1}}$$
##### 2. Order
$$H(z) = \frac{Y(z)}{X(z)} = \frac{a_{0} + a_{1}z^{-1} + a_{2}z^{-2}}{1+b_{1}z^{-1}+b_{2}z^{-2}} = \frac{a_{0}z^2 + a_{1}z + a_{2}}{z^{2} + b_{1}z + b_{2}}$$


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
This is done with a ***table lookup***. See [[#Lookup Tables|tables]]. See [[Lektion 5 - Introduktion til z-transformation.pdf#page=81|slides]].

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

### Impulse Response ([[Impulse Response|note]])

##### For the Unit Sample
The impulse response $h(n)$ for a [[Unit Sample|unit sample sequence]] can be found by taking the inverse z-transformation of the transfer function.

$$h(n) = \mathcal{Z}^{-1}\{H(z)\}$$
### Stabilitet
See [[Lektion 6 - Systemanalyse i z-domæne.pdf#page=42|slides]].

#### Stabilt system
Et system er stabilt hvis dets impulsrespons $h(n)$ *går mod nul når n går med uendelig*.
$$\lim_{n\to\infty}\ |h(n)| = 0$$
Her ligger **alle poler inden for enhedscirklen** i z-domænet.
$$|p_{i}| < 1, \s \forall i \in \set{1,2,3,\dots,N}$$
#### Marginalt stabilt system
Et system er marginalt stabilt hvis dets impulsrespons $h(n)$ går mod konstant værdi forskellig fra nul eller *oscillerer med konstant amplitude og frekvens* når $n$ går mod uendelig.

**Mindst én pol skal ligge på enhedcirklen** og resten indenfor.

#### Ustabilt system
Et system er ustabilt hvis dets impulsrespons $h(n)$ vokser ubegrænset når $n$ går mod $\infty$.
$$\lim_{n\to\infty}\ |h(n)| = \infty$$
Hvis bare **én pol ligger udenfor enhedscirklen** er systemet ustabilt.
$$|p_{i}| > 1, \s \exists i \in \set{1,2,3,\dots, N}$$

### Frekvensrespons
See [[Lektion 6 - Systemanalyse i z-domæne.pdf#page=46|slides]].
See also [[Lektion 6 - Systemanalyse i z-domæne.pdf#page=66|grafisk bestemmelse]].

---
#signalprocessing
