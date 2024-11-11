# Multivariate Random Variables
See [[lecture7.pdf#page=24|slides]].

$$
X =
\begin{bmatrix}
X_{1} \\ \vdots \\ X_{n}
\end{bmatrix}
\quad \quad
\mu =
\begin{bmatrix}
\mu_{1} \\ \vdots \\ \mu_{n}
\end{bmatrix} =
\begin{bmatrix}
\mathbb{E}({1}) \\ \vdots \\ \mathbb{E}({n})
\end{bmatrix}
$$

#### Expected Value
$$
\begin{align}
\mathbb{E}(a^{T} X) &= a^{T}\mu      \\
\mathbb{E}(AX) &= A\mu               \\
\end{align}
$$


#### Variance

**Covariance Matrix:**
$$
\mathbb{V}(X) =
\begin{bmatrix}
\mathbb{V}(X_{1}) & \mathrm{Cov}(X_1, X_2) & \cdots & \mathrm{Cov}(X_1, X_k) \\
\mathrm{Cov}(X_2, X_1) & \mathbb{V}(X_{2}) & \cdots & \mathrm{Cov}(X_2, X_k) \\
\vdots & \vdots & \ddots & \vdots \\
\mathrm{Cov}(X_k, X_1) & \mathrm{Cov}(X_k, X_2) & \cdots & \mathbb{V}(X_k)
\end{bmatrix}
$$


**Properties:**

$$
\begin{align}
\mathbb{V}(a^{T} X) &= a^{T}\Sigma a \\
\mathbb{V}(AX) &= A\Sigma A^T
\end{align}
$$

---
#statistics
