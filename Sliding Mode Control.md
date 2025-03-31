# Sliding Mode Control
See [[Lecture 8 - Sliding Mode Control.pdf|slides]].

> Are we to the **left** of the target? *go right*
> Are we to the **right** of the target? *go left*

**NOT MODEL BASED**... and that is a good thing!

This is our system:
$$
\dot{x} =
\begin{bmatrix}
\dot{x}_1 \\
\dot{x}_2
\end{bmatrix}
=
\begin{bmatrix}
\dot{q} \\
-B^{-1}(q)(C(q,\dot{q})\dot{q} + g(q)) + B^{-1}(q) \tau
\end{bmatrix}
$$

We begin by constraining the motion of the system to a surface

$$
s = a_{1}x_{1} + x_{2} = 0 
\quad\Rightarrow\quad
\dot{x}_{1} = -a_{1}x_{1}
$$

We want to create a controller which "pushes" to motion of the robot into this surface.
$$
u = -\beta\;\mathrm{sign}(s)
$$

Usually $\beta$ is as large as possible resulting in a "bang bang" control system.

After reaching the 

---
#underactuated-robots