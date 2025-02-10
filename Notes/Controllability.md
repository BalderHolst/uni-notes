# Controllability
See [[Lecture 9 - State Feedback Control.pdf#page=6|slides]].

> *"When can a system be controlled to a reference."*
> *"The system can reach any position at any velocity"*

$$
x_{n} =
\underbrace{
    \begin{bmatrix}
    \Gamma & \Phi\Gamma & \cdots & \Phi^{n-1}\Gamma
    \end{bmatrix}
}_{\mathcal{C}}
\begin{bmatrix}
u_{n-1} \\
u_{n-2} \\
\vdots \\
u_{0}
\end{bmatrix}
$$
$\mathcal{C}$: Controllability Matrix
$u$: Input

A system is controllable if and **only if** the controllability matrix has [[Rank of Matrix|full rank]].

## Controllable Canonical Form
See [[Lecture 9 - State Feedback Control.pdf#page=33|slides]].

$$
\dot{z} = \hat{A}z+\hat{B}u, \quad z \in \mathbb{R^{n}},\quad u \in \mathbb{R}
$$

where
$$
\hat{A} =
\begin{bmatrix}
a^{T} \\
\hline
\begin{array}{c|c}
I_{n-1} & 0_{(n-1) \times 1}
\end{array}
\end{bmatrix}
\quad \mathrm{and} \quad
\hat{B} =
\begin{bmatrix}
1 \\
\hline
0_{(n-1)\times1}
\end{bmatrix}
$$
$a^{T}$: $\begin{bmatrix} a_{1} & a_{2} & \cdots & a_{n} \end{bmatrix}$
$I_{n-1}$: Identity matrix of size $(n-1) \times (n-1)$
$0_{(n-1)\times 1}$: Matrix of zeros

>[!Example]- Example where $n=3$
>![[Lecture 9 - State Feedback Control.pdf#page=35]]

#### Characteristic Polynomial
$$
\det(\lambda I - \hat{A}) = \lambda^{n} - a_{1}\lambda^{n-1}-\dots- a_{n}
$$
$\lambda$ is sometimes replaced with $s$.

#### Transformation to Canonical Form

>[!Warning]
>The system *must be controllable* to be representable on controllable canonical form.

>[!video]- Transformation to a canonical form
>![](https://www.youtube.com/watch?v=anlC9ackwV4)

$$
\begin{align}
\dot{x} = Ax + Bu \quad &\Leftrightarrow \quad \dot{z} = \hat{A} z + \hat{B} u \\
x = T^{-1}z \quad &\Leftrightarrow \quad z = Tx
\end{align}
$$
We can convert between the matrices like this
$$
\begin{align}
\hat{A} &= T^{-1}AT \\
\hat{B} &= T^{-1}B
\end{align}
$$

Where the controllability matrices are relates as follows
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

##### Getting the Transformation
This is the (inverse of) the transformation
$$
T^{-1} =
\begin{bmatrix}
s_{1} \\
s_{2} \\
\vdots \\
s_{n}
\end{bmatrix}
$$
Its constants can be found like this
$$
\begin{align}
s_{n} &= 
\begin{bmatrix}
0_{(n-1)\times 1} & 1
\end{bmatrix}
\, \mathcal{C}^{-1} \\
s_{n-1} &= s_{n} A \\
s_{n-2} &= s_{n-1} A \\
&\vdots \\
s_{1} &= s_{2}A
\end{align}
$$

##### Procedure for Pole Placement
1. Find transfer function representation.
$$C(sI-A)^{-1}B$$
2. Find control canonical form
$$\dot{z} = \hat{A}z + \hat{B}u$$
3. Find pole placement state feedback for control canonical form.
$$u = \hat{F}z$$
4. Find transformation matrix using controllability matrices.
$$T = \mathcal{C}_{z} \cdot \mathcal{C}_{x}^{-1}$$
5. Find state feedback for original state space system.
$$F = \hat{F}T^{-1}$$

>[!example]- General Transformation to Canonical form in three dimensions
>![[Lecture 9 - State Feedback Control.pdf#page=37]]

---
#controlsystems
