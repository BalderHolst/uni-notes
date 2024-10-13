# Singular Value Decomposition (SVD)
A generalized [[eigendecomposition]] which works for non-square matrixes.

$$
A = U \Sigma V^{T} =
\begin{bmatrix}
u_1 & \dots & u_n
\end{bmatrix}
\begin{bmatrix}
\sigma_1 & \cdots & 0 \\
\vdots & \ddots & 0 \\
0 & 0 & \sigma_n
\end{bmatrix}
\begin{bmatrix}
v_{1}^{T} \\
\vdots    \\
v_{n}^{T} \\
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

---

## Calculating
1. Find $P$ and $\Sigma^T\Sigma$ with [[eigendecomposition]] of $A^TA$.

Do eigendecomposition of $A^TA$ where $D = \Sigma^T\Sigma$ and $P=V$ to find $V$ and $\Sigma^{T}\Sigma$.

>[!tip]- Why?
>$$
>A^{T}A = V\Sigma^{T} \cancel{U^{T}} \cdot \cancel U\Sigma V^{T} =V\Sigma^{T}\Sigma V^T = PDP^{-1}
>$$

2. Find $\Sigma$
$$
\Sigma^{T}\Sigma = \begin{bmatrix}
\lambda_1 & \cdots & 0      \\
\vdots    & \ddots & \vdots \\
0         & \cdots & \lambda_n
\end{bmatrix} \Rightarrow
\Sigma = \begin{bmatrix}
\sqrt{\lambda_1} & \cdots & 0      \\
\vdots    & \ddots & \vdots \\
0         & \cdots & \sqrt{\lambda_n}
\end{bmatrix} = \begin{bmatrix}
\sigma_1 & \cdots & 0      \\
\vdots    & \ddots & \vdots \\
0         & \cdots & \sigma_n
\end{bmatrix}
$$

3. Find eigenvectors of $A^TA$. $U$ is the eigen vector matrix of these vectors.
$$
U = \begin{bmatrix}
u_1, u_2, \dots, u_m
\end{bmatrix}
$$

4. Write the SVD
$$A = U\Sigma V^T$$

---
#linearalgebra
