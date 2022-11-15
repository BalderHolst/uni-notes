# Sfæriske Koordinater

$$P = (R, \phi, \theta)$$
$R$ : Længden fra orego til $P$
$\phi$ : Vinkel opad 
$\theta$ : Vinklen fra $x$-aksen i $xy$-planen

---
![Spherisk punkt|center|400](https://mse.redwoods.edu/darnold/math50c/mathjax/spherical/spherical3.png)

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