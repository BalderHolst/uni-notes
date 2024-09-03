# Vektorer
Vectors are multidimensional numbers.

$$
\vec{x} =
\begin{bmatrix}
x_{1}  \\
x_{2} \\
\vdots \\
x_n
\end{bmatrix}
\in \mathbb{R}^{n}
$$

---

## Noter om Vektorer
```dataview 
list
from #vektorer 
sort file.name
```

---

### Length
$$|\vec{a}|^{2} = x^{2} + y^{2} $$

### Addition
$$\begin{pmatrix}
x_1 \\
y_1 \\
\end{pmatrix} + \begin{pmatrix}
x_2 \\
y_2 \\
\end{pmatrix} = \begin{pmatrix}
x_1 + x_2 \\
y_1 + y_2 \\
\end{pmatrix}$$

### Prik produkt
$$\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2  \cdot b_2 + \dots = \sum_{i=1}^{n}a_i b_i$$
Ortogonal hvis $\vec{a} \bullet \vec{b} = 0$

Hvis to vektorer er *paralelle* ($\vec{a} || \vec{b}$):   $\vec{a} \bullet \vec{b}  = |\vec{a}| \cdot  |\vec{b}|$ (see [[#Angle between vectors]])

---

### Krydsprodukt
**Kun for 3D vektorer**
$$v \times w = \det(\left[v \, w\right])$$

$$\vt{a_1}{a_2}{a_3} \times \vt{b_1}{b_2}{b_3} = \vt{a_2b_3-a_3b_2}{-(a_1b_3 - a_3b_1)}{a_1b_2-a_2b_1}$$

$$\vec{u} \times \vec{u} = \vec{0} \s \text{fordi den er parallel med sig selv}$$
$$\vec{u} \times \vec{v} = -\vec{v} \times \vec{u}$$
#### Længden af et krydsprodukt
$$|\vec{u} \times \vec{v}| = |\vec{u}||\vec{v}| \cdot \sin \theta$$
$\theta$: Vinkel mellem vektorene.


---

### Vinkel mellem Vektorer
$$\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} \arrows \vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}| \cdot \cos \theta$$

---
### Længde
$$|\vec{a}| = \sqrt{\sum _{i=1}^n a_i^2}$$

---

### Projektion

##### Scalar Projektion
![|center|400](http://lh4.ggpht.com/-rRaMje7-pyw/TiaX5_6ae2I/AAAAAAAAAqQ/mSoHIfkFeyA/image_thumb19.png?imgmax=800)
Projection af $\vec{u}$ på $\vec{v}$. Dvs. $\vec{u}$ i $\vec{v}$'s retning. 
$$s = \vec{u} \bullet \frac{\vec{v}}{|\vec{v}|} = |\vec{u} | \cdot \cos \theta $$
$\theta$: angle between $b$ and $a$

##### Vektor projektion
Projection af $\vec{u}$ på $\vec{v}$.
$$\vec{u}_{\vec{v}} = s \cdot \hat{\vec{v}} = \left(\vec{u} \cdot \frac{\vec{v}}{|\vec{v}|}\right) \cdot \frac{\vec{v}}{|\vec{v}|}$$

---
#matematik #subject