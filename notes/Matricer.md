# Matricer
En matrix her $m$ rækker og $n$ **søjler**.

$$ A_{m\times n} =
\left( {\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}\\
\end{array} } \right)$$
Se også [[Calculus 9th.pdf#page=629|bogen]].

### Gange med matricer
$$c_{ij} = \sum_{k=1}^n a_{ik} \cdot b_{kj}$$
$c_{ij}$ er altså prikproduktet af $A$'s række $i$ og $B$'s søjle $j$.

Hvis man vil gange matrix $A$ med matrix $B$, så skal ***$A$'s rækker være lig $B$'s søjler***.

Altid række gange søjler.


##### Ikke Kommutativ
Rækkefølgen er **IKKE ligegyldig**. (heller ikke hvis deres dimensioner er de samme).

$$A \cdot B \neq B \cdot A$$
##### Associativ
$$A \cdot (B \cdot C) = (A \cdot B) \cdot C$$

##### Resultat
$$C_{m\times p} = A_{n\times m} \cdot B_{n\times p}$$

Se eventuelt videoen:
<iframe width="350" height="200" src="https://www.youtube.com/embed/vzt9c7iWPxs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Addition
- **Skal have samme størrelse**
- Man lægger sammen elementvis

$$A + B = B + A$$

### Kvadratiske matricer
En matrix er kvadratisk hvis den har **lige mange rækker og kolonner**.

### Transposition
> *"Byt rækker og kolonner"*

$$ A_{m\times n}^T =
\left( {\begin{array}{cccc}
a_{11} & a_{21} & \cdots & a_{1m}\\
a_{11} & a_{22} & \cdots & a_{2m}\\
\vdots & \vdots & \ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{mn}\\
\end{array} } \right) $$
$$\left(A^T\right)^T = A$$

##### Symmetriske matricer
Matrix a er symmetrisk hvis $A^T = A$.

*Alle symmetriske matricer er kvadratiske.*


### Række og Søjle vektorer

##### Kolonnevektor
 $$v_{n\times 1} =
\left( {\begin{array}{cccc}
v_{1}\\
v_{2}\\
\vdots\\
v_{n}\\
\end{array} } \right) $$
##### Rækkevektor
 $$v_{1\times n} =
\left( {\begin{array}{cccc}
v_{1} & v_{2} & \dots & v_{n}
\end{array} } \right) $$

---
#matematik 