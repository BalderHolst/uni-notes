# Differensligninger
Describe the output ($y$) as a function of an input ($x$) and previous values of $y$.
$$
y(n) = \sum_{i=0}^{N}a_{i}x(n-i) - \sum_{i=1}^{N}b_{i}y(n-i)
$$

#### Første Orden
$N=1$
$$y(n) = a_{0}x(n) + a_{1}x(n-1) - b_{1}y(n-1)$$
#### Anden Orden
$N=2$
$$y(n) = a_{0}x(n) + a_{1}x(n-1) + a_{2}x(n-2) - b_{1}y(n-1) - b_{2}y(n-2)$$

### Overføringsfuntion
Samme som i [[Laplace Transformation]].

$$H(z) = \frac{Y(z)}{X(z)}$$

>[!example]- Differensligning til overføringsfunction
> $$y(n) = 2y(n-1) + 3x(n) \Rightarrow Y(z) = 2Y(z) \cdot z^{-1} + 3X(n)$$

>[!video]- Example: transfer function from difference equation
>![](https://www.youtube.com/watch?v=IJhyJGjeLvA)

---
#signalprocessing