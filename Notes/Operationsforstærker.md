# Operationsforstærker
> *"Snuser hvad den skal aflevere"*
> \- Jan

Kan maks forstærke til $V^+$ eller negativt til $V^-$. Forsyningsspændingerne *bergænser* altså $V_{out}$.

*tip:* Man kan regne forstærkningen af hver spændingskilde individuelt. ([[Superposistion]])

Modkobling = Negativ feedback

### Inverterende (Negativ feedback)

![|300](https://i.stack.imgur.com/QCX6a.jpg)

$$V_{out} = -\frac{R_f}{R1} \cdot V_{in}$$
$V_{out}$ : Operationsforstærkerens output-spænding.
$V_{in}$ : Input-spændingen.
$R_f$ : Feedback modstanden (den fra $V_{out}$ til operationsforstærkerens negative indgang)
$R_1$ : Modstanden mellem $V_{in}$ og operationsforstærkerens negative indgang.


### Ikke-inverterende
![|340](https://www.allaboutelectronics.org/wp-content/uploads/2020/10/op-amp_1.png)
$$V_{out}= \left(1+\frac{R_f}{R_1}\right) \cdot V_{in}$$
$V_{out}$ : Operationsforstærkerens output-spænding.
$V_{in}$ : Input-spændingen (der er forbundet til operationsforstærkerens positive indgang).
$R_f$ : Feedback modstanden (den fra $V_{out}$ til operationsforstærkerens negative indgang)
$R_1$ : Modstanden mellem operationsforstærkerens negative indgang og jord (gnd).

### Biaskompensering
Hver terminal trækker en strøm. Denne strøm er ikke den samme.
$$R_{B}^{+} \neq R_{B}^{-}$$
Biaskompensering er at lave de to strømme lig hinanden. Dette gøres typisk ved at sætte en modstand ind sådan at begge biasstrømme trækkes gennem samme modstand. Dette gør det muligt kun at opgive offset mellem terminalerne.

![[Pasted image 20240402084028.png]]

Offset strømmen $I_{off}$ kompenserer vi for ved at indsætte en $V_{off}$ sådan af vi kompenserer for $I_{off}$.


---
#elektronik #komponent 