# Vektorer

Vektor = en retning i et punkt. Det kan opfattes som et linjestykke der
går ud fra punktet.
$$\overrightarrow{a} = \begin{pmatrix}
x \\
y \\
\end{pmatrix}$$
$$længde\ af\ vektor = \left| \overrightarrow{a} \right|,\ \ x^{2} + y^{2} = {|\overrightarrow{a}|}^{2}$$
vektor lægges sammen:
$$\begin{pmatrix}
x1 \\
y1 \\
\end{pmatrix} + \begin{pmatrix}
x2 \\
y2 \\
\end{pmatrix} = \begin{pmatrix}
x1 + x2 \\
y1 + y2 \\
\end{pmatrix}$$

---
[[Linært Afhængige Vektorer]]


---

### Prik produkt
$$\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2  \cdot b_2 + \dots = \sum_{i=1}^{n}a_i b_i$$
Ortogonal hvis $\vec{a} \bullet \vec{b} = 0$

Hvis to vektorer er *paralelle* ($\vec{a} || \vec{b}$):   $\vec{a} \bullet \vec{b}  = |\vec{a}| \cdot  |\vec{b}|$ (see [[#Angle between vectors]])

---

### Krydsprodukt
**Kun for 3D vektorer**

$$\vt{a_1}{a_2}{a_3} \times \vt{b_1}{b_2}{b_3} = \vt{a_2b_3-a_3b_2}{-(a_1b_3 - a_3b_1)}{a_1b_2-a_2b_1}$$

$$\vec{u} \times \vec{u} = \vec{0} \s \text{fordi den er parallel med sig selv}$$
$$\vec{u} \times \vec{v} = -\vec{v} \times \vec{u}$$
#### Længden af et krydsprodukt
$$|\vec{u} \times \vec{v}| = |\vec{u}||\vec{v}| \cdot \sin \theta$$
$\theta$: Vinkel mellem vektorene.


---

### Angle between vectors
$$\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} \arrows \vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}| \cdot \cos \theta$$

---
### Length
$$|\vec{a}| = \sqrt{\sum _{i=1}^n a_i^2}$$

---

### Projektion

##### Scalar Projektion
![|400](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.zegYOHIg4NPREgMs6ZjujAHaD1%26pid%3DApi&f=1)
Projection af $\vec{u}$ på $\vec{v}$.
$$s = \vec{u} \cdot \frac{\vec{v}}{|\vec{v}|} = |\vec{u} | \cdot \cos \theta $$
$\theta$: angle between $b$ and $a$

##### Vektor projektion
Projection af $\vec{u}$ på $\vec{v}$.
$$\vec{u}_{\vec{v}} = s \cdot \hat{\vec{v}} = \left(\vec{u} \cdot \frac{\vec{v}}{|\vec{v}|}\right) \cdot \frac{\vec{v}}{|\vec{v}|}$$

---
#matematik 