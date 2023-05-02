# Jacobian Matrix
A matrix relating robot joint velocities to end-affector velocity.
$$v = J(q) \cdot \dot{q}$$
$v$: Velocity of the end-affector (cartesian space)
$J(q)$: The jacobian matrix
$\dot{q}$: Velocity of the robot in joint space

Each column tells how each joint contributes to the end-affector in cartesian coordinates.

You can also find the joint velocities from the end-affector velocity like this:
$$\dot{q} = J^{-1}(q) \cdot v$$
Note that *THE INVERSE JACOBIN MAY NOT EXIST*.

### Rank
If the [[Rang af Matrix|rank]] of the jacobian is not full, the robot can not move in one or more directions.

### Determinant
If the 

---
#kinematik 