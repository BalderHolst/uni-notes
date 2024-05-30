# Fejlberegning på Operationsforstærker
See [[Noter lektion 2.pdf|lecture notes]].

![[Pasted image 20240312083453.png]]
$$
V_{o} = A_\mathrm{OL} \cdot V_{id}
$$
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
A_{L} = \frac{V_{o}}{V_{in}} = \frac{\alpha}{\beta }\cdot  \underbrace { \frac{1}{1 + \frac{1}{\beta A_{OL}}} }_{k_{p}}
$$
### Bandwidth
The bandwidth of an opamp is partly determined by the gain used. Datasheets often specify a **GBWP** (gain bandwidth product) also called *unity gain bandwidth*.

$$
\mathrm{BW} = \frac{\mathrm{GBWP}}{\mathrm{G}}
$$

### Common Mode Rejection Ratio

In reality the common mode input (mean of inputs) is also amplified. This is caused by differences in amplification of the two inputs.

$$
\mathrm{CMRR} = 20\, \log \left( \frac{|A_d|}{|A_{cm}|} \right)
$$
$A_d$: Amplification of input difference
$A_{cm}$: Common mode amplification

---
#forstærker