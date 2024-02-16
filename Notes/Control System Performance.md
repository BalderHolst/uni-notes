# Control System Performance
See [[Lecture 2 - Stability Analysis.pdf#page=44|slides]].

We are interested in three parameters
- Rise time $t_{r}$
- Settling time $t_{s}$
- Overshoot $M_{p}$

![[Pasted image 20240209091249.png|center|500]]

For **second order systems**:
$$t_{r} = \frac{1.8}{\omega_{n}}$$
$$
t_{s} = \frac{-\ln(\alpha / 100)}{\omega_{n} \zeta}
$$
$$
M_{p} = e^{-\pi / \sqrt{1-\zeta^{2}}}
$$
$\zeta$: Dampening factor (larger means more dampening)

![[Pasted image 20240209092310.png]]

---
#controlsystems