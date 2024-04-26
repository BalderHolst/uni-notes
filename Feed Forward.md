# Feed Forward
See [[Lecture 11 - Integral Control.pdf#page=31|slides]].
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
where $\tilde{}$


---
#controlsystems