# Sfæriske Koordinater

$$P = (R, \phi, \theta)$$
$R$ : Længden fra orego til $P$
$\phi$ : Vinkel opad 
$\theta$ : Vinklen fra $x$-aksen i $xy$-planen

---

![Spherisk punkt| 270](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmse.redwoods.edu%2Fdarnold%2Fmath50c%2Fmathjax%2Fspherical%2Fspherical3.png&f=1&nofb=1)

---


### Oversæt til Cartesiske koordinater
$$\begin{align}
x &= R \cdot  \sin \phi \cdot \cos \theta\\
y &= R \cdot  \sin \phi \cdot \sin \theta\\
z &= R \cdot  \cos \phi
\end{align}$$

$R$ kan også findes på denne måde
$$R^2 = x^2 + y^2 + z^2 = r^2+z^2$$
$r$ er længden til punktet i $xy$-planen (længden fra $O$ til $Q$ på billedet ovenfor). Se i [[Calculus 9th.pdf#page=627|bogen]].

$r$ kan findes således
$$r = \sqrt{x^2 + y^2} = R \cdot  \sin \phi$$
Derudover er dette sandt
$$\tan \phi = \frac{r}{z} = \frac{\sqrt{x^2 + y^2}}{z} \s \text{og} \s \tan \theta =\frac{y}{x}$$

---
#matematik 