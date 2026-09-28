# State Space Models
See [[Lecture 1 - Slides.pdf#page=32|control slides]] or [[Lessons/Semester 7/ssp/Lektion 1 slides.pdf|ssp slides]].

![[Pasted image 20260928091536.png|800]]

- [[Linear State Space Models]]
- [[Discrete Time Space Models]]

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

