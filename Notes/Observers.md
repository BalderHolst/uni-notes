---
created: 2025-09-21
slides:
  - "[[Lecture 10 - Observers.pdf#page=6]]"
  - "[[CAS-2026-Lecture7-obs.pdf]]"
  - "[[CAS-2026-Lecture7-LectureNotes.pdf]]"
tags:
  - controlsystems
---
# Observers
We create a *"virtual" copy* of our system where we have direct access to the internal states of the system.

Always check [[observability]] before implementing an observer.

>[!warning] Place poles to the left of system
>When choosing $L$ **make sure that the poles of $A+LC$ are to the left of the system** (about seven times) this makes sure that the system has the dominant poles.

Create an estimate of the system and feed the error from the real system into the estimate system.

![[Observers.png|Pasted image 20240419084942.png]]

$$ \dot{e} = (A + LC) e $$

$(A + LC)$'s

[[Eigen values and vectors|eigen values]]

must be in the left half plane. This is also the general criteria for stability of a system. Choosing an $L$ to make the system stable is *only possible if the system is observable*. $L$ can be found matlab using the `place` function.  [[Notes/State Feedback|State feedback]] based on estimated state instead of real system state.

![[Observers-1.png|Pasted image 20240419091927.png]]
![[Observers-2.png|Pasted image 20240419093350.png]]

For the observer based control to be closer to the state feedback. Place the $A+LC$ poles further to the left in the $s$-plane.

### Placing Observer Poles

$$
p_\mathrm{pbs} = \mathrm{eig}[A-LC] =  \mathrm{eig}[(A-LC)^{T}] = \mathrm{eig}[(A^{T}-L^{T}C^{T})]
$$


### Observers as a Filter
An observer can also be used as a filter, as it smooths out the estimated output compared to the measured output. It can therefore sometimes me be a good idea to implement an observer, even though we measure all the system states.
