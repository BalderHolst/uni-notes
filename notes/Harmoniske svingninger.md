# Harmoniske svingninger

Den genneralle form for funktionen
$$x(t)= A \cdot \sin(\omega \cdot t + \phi) + d$$
$x(t)$ : Position som funktion af Tid
$A$ : Amplituden
$\omega$ : [[Vinkelfrekvens|Vinkelfrekvensen]]
$\phi$ : Faseforskydning
$d$ : Position forskydning


---

### Ekstra formler til aflæsning af transformation i x-retningen

**Perioden**

$$T = \frac{2\pi}{\omega}$$

$T$ = perioden/bølgelængden

**Faseforskydningen** kan regnes med denne formel

$$\frac{-\phi}{\omega}$$

Dette er også sandt (radianer)

$$sin(x) = cos(x-\frac{\pi}{2})$$


---

### Differentieret bølgefunktion

##### Hastighed
$$v(t)=\omega \cdot A \cdot \cos(\omega \cdot t + \phi)$$

##### Acceleration
$$a(t)=\omega^2 \cdot A \cdot \cos(\omega \cdot t + \phi)$$

---

### Med Fjeder
Se [[Fjederkraft]].

Dette er sandt for en harmonisk svingning forsaget af en fjeder.
$$\omega=\sqrt{\frac{k}{m}} \s \text{og} \s T=2\pi \sqrt{\frac{m}{k}} \Rightarrow T\propto \sqrt{m} \s \text{og} \s f=\frac{1}{2\pi} \sqrt{\frac{k}{m}}$$

#### Energi

Den [[Potentiel Energi|potentielle energi]].
$$U(x) = \frac{1}{2}kx^2$$
Den [[Kinetisk Energi|kinetiske energi]].
$$K(v)=\frac{1}{2}mv^2$$

Den totale energi i systemet ([[Mekanisk energi]]).
$$E_{mek} = \frac{1}{2}kA^2=\frac{1}{2}m\omega^2A^2$$

Altså skal ændringen i *mekanisk energi* over tid være $0$.
$$\frac{dE_{mek}}{dt}=0$$
#### Dæmpede Svingninger
$$\vec{F_d}=-b\vec{v}=-b \frac{d\vec{x}}{dt}$$
$\vec{F_d}$ : Dæmpningskraften
$b$ : Dæmpningskoefficienten

Dæmpningskraften kan trækkes fra fjederkraften, for at finde net kraften. 
$$F_{res}=-F_{fjeder}-F_{d} \arrow m \cdot x'' + b x' + k \cdot x = 0$$

For at løse den, se [[Dæmpede Svingninger - Differentialligning]].

Løsningen er på formen:
$$x(t)=A e^{-\alpha t}\sin(\omega't+\phi)$$

Hvor
$$\alpha = \frac{b}{2m} \s \text{og} \s \omega'=\sqrt{\frac{k}{m}- 
 \frac{b^{2}}{4m}}$$

---
#fysik 
#matematik 

