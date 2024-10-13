# Eigendecomposition

A *square matrix* $A$ can a be factored into
$$
A = PDP^{-1}, \quad P \in \mathbb{R}^{n \times n}
$$
$D$: A diagonal matrix containing the eigen-values of $A$.

### Calculation
1. Calculate the eigen values of $A$ and construct $D$
$$
D = \begin{bmatrix}
\lambda_{1} & 0 & \cdots & 0 \\
0 & \lambda_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & 0 \\
0 & 0 & 0 & \lambda_{n}
\end{bmatrix}
$$
2. Calculate eigen vectors of $A$ to construct $P$
$$
P = \begin{bmatrix}
v_{1}, v_{2}, \dots, v_{n}
\end{bmatrix}
$$


---
#linearalgebra 