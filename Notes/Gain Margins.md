# Gain Margins

We look for when the loop transfer function crosses the neutral stability threshold and becomes unstable.
$$
|L(s)| = 1 \quad \angle L(s) = 180\degree
$$

>[!tip] Rule of thumb
> Phase margin should be at least $40\degree$

## Bode Plot
Draw [[Notes/Bode Plot|Bode Plot]] for loop amplification.
1. Look where phase is $180\degree$
2. Look at the same place in the amplitude plot and read the difference from $0dB$ to get $GM$ (gain margin).
3. The phase margin is read in the phase plot where the amplitude plot is $0\ \mathrm{dB}$ to find $PM$ (phase margin).
![[Gain-Margins-Bode-Plot.png|Pasted image 20240322083822.png]]

## Nyquist Plot
![[Gain-Margins-Nyquist-Plot.png|Pasted image 20240322083846.png]]

>[!tip]- Vector Margin
>![[Gain-Margins-Nyquist-Plot-1.png|Pasted image 20240322090059.png]]

---
#controlsystems
