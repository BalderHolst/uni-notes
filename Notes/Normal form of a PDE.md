# Normal form of a PDE
See [video](https://www.youtube.com/watch?v=x2zrBDBk2ps).

See [nice PDF](https://faculty.uml.edu//spennell/Teaching/PDE/classification.pdf).

>[!video]- Normal form of *hyperbolic* PDE
>![](https://www.youtube.com/watch?v=-iI8p1CtifU&list=PLZSrM0Ajr9iTk-vzVEyjJkKL2T5ZEeCgz&index=9)

>[!video]- Normal form of *elliptic* PDE
>![](https://www.youtube.com/watch?v=2uWh9y5Zuw0&list=PLZSrM0Ajr9iTk-vzVEyjJkKL2T5ZEeCgz&index=10)

>[!tip]- A nice lille overview
>![[caracteristic_examples.png]]

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
\int dy = \int\lambda_{1} dx \\
\int dy = \int\lambda_{2} dx
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

There is the ONE solution  for the equation.
$$\lambda = \frac{B}{2A}$$

Integration to find $c_{1}$.
$$
\frac{dy}{dx} = \lambda
\Rightarrow 
\int dy = \int \lambda\ dx
\Rightarrow 
\psi(x,y) = c_{1}
$$

$\xi = \psi(x,y)$ and $\eta$ will be chosen such that is will not be parallel to the $\xi$ coordinate; $\eta$ is chosen such that *the determinamt of the [[Jacobian Matrix for Robotics|jacobian]] of the transformation is not zero*.

$$
|J(x,y)| = 
\begin{vmatrix}
\xi_{x} & \xi_{y} \\
\eta_{x} & \eta_{y}
\end{vmatrix}
\neq 0
$$

**Elliptic**:
The solution to the equation will be given by $\lambda_{1} + i\lambda_{2}$ and  $\lambda_{1} - i\lambda_{2}$.

We integrate them to get $c_{1}$ and $c_{2}$:
$$
\begin{cases}
\frac{dy}{dx} = \lambda_{1} +i\lambda_{2} \\
\frac{dy}{dx} = \lambda_{1} -i\lambda_{2}
\end{cases}
\Rightarrow
\begin{cases}
\int dy = (\lambda_{1} +i\lambda_{2}) dx \\
\int dx = (\lambda_{1} -i\lambda_{2}) dx
\end{cases}
\Rightarrow
\begin{cases}
c_{1} = f_{1}(x,y) + if_{2}(x,y) \\
c_{2} = f_{2}(x,y) - if_{2}(x,y)
\end{cases}
$$

We define $\xi$ and $\eta$ like this
$$
\begin{cases}
\xi  = f_{1}(x,y) + if_{2}(x,y) \\
\eta = f_{1}(x,y) - if_{2}(x,y)
\end{cases}
$$


A *second transformation is done* after finding  $\xi(x, y) = c_{1}$ and $\eta(x,y) = c_{2}$:
$$
\begin{cases}
\alpha = \frac{\xi + \eta}{2} \\
\beta = \frac{\xi - \eta}{2i}
\end{cases}
\Rightarrow
\begin{cases}
\alpha = f_{1}(x,y) \\
\beta = f_{2}(x,y)
\end{cases}
$$

Use $\alpha$ and $\beta$ instead of $\xi$ and $\eta$ in the following steps.

#### 4. Find the needed derivatives
Only calculate the ones that are part of the original PDE.

Note that *derivatives of $\xi$ and $\eta$ are **constant**.

$$
\begin{align}
u_{x} &= u_{\xi}\xi_{x} + u_{\eta}\eta_{x} \\
u_{y} &= u_{\xi}\xi_{y} + u_{\eta}\eta_{y} \\

u_{xx} &= u_{\xi\xi}(\xi_{x})^{2} + 2u_{\xi\eta}\xi_{x}\eta_{x} + u_{\eta\eta}(\eta_{x})^{2} + u_{\xi}\xi_{xx} + u_{\eta}\eta_{xx} \\

u_{yy} &= u_{\xi\xi}(\xi_{y})^{2} + 2u_{\xi\eta}\xi_{y}\eta_{y} + u_{\eta\eta}(\eta_{y})^{2} + u_{\xi}\xi_{yy} + u_{\eta}\eta_{yy} \\

u_{xy} &= u_{\xi\xi}\xi_{x}\xi_{y} + u_{\eta\eta}\eta_{x}\eta_{y} + u_{\xi}\xi_{xy} + u_{\eta}\eta_{xy} + u_{\xi\eta}(\xi_{x}\eta_y + \xi_y\eta_x)

\end{align}
$$

#### 5. Replace the derivatives
Replace the derivatives of $u$ with the newly calculated ones.

The resulting equation is the normal form of the PDE.

**Hyperbolic**:
$$u_{\xi\eta} = \Phi(\xi, \eta,u,u_\xi,u_\eta)$$
**Elliptic**:
$$u_{\alpha\alpha} + u_{\beta\beta} = \Phi(\alpha, \beta, u, u_{\alpha}, u_{\beta})$$

#### 6. Solve PDE

#### 7. Replace Variables
Replace $\xi$ and $\eta$ with functions of $x$ and $y$.

---
#matematik #multivariablemath
