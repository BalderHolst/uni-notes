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

### Rank and Determinant
If the [[Rang af Matrix|rank]] of the jacobian is not full, the robot can not move in one or more directions.

At a singularity, the determinant of the jacobian will be zero.aa Therefore, the inverse jacobian will not exist.


---
#kinematik 