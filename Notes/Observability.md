---
created: 2026-11-16
tags:
  - controlsystems
---

# Observability
A system is observable if the knowlege og the output $y$, is sufficient to reconstruct the whole state $x$.

See [[Lecture 10 - Observers.pdf#page=6|slides]].

$$
\mathcal{O} = 
\begin{bmatrix}
C \\
CA \\
CA^{2}\\
\vdots \\
C A^{n-1}
\end{bmatrix}
$$
$\mathcal{O}$: Observability matrix
$A$: A matrix from [[State Space Models|state space model]].
$C$: C matrix from [[State Space Models|state space model]].
$n$: Number of states

If a state $x$ exists so that $y$ is always $0$, and $x \neq 0$, then the system is not observable.

We can estimate the state **if the observability matrix is invertible** $\mathrm{det}(\mathcal{O}) \neq 0$.

$$
\hat{x}(t) = \mathcal{O}^{-1} \bar{y}(t)
$$
$\bar{y}(t)$: Measured output
$\hat{x}(t)$: Estimated state vector

Dual of [[Controllability]]. 