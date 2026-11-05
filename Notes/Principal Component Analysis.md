---
created: 2026-11-04
tags:
  - statistics
slides:
  - "[[Lessons/Semester 7/statistics/Lektion 8 slides.pdf]]"
---

## Principal Component Analysis - PCA
We find new axis for the dataset calls $\mathrm{PC}_{i}$. They are ordered from most to least important for describing the data. $\mathrm{PC}$s that do not explain much of the variation in the data may be removed to *compress the model* without too much loss.

![[Pasted image 20261104125827.png|500]]

- Decorrelation of variables
- Lossy compression
- DImension reduction

#### IDEA
Define new variables (PSs - Princibal Components) as *linear combinations* of the original variables.

We will do it in a way where:
- PCs are uncorrelated
- The variance if PCs is maximized

#### PROBLEM

We define a PC
$$
\begin{align}
\mathrm{PC}_{1} &:= a_{11}X_{1} + a_{12}X_{2} + \dots + a_{1p}X_{p} = a_{1}^{T}Xs \\
&\mathrm{where}\ \mathbb{V}[PC_{1}] = a_{1}^{T} \Sigma a_{1}\ \mathrm{is\ maximized}\ \land\ ||a_{1}|| = 1
\end{align}
$$
and another
$$
\mathrm{PC_{2}} := a_{2}^{T} X, \quad \mathrm{where}\ \mathbb{V}[PC_{2}] = a_{2}^{T} \Sigma a_{2}\ \mathrm{is\ maximized}\ \land\ ||a_{2}|| = 1
$$
and the covariance between them should be 
$$
\mathbf{Cov}(\mathrm{PC}_{1}, \mathrm{PC}_{2}) = 0
$$
When we define a new PC, it should be uncorrelated with all previous ones.

$$
\begin{align}
\mathrm{PC}_{p} := a_{p}^{T}X
\mathrm{PC_{p}} := a_{p}^{T} X, \quad \mathrm{where}\ &\mathbb{V}[PC_{p}] = a_{p}^{T} \Sigma a_{p}\ \mathrm{is\ maximized}\\
&\mathrm{and} \ ||a_{p}|| = 1 \\
&\mathrm{and}\ \mathbf{Cov}(\mathrm{PC}_{p}, \mathrm{PC}_{i})\ \forall\ i \in \set{1, \dots, p-1}
\end{align}
$$

#### SOLUTION
When we maximize the variance the $a$-vectors will be found as the eigenvectors of the covariance matrix $\Sigma$.

So the problem becomes an [[Eigendecomposition|eigen vector decomposition]] problem.
$$
\Sigma\ e = \lambda \ e
$$
$e$: Eigenvectors
$\lambda$: Eigen values

$$
\begin{align}
(\lambda I - \Sigma) e &= 0, \quad e \neq 0 \\
\Rightarrow |\lambda I - \Sigma | &= 0 \to \mathrm{eigen\ values}
\end{align}
$$

With the eigenvalues, use them one at a time in the original equation to get each eigen vector.
$$
\Sigma\ e_{i} = \lambda_{i}\ e_{i} \to p\ \mathrm{eigen\ vectors}
$$

In practice **we use tools to do this**.

The covariance matrix can then be described as
$$
\Sigma = E\Lambda E^{T} = \sum_{i=1}^{p} \lambda_{i} e_{i} e_{i}^{T}, \quad \mathrm{where}\
\lambda_{1} \geq \lambda_{2} \geq \dots \lambda_{p} \geq 0
$$

#### TERMONOLOGY
- "Loadings": Eigenvector values. How much is each PC depending on each original value.
- "Scores": $\mathrm{PC}_{ij} = e_{i}^{T}X_{j}$ and $\mathbb{V}[\mathrm{PC}_{i}] = \lambda_{i}$
- "Variance explained by $\mathrm{PC}_{i}$": How much variance is explained by this variance, as opposed to the sum of them all. $= \frac{\lambda_{i}}{\sum_{i=1}^{p} \lambda_{j}} \cdot  100\%$

PCs are uncorrelated
$$
\mathbf{Cov}[\mathrm{PC}_{i}, \mathrm{PC_{k}}] =
\begin{cases}
\Sigma & i=k \\
0      & i \neq k
\end{cases}
$$