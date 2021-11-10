
# Differentialligninger
Har altid en funktion som løsning.

En ligning der indeholder en [[Differentialregning|afledt funktion]]

---
### Førsteordensdifferentialligninger
$$y'=y \cdot (b-ay) \arrows y'=ay \cdot (M-y), \text{ hvor } M = \frac{b}{a}$$

##### Løsning
$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}} \arrows f(x)=\frac{M}{1+C \cdot e^{-bx}}$$

**Variabler**
$M$: grenseværdien


##### Bevis
 Bevis for at dette er løsningen på differentialligningen
 
 $$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}}, \s f(x) \ne 0$$

Hvis $f(x)$ er en løsning til differentialligningen $y'=y \cdot (b-ay)$, må dette gælde (har bare sat $f(x)$ ind på $y$'s plads)

$$y'=y \cdot (b-ay) \arrows f'(x)=f(x) \cdot (b-a \cdot f(x))$$

Ganger $f(x)$ ind i parantesen

$$f'(x)=f(x) \cdot b-a \cdot f(x)^2$$

**God ide:** ganger med $-\frac{1}{f(x)^2}$ på begge sider

$$-\frac{1}{f(x)^2} \cdot f'(x)=-\frac{1}{f(x)^{\c{2}}} \cdot \c{f(x)} \cdot b-\left(-\frac{1}{\c{f(x)^2}}\right) \cdot a \cdot \c{f(x)^2}$$




### Til løsning af alle linære førsteordensdifferentialligninger
[[Linære førsteordensdifferentialligninger]]


---

### At Gøre Prøve

At gøre prøve er en måde at teste om en bestemt funktion, er en løsning for en given differentialligning. Eksempelvis kunne man spørge: er $f(x) = 2e^{16x}$ en gyldig løsning på differentialligningen $y' = 16y$? Det første skridt mod at besvare spørgsmålet er at [[Differentialregning|differentiere]] funktionen.


$$f'(x)=32e^{16x}$$

Vi kan nu sætte vores $f(x)$ og $f'(x)$ ind i differentialligningen

$$y = 16y  \s f'(x) = 16 \cdot f(x) \s 32e^{16x} = 16 \cdot 2e^{16x} \s 32e^{16x} = 32e^{16x}$$

Her kan det ses at funktionen $f(x) = 2e^{16x}$ er en løsning på differencialligningen $y'=16y$, fordi at at vi ender med et sandt udtryk. På den måde kan man afgøre om en funktion er en løsning på en given differentialligning, ved at gøre prøve.


```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

![[Bevis for differentialligninger]]

```

---

### *Fuldstændig* og *partikulær* løsning
##### Fuldstændig Løsning
En løsning med en ubestemt konstant til sidst. Denne konstant er et produkt af [[Integralregning]].

**Eks.**





---
#matematik 

