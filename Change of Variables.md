# Change of Variables
Used to get of non-constant boundaries of integrals.

We define a function to map another, more convenient, space to the original space:
$$
\int_{g(D)} f(x,y) = \int_D f(g(u,v)) \cdot ||J||
$$
$f(x,y)$: The original function
$g(x,y)$: The function in the more convenient space ($g$ must be injective)
$||J||$: The absolute value of the determinant of the [[Jacobian Matrix|jacobian]] of $g(u, v)$ at the point $(u,v)$

>[!video]- Explaination
>[What is Jacobian? | The right way of thinking derivatives and integrals](https://www.youtube.com/watch?v=wCZ1VEmVjVo&t=1165s)

## Other Coordinate Systems
It is often a good idea to translate an integral to another known coordinate system, with a known jacobian determinant. Here are some options:

- [[Polar Coordinates]]
- [[Spherical Coordinates]]
- [[Cylindrical Coordinates]]

---
#multivariablemath