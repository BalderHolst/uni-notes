# Fejlberegning på Operationsforstærker

![[Pasted image 20240312083453.png]]

$$A_{OL} = \frac{dV_{o}}{dV_{id}}$$
$A_{OL}$: Open loop amplification 

$$
V_{id} = \alpha V_{in} - \beta V_{o} \Rightarrow
\begin{cases}
\alpha = \frac{V_{id}}{V_{in}}|_{V_{o} = 0} \\
\beta = \frac{-V_{id}}{V_{o}}|_{V_{in}=0}
\end{cases}
$$

##### Error Factor
$$
k_{p} = \frac{1}{1 + \frac{1}{\beta A_{OL}}}
$$

##### Closed Loop Amplification

$$
A_{L} = \frac{V_{o}}{V_{in}} = \frac{\alpha}{\beta }\cdot k_{p}
$$


---
#forstærker