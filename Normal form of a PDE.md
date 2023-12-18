# Normal form of a PDE
See [video](https://www.youtube.com/watch?v=x2zrBDBk2ps).

#### 1. Compare with the standard PDE
$$Au_{xx} + Bu_{xy} + C_{yy} + Du_{x} + Eu_{y} + Fu = G$$
Obtain constant values

#### 2. Classify with Discriminant

Classify PDE:

| Discriminant | PDE type |
| ------------ | --- |
| $B^{2}-4AC>0$  | Hyperbolic    |
| $B^{2}-4AC=0$  | Parabolic    |
| $B^{2}-4AC<0$  | Elliptic    |

#### 3. Find Characteristic Equation (normal form)

**Hyperbolic**:
$$
\begin{cases}
\frac{dy}{dx} &= &\frac{\xi(y)}{\xi(x)} &= &\frac{ -B + \sqrt{B^{2} - 4AC} }{ 2A } \\
\frac{dy}{dx} &= &\frac{\eta(y)}{\eta(x)} &= &\frac{ -B - \sqrt{B^{2} - 4AC} }{ 2A }
\end{cases}
$$
**Parabolic**:
$$
\frac{dy}{dx} = \frac{B}{2A}
$$
**Hyperbolic**:
$$
\begin{cases}
\frac{dy}{dx} &= &\frac{ B + \sqrt{B^{2} - 4AC} }{ 2A } \\
\frac{dy}{dx} &= &\frac{ B - \sqrt{B^{2} - 4AC} }{ 2A }
\end{cases}
$$

#### 4. Integrate Characteristic Equations
We are trying to obtain the following values:
$$\xi(x, y) = c_{1}, \s \eta(x,y) = c_{2}$$

This is done differently depending on the type of PDE.

**Hyperbolic**:
$$\xi(x, y) = c_{1}, \s \eta(x,y) = c_{2}$$
**Parabolic**:
$\xi(x, y) = c_{1}$ and $\eta$ will be chosen such that is will not be parallel to the $\xi$ coordinate; $\eta$ is chosen such that *the [[Jacobian Matrix|jacobian]] of the transformation is not zero*.


**Elliptic**:
A *second transformation is done* after finding  $\xi(x, y) = c_{1}$$s \eta(x,y) = c_{2}$


---
#matematik