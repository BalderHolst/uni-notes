# PID-controller
See [[Lecture 4 - Design of PID Controllers.pdf|slides]].

$$
K(s) = \frac{u(s)}{e(s)} = k_{p} + \frac{k_{i}}{s} + k_{d}s
=
\frac{k_{d}s^{2} + k_{p}s + k_{i}}{s}
$$
$u(s)$: reference transfer function
$e(s)$: error transfer function

![[PID-controller.png|Pasted image 20240607144028.png]]
or alternatively
$$
K(s) = K_{p} \left( 1 + \frac{1}{sT_{i}} + sT_d \right)
$$
Which includes a low pass filder for the D-term.
$K_p$: Constant gain of the controller
$T_d$: Derivative time constant
$T_i$: Integral time constant

![[PID-controller-1.png|Pasted image 20240607144634.png]]

>[!Warning] Please add a Low Pass Filter!
>Add a low pass filter to reduce the effect of noise on the D-term.
>$$
>K(s) = K_{p} \left( 1 + \frac{1}{sT_{i}} + \frac{sT_{d}}{1+ sT_{d}/N} \right)
>$$
>$N$: Filter constant. Typically values between 2 and 20.

### PID-controller as a [[Notes/Differensligninger|Difference Equation]]
See [[Lecture 8 - Implementation.pdf#page=45|slides]].

$$
u(kT + T) =
\underbrace{k_p\ e(kT + T)}
_{u_p(kT + T)}
+
\underbrace{u_I(kT) + k_I \frac{T}{2} \left( e(kT + T) + e(KT) \right)}
_{u_I(kT + T)}
+
\underbrace{k_D \frac{2}{T}(e(kT + T) - e(kT)) - u_D(kT)}
_{u_D(kT + T)}
$$

$kT + T$: Current time step
$kT$: Previous time step
$e(n)$: Error at a certain time step


---
#controlsystems
