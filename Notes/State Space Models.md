# State Space Models
See [[Lecture 1 - Slides.pdf#page=32|slides]].

The system is designated as
$$
\dot{x} = Ax + Bu
$$


| Variable  | Type           | Space          |
| --------- | -------------- | -------------- |
| $\dot{x}$ | Dynamic matrix | $\mathbb{R}^n$ |
| $x$       | State vector   | $\mathbb{R}^n$ |
| $u$       | Input vector   | $\mathbb{R}^m$ |
| $A$       | System matrix  | $\mathbb{R}^{n\times n}$ |
| $B$       | Control matrix | $\mathbb{R}^{n\times m}$ |

The output os defined as
$$
y = Cx  + Du
$$

$n$: Order of the differential equation.

### Poles
$$G(s) = C (sI-A)^{-1} B + D$$
This is only possible if
$$\det(sI-A) \neq 0$$
This is also the definition of [[Eigen values and vectors|eigen values]].

At $\det(sI-A) = 0$ the system must have a pole. Therefore, the **poles of a state space model are the eigenvalues of $A$.**

### Zeroes
See [[Lecture 2 - Stability Analysis.pdf#page=60|slides]].

Transmission zeroes are at
$$
\begin{vmatrix}
A - zI & B \\
C & D
\end{vmatrix}
= 0
$$


### Discrete Time Space Models
See [[Lecture 1 - Slides.pdf#page=53|slides]].

$$
\begin{cases}
x_{k+1} &= \Phi x_{k} + \Gamma u_{k} \\
y_{k} &= Cx_{k} + Du_{k}
\end{cases}
$$

#### Stability
See [[Lecture 2 - Stability Analysis.pdf#page=63|slides]].

### Procedure
1. Develop relevant differential equations from the given system
2. Identify (or select) state variables
**Hint:** Variables are the ones with derivatives!
3. Organize your D.E.'s so that they are in the canonical forms.

### First Order System
See [[Lecture 2 - Stability Analysis.pdf#page=10|slides]].

$$
\underbrace{
H(s) = \frac{k}{\tau s + 1}
}_\text{Frequency Domain}
\arrows

\underbrace{
\begin{cases}
\dot{x} = -\frac{1}{\tau}x + \frac{k}{\tau}u \\
y = x
\end{cases}
}_\text{Time Domain}
$$
$k$: DC-gain
$\tau$: Time constant

There is a pole at $s= -\frac{1}{\tau}$

Large $\tau$ is *slow*
Small $\tau$ is *FAST*

##### Step Response
![[State-Space-Models-Step-Response.png|400]]

##### Impulse Response
![[State-Space-Models-Impulse-Response.png|400]]

### Second Order Systems
See [[Lecture 2 - Stability Analysis.pdf#page=14|slides]].

$$
H(s) = \frac{k \omega_{n}^{2}}{s^{2} + 2 \zeta \omega_{n}s + \omega_{n}^{2}}
$$
$\zeta$: Dampening ratio
$\omega_{n}$: Underamped natutal frequency

Poles are given by
$$
-\zeta \omega_{n} \pm \omega_{n} \sqrt{\zeta^{2} - 1}
$$

| $\zeta$     | Poles          | System              |
| ----------- | -------------- | ------------------- |
| $\zeta > 0$ | Two real poles | Underdamped         |
| $\zeta = 0$ | One real pole  | Critically Damenped |
| $\zeta < 0$ | Complex poles  | Overdamped          |

![[State-Space-Models-Second-Order-Systems.png|400]]


#### Under Damped
##### Impulse Response
![[State-Space-Models-Impulse-Response-1.png|400]]

##### Step Response
![[State-Space-Models-Step-Response-1.png|400]]

##### Bodeplot
![[State-Space-Models-Bodeplot.png|400]]

#### Critically Damped
See [[Lecture 2 - Stability Analysis.pdf#page=40|slides]].

*The safe choise*

#### Over Damped
See [[Lecture 2 - Stability Analysis.pdf#page=36|slides]].


---
#controlsystems
