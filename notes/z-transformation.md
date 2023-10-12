# z-transformation

When we sample a signal, be may get poles repeated up and down the imaginary axis. The z-transformation solves this by *wrapping the imaginary axis around the unit circle* of the z-plane.

$$ \mathcal{Z}\{x(t)\} = \sum_{n=0}^{\infty} x(n)z^{-n}  $$

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
s = e^{sT} = e^{j\omega T}
$$


---
#signalprocessing
