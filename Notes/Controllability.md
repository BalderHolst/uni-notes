# Controllability
See [[Lecture 9 - State Feedback Control.pdf#page=6|slides]].

> *"When can a system be controlled to a reference."*

$$
x_{n} =
\underbrace{
    \begin{bmatrix}
    \Gamma & \Phi\Gamma & \dots & \Phi^{n-1}\Gamma
    \end{bmatrix}
}_{\mathrm{Controllability\ Matrix}}
\begin{bmatrix}
u_{n-1} \\
u_{n-2} \\
\vdots \\
u_{0}
\end{bmatrix}
$$

A system is controllable if and **only if** the controlability matrix has full rank.

---
#controlsystems