# Feed Forward
See [[Lecture 11 - Integral Control.pdf#page=31|slides]].

*Placing zeros* and thereby increasing [[Signal Bandwidth|bandwidth]].

![[Pasted image 20240426092506.png|center|500]]

$$
\begin{align}
\dot{x} &= Ax + B(F\hat{x} + Nr) \\
y &= Cx
\end{align}
$$

Zeros for the open loop system is given by
$$
\det\left(
\begin{bmatrix}
A-zI & B \\
C & 0
\end{bmatrix}
\right) = 0
$$
Further zeros added by feed forward are given by
$$
\det(A + BF + LV - \tilde{M}F - zI) = 0
$$
where $\tilde{M} = MN^{-1}$.

#### Zero Assignment Procedure
See [[Lecture 11 - Integral Control.pdf#page=46|slides]].

1. Design $\tilde{M}$ assigning zeros close to the cut-off frequency of the Bode plot, such that the "horizontal" part is extended.
2. Compute $N$ such that the DC-value of the transfer function from $r$ to $y$ is unity:
$$
N = -(C_{\mathrm{cl}}A_{\mathrm{cl}}^{-1}\tilde{B}_{\mathrm{cl}})^{-1}
$$
where
$$
\begin{align}

A_\mathrm{cl} &=
\begin{bmatrix}
A & BF \\
-LC & A+BF+LC
\end{bmatrix} \\

\tilde{B}_\mathrm{cl} &=
\begin{bmatrix}
B \\
\tilde{M}
\end{bmatrix} \\

C_\mathrm{cl} &=
\begin{bmatrix}
C & 0
\end{bmatrix}

\end{align}
$$

---
#controlsystems