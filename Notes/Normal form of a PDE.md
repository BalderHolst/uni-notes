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
\frac{dy}{dx} &= &-\frac{\xi_y}{\xi_x} &= &\frac{ -B + \sqrt{B^{2} - 4AC} }{ 2A } \\
\frac{dy}{dx} &= &-\frac{\eta_y}{\eta_x} &= &\frac{ -B - \sqrt{B^{2} - 4AC} }{ 2A }
\end{cases}
$$
**Parabolic**:
$$
\frac{dy}{dx} = \frac{B}{2A}
$$
**Elliptic**:
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
A *second transformation is done* after finding  $\xi(x, y) = c_{1}$ and $\eta(x,y) = c_{2}$:
$$
\begin{cases}
\alpha = \frac{\xi + \eta}{2} \\
\beta = \frac{\xi - \eta}{2i}
\end{cases}
$$

#### 5. Write the canonical equation (normal form)!
$$\bar{A}u_{\xi\xi} + \bar{B}u_{\xi\eta} + \bar{C}_{\eta\eta} + \bar{D}u_{\xi} + \bar{E}u_{\eta} + \bar{F}u = \bar{G}$$
where
$$
\begin{cases}
\bar{A} &= A\xi_{x}^{2} + B\xi_{x}\xi_{y} + C\xi_{y}^{2} \\
\bar{B} &= 2A\xi_{x}\eta_{x} + B(\xi_{x}\eta_{y} + \xi_{y}\eta_{x}) + 2C\xi_{y}\eta_{x} \\
\bar{C} &= A\eta_{x}^{2} + B\eta_{x}\eta_{y} + C\eta_{y}^{2}\\
\bar{D} &= A \xi_{xx} + B\xi_{xy} + C\xi_{yy} + D\xi_{x} + E\xi_{y}\ \\
\bar{E} &= A \eta_{xx} + B\eta_{xy} + C\eta_{yy} + D\eta_{x} + E\eta_{y}\ \\
\bar{F} &= F \\
\bar{G} &= G
\end{cases}
$$

---
#matematik