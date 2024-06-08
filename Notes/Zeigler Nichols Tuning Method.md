# Zeigler Nichols Tuning Method
Use if a model of the **system is not available**. Otherwise use [[Root Locus Tuning]] instead.

There are two Zeigler Nichols tuning methods:
- Zeigler Nichols Tuning method based on **step response**
- Zeigler Nichols' *Ultimate Sensitivity Method*

### Based on Step Responce
Consider a system with the following step response

![[Pasted image 20240607152006.png|center|450]]

The constants for a P, PI or PID controller can then be determined as follows

| Controller | PID Gains              |
| ---------- | :--------------------- |
| P          | $K_{p} = \frac{1}{RL}$ |
| PI         | $\begin{cases} K_p = \frac{0.9}{RL} \\ T_i = \frac{L}{0.3} \end{cases}$        |
| PID        | $\begin{cases} K_p = \frac{1.2}{RL} \\ T_i = 2L \\ T_d = 0.5L \end{cases}$        |

Where
$$
R = A/\tau
$$

### Ultimate Sensitivity Method
Attach a P-controller to the system and turn up the gain until the system output oscilates. The gain is now the *ultimate gain* $K_u$. The period of the output signal is called $P_u$. PID controller constants can now be found with the following table.

![[Pasted image 20240607152958.png]]

| Controller | PID Gains              |
| ---------- | :--------------------- |
| P          | $K_{p} = 0.5K_u$ |
| PI         | $\begin{cases} K_p = 0.45K_u \\ T_i = \frac{P_u}{1.2} \end{cases}$        |
| PID        | $\begin{cases} K_p = 0.6K_u \\ T_i = 0.5P_u \\ T_d = \frac{1}{8}P_u \end{cases}$        |


---
#controlsystems
