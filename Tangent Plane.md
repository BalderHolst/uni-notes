# Tangent Plane
![[Pasted image 20230911130655.png|300]]

$$\vec n = \vec T_{1} \cdot \vec T_{2} = 
\left(
\begin{matrix}
i & j & k \\
0 & 1 & f_{2}(a,b) \\
1 & 0 & f_{1}(a,b)
\end{matrix}
\right)
= f_{1}(a,b)i + f_{2}(a,b)j - k
$$

>[!example]- Finding the Normal Vector
>Find a normal vector and equation of the tangent plane and normal line to the graph.
>$$z = f(x,y) = \sin (xy) \s \text{at} \, P\left(\frac{\pi}{3}, -1\right)$$
>Calculate $z$
>$$z = \sin\left(\frac{-\pi}{3}\right) = \frac{-1}{2}$$
>Partial derivatives
>$$f_{1} = \frac{\partial z}{\partial x} = \frac{\partial}{{\partial x}} \sin(xy) = \cos(xy) \cdot y \cdot 1$$
>$$f_{2} = \frac{\partial z}{\partial y} = \frac{\partial}{{\partial y}} \sin(xy) = \cos(xy) \cdot x \cdot 1$$
>Calculate $\vec n$
>$$
>\vec n = f_{1}(a,b)i + f_{2}(a,b)j - k = \cos\left(\frac{\pi}{3} \cdot (-1)\right) \cdot (-1) + \cos\left(\frac{\pi}{3} \cdot (-1)\right) \cdot \frac{\pi}{3} - k
>$$
>
>$$
>\vec n = -\frac{1}{2}i + \frac{1}{2} \cdot \frac{\pi}{3}j - k = - \frac{1}{2}i + \frac{\pi}{6}j - k
>$$

---
#matematik #multivariablemath
