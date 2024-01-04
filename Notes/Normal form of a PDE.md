# Normal form of a PDE
See [video](https://www.youtube.com/watch?v=x2zrBDBk2ps).

See [nice PDF](https://faculty.uml.edu//spennell/Teaching/PDE/classification.pdf).
 
>[!video]- Normal form of *hyperbolic* PDE
>![](https://www.youtube.com/watch?v=-iI8p1CtifU&list=PLZSrM0Ajr9iTk-vzVEyjJkKL2T5ZEeCgz&index=9)

>[!video]- Normal form of *elliptic* PDE
>![](https://www.youtube.com/watch?v=2uWh9y5Zuw0&list=PLZSrM0Ajr9iTk-vzVEyjJkKL2T5ZEeCgz&index=10)

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
#### 4. Find the needed derivatives
Only calculate the ones that are part of the original PDE.

Note that *derivatives of $\xi$ and $\eta$ are **constant**.

$$
\begin{align}
u_{x} &= u_{\xi}\xi_{x} + u_{\eta}\eta_{x} \\
u_{y} &= u_{\xi}\xi_{y} + u_{\eta}\eta_{y} \\

u_{xx} &= u_{\xi\xi}(\xi_{x})^{2} + 2_{\xi\eta}\xi_{x}\eta_{x} + u_{\eta\eta}(\eta_{x})^{2} + u_{\xi}\xi_{xx} + u_{\eta}\eta_{xx} \\

u_{yy} &= u_{\xi\xi}(\xi_{y})^{2} + 2_{\xi\eta}\xi_{y}\eta_{y} + u_{\eta\eta}(\eta_{y})^{2} + u_{\xi}\xi_{yy} + u_{\eta}\eta_{yy} \\

u_{xy} &= u_{\xi\xi}\xi_{x}\xi_{y} + u_{\eta\eta}\eta_{x}\eta_{y} + u_{\xi}\xi_{xy} + u_{\eta}\eta_{xy} + u_{\xi\eta}(\xi_{x}\eta_y + \xi_y\eta_x)

\end{align}
$$

#### 5. Replace the derivatives
Replace the derivatives of $u$ with the newly calculated ones.

The resulting equation is the normal form of the PDE.

**Hyperbolic**:
$$u_{\xi\eta} = \Phi(\xi, \eta,u,u_\xi,u_\eta)$$

---
#matematik #multivariablemath
