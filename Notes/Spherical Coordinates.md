# Spherical Coordinates


$$P = (R, \phi, \theta)$$
$R$ : Længden fra orego til $P$
$\phi$ : Vinkel opad 
$\theta$ : Vinklen fra $x$-aksen i $xy$-planen

---
![[Pasted image 20231105163245.png|center|300]]

---


### Oversæt fra Cartesiske koordinater
$$\begin{align}
x &\rightarrow \rho \cdot  \sin \phi \cdot \cos \theta\\
y &\rightarrow \rho \cdot  \sin \phi \cdot \sin \theta\\
z &\rightarrow \rho \cdot  \cos \phi \\
\mathrm{dV} &\rightarrow \rho^{2} \cdot \sin{\phi}\ \mathrm{d\rho\ d\phi\ d\theta}
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
