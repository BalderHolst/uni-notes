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

## Transformation to Canonical Form

>[!video]- Transformation to a canonical form
>![](https://www.youtube.com/watch?v=anlC9ackwV4)

$$
\begin{align}
\dot{x} = Ax + Bu \quad &\Leftrightarrow \quad \dot{z} = \hat{A} z + \hat{B} u \\
x = T^{-1}z \quad &\Leftrightarrow \quad z = Tx
\end{align}
$$
Where the controlabillity matrices are relates as follows
$$

$$

---
#controlsystems