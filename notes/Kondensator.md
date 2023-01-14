# Kondensator
>*"Jo mere ladning, jo større spændingsforskel over pladen"*
>*"Man kan ikke afsætte effekt i en kondensator"*
> \- Jan

![|300](https://electronicspost.com/wp-content/uploads/2015/10/capacitor-symbol.png)

**Strømmen er *nul*** når kondensatoren er opladt.

### Formler
$$Q=C \cdot V_c$$
$C$ : Kapacitansen $\frac{\text{C}}{\text{v}}$.
$Q$ : [[Ladning]] i kondensatoren.
$V_c$ : Spænding over kondensatoren. 

Hvis man [[Differentialregning|differentierer]] kan man finde strømmen.
$$I_c = C \cdot \frac{dV_c}{dt}$$
$I_c$ : Strømmen gennem kondensatoren.

Spænding kan derfor *ikke ændre sig momentant*, da det ville betyde en uendelig stor spænding. 

### Opladning og Afladning

#### Tidskonstanten
$$\tau = R_T \cdot C$$
$R_T$ : [[Thevenin Ækvivalens|Thevenin Modstanden]]
$C$ : Kapacitansen 

##### Opladning
$$V(t)=V_{maks} \cdot e^{\frac{-t}{\tau}}$$
$V_{maks}$ : Spændingen ved fuld opladning.

##### Afladning 
$$V(t) = V_{start} \cdot (1 - e^{\frac{-t}{\tau}})$$
$V_{start}$ : Startspændingen.

### Arbejdet
$$W_C= \frac{1}{2} \cdot C \cdot V_C^2$$
$W_C$ : Energien lagret i kondensatoren.
$C$ : Kapaciteten $\frac{\text{C}}{\text{v}}$.
$V_C$ : Spænding over kondensatoren. 

### Konstanten

$$C = \frac{\epsilon_r \cdot \epsilon_0 \cdot A}{d}$$
$\epsilon_r$ :
$\epsilon_0$ :
$A$ :
$d$ :

### Impedans
$$z_{c}=\frac{1}{j \omega C}$$
Imdansen er $\infty$ i ved DC

### Opladning
$$V_{c}(t) = V_{full} \cdot e^{\frac{-\tau}{t}}$$

Kondensatoren er fuldt opladt efter $5\tau$.

$\tau$ kan findes således
$$\tau = R_{T} \cdot C$$
$R_{T}$ : [[Thevenin Ækvivalens|Theveninmodstanden]]
$C$ : Kapacitansen

---
#elektronik #komponent