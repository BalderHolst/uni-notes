# Linear State Space Models

The system is designated as
$$
\dot{x} = Ax + Bu
$$


| Variable  | Type           | Space                    |
| --------- | -------------- | ------------------------ |
| $\dot{x}$ | Dynamic matrix | $\mathbb{R}^n$           |
| $x$       | State vector   | $\mathbb{R}^n$           |
| $u$       | Input vector   | $\mathbb{R}^m$           |
| $A$       | System matrix  | $\mathbb{R}^{n\times n}$ |
| $B$       | Control matrix | $\mathbb{R}^{n\times m}$ |

The output os defined as
$$
y = Cx  + Du
$$

$n$: Order of the differential equation.

## Poles
$$G(s) = C (sI-A)^{-1} B + D$$
This is only possible if
$$\det(sI-A) \neq 0$$
This is also the definition of [[Eigen values and vectors|eigen values]].

At $\det(sI-A) = 0$ the system must have a pole. Therefore, the **poles of a state space model are the eigenvalues of $A$.**

## Zeroes
See [[Lecture 2 - Stability Analysis.pdf#page=60|slides]].

Transmission zeroes are at
$$
\begin{vmatrix}
A - zI & B \\
C & D
\end{vmatrix}
= 0
$$

---
#controlsystems