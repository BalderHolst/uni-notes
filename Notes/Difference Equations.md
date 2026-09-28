# Difference Equations
Describe the output ($y$) as a function of an input ($x$) and previous values of $y$.

$$
y(n) = \sum^{M}_{i=0}b_{i}\ y(n-i) - \sum_{i=1}^{N}a_{i}\ y(n-i)
$$
This becomes
$$
H(z) = \frac{Y(z)}{U(z)} = \frac{b_{0} + b_{1}z^{-1} + \cdots + b_{M}z^{-M}}{1 + a_{1}z^{-1} + \cdots + a_{N}z^{-N}}
$$

#### First Order
$N=1$
$$y(n) = a_{0}x(n) + a_{1}x(n-1) - b_{1}y(n-1)$$
#### Second Order
$N=2$
$$y(n) = a_{0}x(n) + a_{1}x(n-1) + a_{2}x(n-2) - b_{1}y(n-1) - b_{2}y(n-2)$$

### Transfer Function
Same as in [[Laplace Transformation]].

$$H(z) = \frac{Y(z)}{X(z)}$$

>[!example]- Difference equation to transfer function
> $$y(n) = 2y(n-1) + 3x(n) \Rightarrow Y(z) = 2Y(z) \cdot z^{-1} + 3X(n)$$

>[!video]- Example: transfer function from difference equation
>![](https://www.youtube.com/watch?v=IJhyJGjeLvA)

---
#signalprocessing
