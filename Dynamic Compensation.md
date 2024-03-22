# Dynamic Compensation
See [[Lecture 7 - Dynamic Compensators and Stability Margins.pdf#page=24|slides]].

### Lead Compensator
$$
D(s) = \frac{Ts + 1}{\alpha Ts + 1} \quad \mathrm{where}\ \alpha < 1
$$

![[Pasted image 20240322094502.png]]

#### Procedure
1. Determine open-loop gain $K$ to satisfy error or bandwidth requirements:
    **1.1** To meet error requirement, pick K to satisfy error constants ($K_p$, $K_V$ , $K_a$) so that $e_ss$ error specification is met.
    **1.2** Alternatively, to meet bandwidth requirement, pick $K$ so that the open-loop crossover frequency is a factor of two below the desired closed-loop bandwidth. 
2. Evaluate the phase margin of the uncompensated system using the value $K$ obtained from Step 1.
3. Allow for extra margin (about $10\degree$), and determine the needed phase lead φmax (one lead compensation should contribute a maximum of $60\degree$ to the phase).
4. Determine $\alpha$ from
$$
\sin \phi_{\mathrm{max}} = \frac{1 - \alpha}{1 + \alpha}
$$

### Lag Compensator
$$
D(s) = K_{0}\alpha \frac{Ts + 1}{\alpha Ts + 1}
$$

5. Pick ωmax to be the crossover frequency; thus, the zero is at $1/T = \omega_{\mathrm{max}} \sqrt{\alpha}$ and the pole is at $1/\alpha T = \omega_{\mathrm{max}}/\sqrt{\alpha}$.

6. Draw the compensated frequency response and check the phase margin.

7. Iterate on the design. Adjust compensator parameters (poles, zeros, and gain) until all specifications are met.

---
#controlsystems
