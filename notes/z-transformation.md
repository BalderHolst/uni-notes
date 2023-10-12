# z-transformation

When we sample a signal, be may get poles repeated up and down the imaginary axis. The z-transformation solves this by *wrapping the imaginary axis around the unit circle* of the z-plane.

$$ \mathcal{Z}\{x(t)\} = \sum_{n=0}^{\infty} x(n)z^{-n}  $$

**We cannot create a z-plane without a sample rate**.

![[Pasted image 20231012084315.png|400]]

>[!tip]- Nice Rules
>![[Pasted image 20231012085739.png]]
>![[Pasted image 20231012092152.png]]

### Poles
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

##### 

[[Partialbrøker]]

---
#signalprocessing
