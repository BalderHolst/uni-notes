# Kondensator
>*"Jo mere ladning, jo større spændingsforskel over pladen"*
>*"Man kan ikke afsætte effekt i en kondensator"*
> \- Jan

![|300](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Felectronicspost.com%2Fwp-content%2Fuploads%2F2015%2F10%2Fcapacitor-symbol.png&f=1&nofb=1&ipt=3ecf5c6913650a85a1c4dbe45bfe9c8972627df71462fa6f22fa98a408a28037&ipo=images)

**Strømmen er *nul*** når kondensatoren er opladt.

### Formler
$$Q=C \cdot V_c$$
$C$ : Kapacitansen $\frac{\text{C}}{\text{v}}$.
$Q$ : [[Ladning]] i kondensatoren.
$V_c$ : Spænding over kondensatoren. 

Hvis man [[Integralregning|integrerer]] kan man finde strømmen.
$$I_c = C \cdot \frac{dV_c}{dt}$$
$I_c$ : Strømmen gennem kondensatoren.

Spænding kan derfor *ikke ændre sig momentant*, da det ville betyde en uendelig stor spænding. 

### Opladning og Afladning

#### Tidskonstanten
$$\tau = R \cdot C$$
$R$ : Modstanden i [[Serieforbindeler|serie]] med kondensatoren.
$C$ : Kapacitansen 

##### Opladning
$$f(t)=A \cdot (1-e^{\frac{-t}{\tau}})$$
$A$ : Spændingen ved fuld opladning.

##### Afladning 
$$g(t) = B \cdot e^{\frac{-t}{\tau}}$$
$B$ : Startspændingen.

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

>[!note]- Imdansen er $\infty$ i ved DC
>$$$$


---
#elektronik #komponent