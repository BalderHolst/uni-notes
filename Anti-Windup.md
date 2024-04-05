# Anti-Windup
See [[Lecture 8 - Implementation.pdf#page=9|slides]].

> *"When the limit is reached, stop integrating."*
>\- Christoffer

![[Pasted image 20240405082915.png]]
![[Pasted image 20240405082809.png]]

### Back Calculation
See [[Lecture 8 - Implementation.pdf#page=16|slides]].

This is a PID controler with back calculation. $T_{t}$ is the "tracking time" constant. If we do not have a good value for $T_t$, use [[#Conditional Integration]] instead.
![[Pasted image 20240405083422.png]]

### Conditional Integration
Turn off the integration when a limit is reached. This creates a *sharp cutoff* at the limit.

![[Pasted image 20240405084122.png]]

---
#controlsystems