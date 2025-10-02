# Line Integrals
Integrate a three-dimensional function along a curve.
$$
\int_{t=a}^{t=b}f(x(t),y(t)) 
\mathrm{dS}
$$
$$
\mathrm{dS} = \sqrt{
	\left(\frac{\partial x}{\partial t}\right)^{2}+
	\left(\frac{\partial y}{\partial t}\right)^2
} \mathrm{dt}
$$
>[!example]- Examples
>[[lektion6.pdf#page=4]]
>[[lektion6.pdf#page=5]]

## With Conservative Fields

Let $C$ be a smooth curve parameterized by $\vec{r}(t)$ from $\vec{r}(a) = A$ to $\vec{r}(b) = B$ for continuous $\mathbf{F} = \nabla f$ ($\mathbf{F}$ is [[Vector Fields#Conservative Fields|conservative]]).
$$
\oint_{C} \mathbf{F} \cdot d\vec{r} = f(B) - f(A)
$$

>[!video]- Explaination
>![](https://www.youtube.com/watch?v=we88mTXj6Yc)

## Line Length


#### See also
- [[Green's Theorem]]



---
#matematik #multivariablemath
