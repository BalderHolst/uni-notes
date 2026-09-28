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

---
#controlsystems