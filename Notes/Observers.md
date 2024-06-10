# Observers
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

The system must have a [[Rang af Matrix|full rank]] observability matrix to be observable. Dual of [[Controllability]]. 

>[!warning] Place poles to the left of system
>When choosing $L$ **MAKE SURE THAT THE POLES OF $A+LC$ ARE TO THE LEFT OF THE SYSTEM** (about seven times) this makes sure that the system has the dominant poles.

Create an estimate of the system and feed the error from the real system into the estimate system. ![[Pasted image 20240419084942.png]] $$ \dot{e} = (A + LC) e $$ $(A + LC)$'s [[Egenværdier og Egenvektorer|eigen values]] must be in the left half plane. This is also the general criteria for stability of a system. Choosing an $L$ to make the system stable is *only possible if the system is observable*. $L$ can be found matlab using the `place` function. ### Observer Based Control See [[Lecture 10 - Observers.pdf#page=71|slides]]. [[Notes/State Feedback|State feedback]] based on estimated state instead of real system state. ![[Pasted image 20240419091927.png]] ![[Pasted image 20240419093350.png]] For the observer based control to be closer to the state feedback. Place the $A+LC$ poles further to the left in the $s$-plane. --- #controlsystems