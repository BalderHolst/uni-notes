# Penduler

>[!warning] Fejl i penduler
>De fleste pendul-modeller er [[notes/Linarisering|linariserede]]. Der er derfor en større og større fejl som $\theta$ øges. Fejlen kan aflæses på [[Lektion 10-FYS1_2022.pdf#page=18|dette]] slide. 

>[!note]- Matematisk vs. Fysisk pendul
>[[Lektion 10-FYS1_2022.pdf#page=14]]



### Matematisk pendul
Objektet er en punktmasse.
$$\theta = \theta_{0} \cdot \sin(\omega t + \delta)$$

$$\omega = \sqrt{\frac{g}{l}}$$
$g$ : [[Tyngdeaccelerationen]]
$l$ : Længden af pendulet

$$T_{mat}= 2\pi \sqrt{\frac{l}{g}}$$

### [[Fjederkraft|Fjeder]]pendul
$$\omega = \sqrt{\frac{k}{m}} \arrows T=\sqrt{\frac{m}{k}}$$

### Fysisk Pendul ([[Lektion 10-FYS1_2022.pdf#page=12|Slide]])
$$\tau = rF_{\perp} = rF_{t}\sin(\theta) = rMg\sin(\theta)$$
$\tau$ : [[Kraftmoment]]
$F_{\perp}$ : Kraften vinkelret på radius
$F_t$ : [[Tyngdekraften]]
$M$ : Massen af objektet
$\theta$ : Vinkel fra lodret



Dette er [[notes/Linarisering|linariseret]]. Det virker derfor bedst for små $\theta$.
$$\alpha = \frac{r \cdot M \cdot g}{I} \cdot \theta $$

#### Perioden
$$T_{fys}= 2\pi\sqrt{\frac{I}{Mgr}} = 2\pi\sqrt{\frac{l_{RP}}{g}} \s \text{hvor } l_{RP}= \frac{I}{Mr}$$
$l_{RP}$ : Reduceret pendullængde
$I$ : [[Inertimoment]]
$r$ : Distance fra aksen til pendulets [[Massemidtpunkt|massemidtpunkt]]

#### Energi

##### Kinetisk energi
$$K(\theta) = \frac{1}{2}mv^2 = \frac{1}{2}m\left( r \cdot \frac{d \theta (t)}{dt} \right)^2 $$
##### Potentiel Energi
$$U(\theta) = mgh = mgl \cdot(1-\cos(\theta))$$
Bruger en første ordens [[Taylorpolynomium|taylorrække]] for at estimere $\cos(\theta)$.
$$\cos(\theta) \approxeq 1 - \frac{\theta^{2}}{2} \arrow U(\theta) = mgl\cdot\left(1-1+\frac{\theta^{2}}{2}\right)$$
$$\Rightarrow \hspace{5mm} U(\theta) = \frac{1}{2}mgl\theta^2$$

---
#fysik 