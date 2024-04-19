# Observability
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
$\mathcal{O}$: Observability matric
$A$: A matrix from [[State Space Models|state space model]].
$C$: C matrix from [[State Space Models|state space model]].

If a state $x$ exists so that $y$ is always $0$, and $x \neq 0$, then the system is not observable.

The system must have a [[Rang af Matrix|full rank]] observability matrix to be observable.

Dual of [[Controllability]].

### Full Order Observer
See [[Lecture 10 - Observers.pdf#page=28|slides]].

Create an estimate of the system and feed the error from the real system into the estimate system.

![[Pasted image 20240419084942.png]]

$$
\dot{e} = (A + LC) e
$$
$(A + LC)$'s [[Egenværdier og Egenvektorer|eigen values]] must be in the left half plane. This is also the general criteria for stability of a system. Choosing an $L$ to make the system stable is *only possible if the system is observable*.

$L$ can be found matlab using the `place` function.

### Observer Based Control
Feedback based on estimated state instead of real syste

![[Pasted image 20240419091927.png]]

---
#controlsystems