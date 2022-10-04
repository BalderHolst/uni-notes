# Optimering

Gøre noget så småt som muligt eller så stort som muligt.

Det vigtige er at stille formler op der beskriver forskellige relationer mellem variablerne.

```ad-example # Admonition type. See below for a list of available types.
title:                  **Eksempel**
collapse:               # Create a collapsible admonition.

Eksempel:
Det hegn på 200m skal optimeres til at omramme det størst mulige areal

Hegnet et x langt og y bredt

Omkredsen
$$o = 200$$

Vi ved at **arealet** af et rektangel kan beskrives således
$$A = x \cdot y$$

Vi ved at **omkredsen** af et rektangel kan beskrives således
$$o = 2x + 2y$$

Læg mærke til at $200 = 2x + 2y$ beskriver længderne på hegnets sider og hvordan de relaterer til omkredsen. Fordi der kun er to variabler, kan vi omskrive y, sådan:

$$y = 100 - x$$

Arealet kan nu skrives således

$$A = x \cdot y \arrows A = x \cdot (100 - x) \arrows A(x) = - x^2 + 100x$$

Har nu fundet en funktion for areal som funktion af sidelængden på hegnet. Her er den plottet:

![[Optimering.png|230]]

Parablens toppunkt må altså være det maskimale areal indhegningen kan være.

$$x = A'(x) = 0 \arrows x = 50$$

Sætter $x$-værdien ind i funktionen for at finde $y$

$$y = A(50) = 2500$$

**Landmanden kan altså maksimalt inhegne $2500m^2$ jord med $200m$ hegn**

```

---

#matematik 