# Normal form of a PDE
See [video](https://www.youtube.com/watch?v=x2zrBDBk2ps).

See [nice PDF](https://faculty.uml.edu//spennell/Teaching/PDE/classification.pdf).

>[!video]- Normal form of *hyperbolic* PDE
>![](https://www.youtube.com/watch?v=-iI8p1CtifU)

#### 1. Compare with the standard PDE
$$Au_{xx} + Bu_{xy} + C_{yy} + Du_{x} + Eu_{y} + Fu = G$$
Obtain constant values

#### 2. Classify with Discriminant

$$d = B^{2}-4AC$$


Classify PDE:

| Discriminant | PDE type   |
| ------------ | ---------- |
| $d>0$        | Hyperbolic |
| $d=0$        | Parabolic  |
| $d<0$        | Elliptic   |

#### 3. Find New Variables
We solve the following equation. Steps are different depending on the type of PDE.
$$A\lambda^{2} - B\lambda + C = 0$$

**Hyperbolic**:

The equation results in two solutions: $\lambda_1$ and $\lambda_2$.

Then solve the following solutions to obtain $c_1$ and $c_2$.
$$
\begin{cases}
\frac{dy}{dx} = \lambda_1 \\
\frac{dy}{dx} = \lambda_2
\end{cases}
\Rightarrow
\begin{cases}
\int\frac{dy}{dx} = \int\lambda_1 \\
\int\frac{dy}{dx} = \int\lambda_2
\end{cases}
\Rightarrow
\begin{cases}
\phi(x, y) = c_1 \\
\psi(x, y) = c_2
\end{cases}
$$

Now assign to $\xi$ and $\eta$.

$$
\begin{cases}
\xi = \phi(x, y) \\
\eta = \psi(x, y) \\
\end{cases}
$$

**Parabolic**:

The is the ONE solution for the equation.
$$
\frac{dy}{dx} = \frac{B}{2A}
\Rightarrow 
\int\frac{dy}{dx} = \int\frac{B}{2A}
\Rightarrow 
\psi(x,y) = c_{1}
$$

$\xi = \psi(x,y)$ and $\eta$ will be chosen such that is will not be parallel to the $\xi$ coordinate; $\eta$ is chosen such that *the [[Jacobian Matrix for Robotics|jacobian]] of the transformation is not zero*.



**Elliptic**:
$$
\begin{cases}
\frac{dy}{dx} &= &\frac{ B + \sqrt{B^{2} - 4AC} }{ 2A } \\
\frac{dy}{dx} &= &\frac{ B - \sqrt{B^{2} - 4AC} }{ 2A }
\end{cases}
$$

A *second transformation is done* after finding  $\xi(x, y) = c_{1}$ and $\eta(x,y) = c_{2}$:
$$
\begin{cases}
\alpha = \frac{\xi + \eta}{2} \\
\beta = \frac{\xi - \eta}{2i}
\end{cases}
$$
#### Find the needed derivatives
Only calculate the ones that are part of the original PDE.

$$u_{x} = \frac{\partial u}{\partial \xi} \frac{\partial \xi}{\partial x} + \frac{\partial u}{\partial \eta} \frac{\partial \eta}{\partial x} $$


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
