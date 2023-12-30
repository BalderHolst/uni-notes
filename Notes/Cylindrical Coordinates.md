# Cylinderiske Koordinater
Se også [[Spherical Coordinates]].

---

Punkter er givet således
$$P = [r, \theta,z]$$


![punkt i cylinder run|170](https://mathinsight.org/media/image/image/spherical_coordinates.png)

$r$ : Længden fra $z$ aksen.
$\theta$ : Vinklen fra $x$ aksen i $xy$ planen.
$z$ : Højden

### Cartesian to Cylindrical Coordinates
$$
\begin{align}
f(\theta, r, z) &= (
\underbrace{r \cdot \cos \theta }_{x},
\underbrace{r \cdot \sin \theta}_{y},
\underbrace{ z }_{z}
) \\
||J|| &= r
\end{align}
$$

**Substitutions:**
$$
\begin{align}
x &\rightarrow r \cdot \cos \theta \\
y &\rightarrow r \sin \theta \\
z &\rightarrow z \\
\mathrm{dxdydz} &\rightarrow r \cdot  \mathrm{d\theta dr dz} \\
x^{2}+y^{2}= a^{2} &\rightarrow r = a
\end{align}
$$

---
#matematik 
