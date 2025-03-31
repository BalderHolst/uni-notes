# Sliding Mode Control
See [[Lecture 8 - Sliding Mode Control.pdf|slides]].

> Are we to the **left** of the target? *go right*
> Are we to the **right** of the target? *go left*


This is our system:
$$
\dot{x} =
\begin{bmatrix}
\dot{q} \\
-B^{-1}(q)(C(q,\dot{q})\dot{q} + g(q)) + B^{-1}(q) \tau
\end{bmatrix}
$$

We begin by constraining the motion of the system to a surface
$$
a_{1}x_{1} + x_{2} = 0 
\quad\Rightarrow\quad
\dot{x}_{1} = -a
$$




---
#underactuated-robots