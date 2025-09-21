# Velocity Curves
Ways of getting from one point to another in a smooth and stylish fashion!

[[Lecture 11 - Jacobian Singularities Numerical IK and Trajectory Generation.pdf#page=18|slides]]

>[!example]- Trapezoidal Velocity Profiles
>A simple velocity profile. It does however result in high [[jerk]] which can result in wear on the motors. Therefore, [[#Cubic Polynomial Profiles]] are usually used instead.
>![[Velocity-Curves.png|Pasted image 20230622100202.png]]

## Cubic Polynomial Profiles
$$
\begin{align}
q(t) &= at^{3} + bt^{2} + ct + d \\
\dot{q}(t) &= 3at^{2} + 2bt + c \\
\ddot{q}(t) &= 6at + 2b \\
\dddot{q}(t)  &= 6a
\end{align}
$$
Because [[jerk]] is constant, the motion will be smooth, and the motor will therefore last longer. Higher order polynomials can also be used.
![[Velocity-Curves-Cubic-Polynomial-Profiles.png|300]]

##### Finding the constants
Here we calculate the velocity profile in *joint space*.
$$
\begin{cases}
q(0) &= q_{start} = d\\
\dot{q}(0) &= \dot{q}_{start} = c \\
q(T) &= q_{end} = aT^{3} + bT^{2} + cT + d \\
\dot{q}(T) &= \dot{q}_{end} = 3aT^{2} + 2bT + c
\end{cases}
$$
$T$: The time when the second point is reached.

##### For all the robot joints
Simply convert all parameters to vectors

$$
\newcommand{\vv}[1]{
\begin{bmatrix} #1_{1} \\ \vdots \\ #1_{n} \end{bmatrix}
}
\newcommand{\vf}[1]{
\begin{bmatrix} #1_{1}(t) \\ \vdots \\ #1_{n}(t) \end{bmatrix}
}
\vf{q} = \vv{a} \cdot t^{3} + \vv{b} \cdot t^{2} + \vv{c} \cdot t + \vv{d}
$$

---
#kinematics 
