# [[Linære Funktioner|Linjer]] og [[Vektorer]]

En linje kan beskrives med to punkt og en vektor. 

Der er to måder en vektor kan beskrive hældningen af en linje. Det er med en *normalvektor* eller en *retningsvektor*.

---

## Linjens Ligningning

Vores punkt
$$p = (x_0,y_y)$$

Vores **normalvektor**

$$\vec{n} = \begin{pmatrix}
a \\
b \\
\end{pmatrix}$$

Ligning for linjen (linjens ligning):

$$a \cdot (x-x_0) + b \cdot (y - y_0) = 0$$

Alternativ ligning:

$$a \cdot x + b \cdot y + c = 0$$
$$c = - (a \cdot x_0 + b \cdot y_0)$$

Det er vigtigt at pointere at $c$ er en *konstant*

---

```ad-example # Admonition type. See below for a list of available types.
title:                  **Bevis for Linjens Ligning**
collapse:               # Create a collapsible admonition.

![[Bevis for Linjens Ligning]]

```

---

## Parameterfremstilling

Ligning:

$$
\v{x}{y} = \v{x_0}{y_0} + t \cdot \v{r_1}{r_2}
$$

Dette kan omskrives som to funktioner for henholdsvis $x$ og $y$ således:

$$x(t) = x_0 + t \cdot r_1$$
$$y(t) = y_0 + t \cdot r_2$$

Dette er altså retningsvektoren

$$\v{r_1}{r_2} = \vec{r}$$

Et punkt på linjen kan beskrives som, vektorbasen $\v{x_0}{y_0}$ + retningsvektoren $\vec{r}$ ganget med $t$. 

Ved at ændre $t$ kan vi altså nå hvilket som helst punkt på linjen.

![[Parameterfremstilling.png|240]]

---
```ad-example # Admonition type. See below for a list of available types.
title:                  **Bevis for Parameterfremstilling**
collapse:               # Create a collapsible admonition.

![[Bevis for Parameterfremstilling]]

```

---

## Vinklen mellem vektorer
$$cos(v) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

Dette kan bruges med både retnings- og normalvektorer

Hvis man har en af hver, omdanner man en af de to.

## Projektion af et punkt på en linje

**Order of operations**
1. Find en retnings- eller no
2. Tegn en hjælpelinje 