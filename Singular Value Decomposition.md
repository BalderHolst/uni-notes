# Singular Value Decomposition
A generalized [[eigendecomposition]] which works for non-square matrixes.

$$
A = U \Sigma V^{T} =
\begin{bmatrix}
a
\end{bmatrix}
$$

$$U \in \mathbb{R}^{m\times m},\quad
\Sigma \in \mathbb{R}^{m\times n},\quad
V\in \mathbb{R}^{n\times n}
$$
where $U$ and $V$ are both [[Orthogonal Matrix|orthogonal matrixes]].
$$
\begin{align}
U^{T}U&=I \\
V^{T}V&=I
\end{align}
$$
### Calculating
1. Find $P$ and $\Sigma^T\Sigma$ with [[eigendecomposition]] of $A^TA$.

Do eigendecomposition of $A^TA$ where $D = \Sigma^T\Sigma$ and $P=V$.

>[!tip]- Why?
>$$
>A^{T}A = V\Sigma^{T} \cancel{U^{T}} \cdot \cancel U\Sigma V^{T} =V\Sigma^{T}\Sigma V^T = PDP^{-1}
>$$

2. Find eigenvectors of $A^TA$. $U$ is the eigen vector matrix of these vectors.
$$
U = \begin{bmatrix}
u_1, u_2, \dots, u_m
\end{bmatrix}
$$

---
#linearalgebra
