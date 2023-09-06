# Fourieseries
[[Trigonometri|Trigonometric]] approximations for **periodic signals**. (As opposed to [[Fourie-transformation]])

$$
f(x) = \frac{a_0}{2} + \sum^\infty_{n=1} \left( a_n \cos \left( \frac{n\pi x}{L} \right) + b_n \sin \left( \frac{n\pi x}{L} \right) \right) 
$$


$n$: A how many times of the base frequency.
$L$: The half period.

$$
\begin{align}
a_n &= \frac{1}{L} \int^L_{-L} f(x) \cos \left( \frac{n\pi x}{L} \right) \dx, \s n \geq 0 \\ \\
b_n &= \frac{1}{L} \int^L_{-L} f(x) \sin \left( \frac{n\pi x}{L} \right) \dx, \s n > 0
\end{align}
$$

You only need to integrate over the one period, thus from $-L$ to $L$.

##### Period and Frequency
$$L = \frac{T}{2} \arrows T = 2L \arrows f = \frac{1}{2L}$$

## With imaginaries
$$
\begin{align}
f(x) &= \sum^\infty_{-\infty} c_n e^{jn\pi x / L} \\
c_n &= \frac{1}{2}(a_n - jb_n), \s n > 0
\end{align}
$$


---
#matematik #signals 
