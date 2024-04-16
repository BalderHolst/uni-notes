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
See [[Lecture 8 - Implementation.pdf#page=62|slides]].

>[!tip] Always use Tustins rule
>Tustins rule is the same as the Trapezoid rule. To transform from $s$-place to $z$-plane, use the following rule:
>$$
>G(s)|_{s=\frac{2}{T}\frac{z-1}{z+1}}
>$$
>This is similar to [[Notes/Bilineær z-transformation|Bilinear z-transformation]] without pre-warping.

>[!warning]
> Do not use forward integration, as it *does not guarantee stability* even if the continuous system is stable.

There are three main ways of approximating integration in discrete time.
![[Pasted image 20240405093924.png|center|500]]

These map the $s$-domain to different parts of the $z$-domain.

![[Pasted image 20240405094204.png]]

### Sampling Delay
See [[Lessons/Semester 3/signalbehandling/Exercises/lektion8.pdf#page=27|slides]].

$$G_{d}(s) = \frac{1}{\frac{T}{2}s + 1}$$
$G_{d}(s)$: Transfer funktion for samling delay

![[Pasted image 20240416084917.png|500]]

>[!tip]- Sampling delay illustration
>![[Pasted image 20240416084850.png]]

---
#controlsystems
