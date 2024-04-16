# PID-controller

$$
u(s) = (k_{p} + \frac{k_{i}}{s} + k_{d}s)e(s)
$$

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
