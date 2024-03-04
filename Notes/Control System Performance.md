# Control System Performance
See [[Lecture 2 - Stability Analysis.pdf#page=44|slides]] and more [[Lecture 5 - Root Locus.pdf#page=21|here]].

We are interested in three parameters
- Rise time $t_{r}$
- Settling time $t_{s}$
- Overshoot $M_{p}$

![[Pasted image 20240209091249.png|center|500]]

#### Second Order Systems

$$
poles = - \underbrace{\zeta \omega_{n}}_\sigma \pm j \underbrace{\omega_{n}\sqrt{1-\zeta^{2}}}_{\omega_d}
$$
$$t_{r} = \frac{1.8}{\omega_{n}}$$
$$
t_{s} = \frac{-\ln(\alpha / 100)}{\omega_{n} \zeta}
$$
$$
M_{p} = e^{-\pi / \sqrt{1-\zeta^{2}}}
$$
$\zeta$: Dampening factor (larger means more dampening/less overshoot)

![[Pasted image 20240209092310.png]]

![[Pasted image 20240304092114.png]]

---
#controlsystems