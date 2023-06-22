# Velocity Curves
Ways of getting from one point to another in a smooth and stylish fashion!

## Trapezoidal Velocity Profiles
A simple velocity profile. It does however result in high [[jerk]] which can result in wear on the motors. Therefore, [[#Cubic Polynomial Profiles]] are usually used instead.
![[Pasted image 20230622100202.png|300]]

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
![[Pasted image 20230622101336.png|300]]

##### Finding the constants
Here we calculate the velocity profile in *joint space*.
$$
\begin{cases}
q(0) &= q_{start} = d\\
\dot{q}(0) &= \dot{q}_{start} = c \\
q(T) &= q_{end} = aT^{3} + bT^{2} 0 
\end{cases}
$$


---
#kinematics 