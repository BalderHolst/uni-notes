# Controllability
See [[Lecture 9 - State Feedback Control.pdf#page=6|slides]].

> *"When can a system be controlled to a reference."*

$$
x_{n} =
\underbrace{
    \begin{bmatrix}
    B & AB & \cdots & A^{n-1}B
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
T 
\underbrace{\begin{bmatrix}
B & AB & A^{2}B & \cdots & A^{n-1}B
\end{bmatrix}}
_{M_{cx}}
\quad = \quad
\underbrace{\begin{bmatrix}
\hat{B} & \hat{A}\hat{B} & \hat{A}^{2}\hat{B} & \cdots & \hat{A}^{n-1}\hat{B}
\end{bmatrix}}
_{M_{cz}}
$$

##### Procedure for Pole Placement
1. Find transfer function representation.
$$C(sI-A)^{-1}B$$
2. Find control canonical form
$$\dot{z} = \hat{A}z + \hat{B}u$$
3. Find pole placement state feedback for control canonical form.
$$u = -\hat{K}z$$
4. Find transformation matrix using controllability matrices.
$$T = M_{cz} \cdot M_{cx}^{-1}$$
5. Find state feedback for original state space system.
$$K = \hat{K}T$$

---
#controlsystems