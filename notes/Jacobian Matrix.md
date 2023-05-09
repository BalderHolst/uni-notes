# Jacobian Matrix
A matrix relating robot joint velocities to end-affector velocity.
$$v = J(q) \cdot \dot{q}$$
$v$: Velocity of the end-affector (cartesian space)
$J(q)$: The jacobian matrix, where $q$ is the current joint configuration
$\dot{q}$: Velocity of the robot in joint space

Each column tells how each joint contributes to the end-affector in cartesian coordinates.

You can also find the joint velocities from the end-affector velocity like this:
$$\dot{q} = J^{-1}(q) \cdot v$$
Note that *THE INVERSE JACOBIN MAY NOT EXIST*.

### If the Jacobian is not square
$$\dot{q} = \alpha J^{T}\dot{x}, \s \alpha>0$$
True for **very** small steps.

## Rank and Determinant
If the [[Rang af Matrix|rank]] of the jacobian is not full, the robot can not move in one or more directions.

### Singularities

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
$$\dot{x}A^{-1}\dot{x} = 1, \s A = JJ$$

The axes $a$, $b$, and $c$ of the ellipsoid can be related to the eigen-values and eigen-vectors of $A$.
![[Pasted image 20230509092020.png]]

>[!example]- 2D Example
>![[Pasted image 20230509092110.png]]

##### Measure #1
$$\mu = \sqrt{\det(JJ^{T)}} = \det(A), \s 
\begin{cases} 
\mu \approx 0 \Rightarrow \text{close}\\
\mu > 0 \Rightarrow \text{not close}\\
\end{cases}$$

##### Measure #2


##### Measure #3

---
#kinematics 
#matricer 