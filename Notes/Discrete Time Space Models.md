---
created: 2026-09-28
---
# Discrete Time Space Models
See [[Lecture 1 - Slides.pdf#page=53|slides]].

Instead of writing a [[Difference Equations|difference equation]] we create an internal model to create a discrete state space model.

**EQUATION 1**: How are the states developing over time?
**EQUATION 2**: How is the output depending of state an control inputs?
$$
\begin{align}
x_{k+1} &= \Phi x_{k} + \Gamma u_{k} \\
y_{k} &= Cx_{k} + Du_{k}
\end{align}
$$
$k$: Current sample index
$x_{k}$: Current state
$x_{k+1}$: Next state
$y_{k}$: Current Output
$\Phi$: State transition matrix
$\Gamma$: Input matrix
$C$: Output matrix
$D$: Feedthrough

### Stability
See [[Lecture 2 - Stability Analysis.pdf#page=63|slides]].

## Procedure
1. Develop relevant differential equations from the given system
2. Identify (or select) state variables
**Hint:** Variables are the ones with derivatives!
3. Organize your D.E.'s so that they are in the canonical forms.

### Poles
Poles exist where
$$
|zI - A| = 0
$$
The poles of $H(z)$ (equivalent transfer function) are the same as the eigenvalues of $A$. If $A$ is $n \times n$, then $n$ poles exist.

### State Transformation
"old state": $x_{k}$
"new state": $z_{k}$

This is simple as long as there is a *linear relationship* between $x_{k}$ and $z_{k}$.

$$
x_{k} \rightarrow E\ z_{k}
\quad
\Rightarrow
\quad
z_{k} = E^{-1}\ x_{k}
$$

We can plug this into the state space model equaitons
$$
\begin{align}
&\begin{cases}
x_{k+1} &= \Phi x_{k} + \Gamma u_{k} \\
y_{k} &= Cx_{k} + Du_{k}
\end{cases} \\
\Rightarrow \quad
&\begin{cases}
Ez_{k+1} &= \Phi Ez_{k} + \Gamma u_{k} \\
y_{k} &= CEz_{k} + Du_{k}
\end{cases} \\
\Rightarrow \quad
&\begin{cases}
z_{k+1} &= E^{-1} \Phi Ez_{k} + E^{-1} \Gamma u_{k} \\
y_{k} &= CEz_{k} + Du_{k}
\end{cases}
\end{align}
$$


---
#controlsystems
