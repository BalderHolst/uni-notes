# Jacobian Matrix
A matrix relating robot joint velocities to end-affector velocity.
$$v = J(q) \cdot \dot{q}$$
$v$: Velocity of the end-affector (cartesian space)
$J(q)$: The jacobian matrix, where $q$ is the current joint configuration
$\dot{q}$: Velocity of the robot in joint space

Each column tells how each joint contributes to the end-affector in cartesian coordinates.

You can also find the joint velocities from the end-affector velocity like this:
$$\dot{q} = J^{-1}(q) \cdot v$$
Note that *THE INVERSE JACOBIN MAY NOT EXIST*. This can be because the columns are linearly dependent (not [[Rang af Matrix#Full Rank|full rank]]), or that the jacobian is not square.

### If the Jacobian is not square
$$\dot{q} = \alpha J^{T}\dot{x}, \s \alpha>0$$
True for **very** small steps.

## Rank and Determinant
If the [[Rang af Matrix|rank]] of the jacobian is not full, the robot can not move in one or more directions.

### Singularities
There is no [[Den Inverse af en Matrix|inverse]] when the determinant is $0$.

##### For SQUARE Jacobians (non-redundant)
At a [[Singularities|singularity]], the **[[Determinanen for Matricer|determinant]] of the jacobian will be *zero***. Therefore, the inverse jacobian will not exist.
$$\mu = \det(J), \s 
\begin{cases} 
\mu \approx 0 \Rightarrow \text{close}\\
\mu > 0 \Rightarrow \text{not close}\\
\end{cases}$$

##### For NON-SQUARE Jacobinas
$$\mu = \sqrt{\det(JJ^{T)}}, \s 
\begin{cases} 
\mu \approx 0 \Rightarrow \text{close}\\
\mu > 0 \Rightarrow \text{not close}\\
\end{cases}$$

#### Manipulability Ellipsoid
Shows how the end-affector can move.
$$\dot{x}A^{-1}\dot{x} = 1, \s A = JJ^{T}$$

The axes $a$, $b$, and $c$ of the ellipsoid can be related to the [[Egenvaerdier og Egenvektorer|eigen-values]] and eigen-vectors of $A$.
![[manipulability-ellipsoid.png]]

>[!example]- 2D Example
>![[2D-manipulibility-example.png]]

##### Measure #1
$$\mu = \sqrt{\det(JJ^{T)}} = \sqrt{\det(A)}, \s 
\begin{cases} 
\mu \approx 0 \Rightarrow \text{close}\\
\mu > 0 \Rightarrow \text{not close}\\
\end{cases}$$

##### Measure #2
$$
\mu = {\sqrt{\lambda_{\text{max}}(A)} \over \sqrt{\lambda_{\text{min}}(A)}} \geq 1, \s \mu >= 1, \s
$$
$\lambda_{max}$: The largest eigen value
$\lambda_{min}$: The smalest eigen value
$$
\begin{cases} 
\mu \text{ is large} &\Rightarrow \text{close to singularity}\\
\mu \text{ is small} &\Rightarrow \text{far from singularity}\\
\mu = 1 &\Rightarrow \text{Isotropic}\\
\end{cases}
$$

##### Measure #3 (Condition number)
$$\mu = {\lambda_{\text{max}}(A) \over \lambda_{\text{min}}(A)} \geq 1, \s 
\begin{cases} 
\mu \text{ is large} \Rightarrow \text{close to singularity}\\
\mu \text{ is small} \Rightarrow \text{far from singularity}\\
\end{cases}$$

---
#kinematics #matricer
