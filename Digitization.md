# Digitization
See [[Lecture 8 - Implementation.pdf|slides]].

Implement control systems in digitally. The sampling frequency for the discrete controller should be at least 20 times. Otherwise special care should be taken to design a discrete controller.

![[Pasted image 20240405090737.png]]

There are two main methods.
- [[#Emulation]]
- [[#Discrete Design]]

### Emulation
Use [[Notes/Bilineær z-transformation|Bilineær z-transformation]] to convert a continuous system to a digital system.

Make sure to take sampling delay into a count (see [[Lecture 8 - Implementation.pdf#page=55|slides]]). 

##### Procedure
1. Design continuous compensation for the system $G_{d}(s)G(s)$, where $G_{d}(s)$ approximates a delay of $T/2$.
2. Derive the discrete controller by applying Tustin’s rule or the matched pole-zero method (other discretization methods exist, but the mentioned methods are preferred).
3. Analyze the design by simulation or experimentally.

### Discrete Design
Design the entire system in the [[Notes/z-transformation|z-domain]].

### Integration
There are three main ways of approximating integration in discrete time.
![[Pasted image 20240405093924.png|center|500]]

---
#controlsystems
