
# Differentialligninger
En ligning med en funktion som løsning.

En ligning der indeholder en [[Differentialregning|afledt funktion]]

---
### Førsteordensdifferentialligninger


#### Logistisk vækst

$$y'=y \cdot (b-ay) \arrows y'=ay \cdot (M-y), \text{ hvor } M = \frac{b}{a}$$

##### Løsning
$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}} \arrows f(x)=\frac{M}{1+C \cdot e^{-bx}}$$

**Variabler**
$M$: grenseværdien/bærekapaciteten

```ad-example # Admonition type. See below for a list of available types.
title:                  Plot
collapse:               # Create a collapsible admonition.

![[Pasted image 20211112124909.png]]

```



```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

Eksempeltekst


 Bevis for at dette er løsningen på differentialligningen
 
 $$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}}, \s f(x) \ne 0$$

Hvis $f(x)$ er en løsning til differentialligningen $y'=y \cdot (b-ay)$, må dette gælde (har bare sat $f(x)$ ind på $y$'s plads)

$$y'=y \cdot (b-ay) \arrows f'(x)=f(x) \cdot (b-a \cdot f(x))$$

Ganger $f(x)$ ind i parantesen

$$f'(x)=f(x) \cdot b-a \cdot f(x)^2$$

**God ide:** ganger med $-\frac{1}{f(x)^2}$ på begge sider

$$-\frac{1}{f(x)^2} \cdot f'(x)=-\frac{1}{f(x)^{\c{2}}} \cdot \c{f(x)} \cdot b-\left(-\frac{1}{\c{f(x)^2}}\right) \cdot a \cdot \c{f(x)^2}$$

$$-\frac{1}{f(x)^2} \cdot f'(x) = -\frac{1}{f(x)} \cdot b +a \arrows -\frac{1}{f(x)^2} \cdot f'(x) = a-\frac{1}{f(x)} \cdot b$$

**Anden gode ide:** vi definerer en funktion $g(x) = \frac{1}{f(x)}$

Vi differentierer $g(x)$, og opdager at $\frac{1}{f(x)}$, er en sammensat funktion. Derfor bruger vi [[Differentialregning Regneregler|regnereglen for sammensatte funktioner]].

$$g'(x) = \left(\frac{1}{f(x)}\right)' = -\frac{1}{(f(x))^2} \cdot f'(x)$$

Vi lægger nu mærke til at venstre side af vores ligning kan omskrives til $g'(x)$,  og at en del af andet led kan omskrives til $g(x)$.

$$g'(x)=a-g(x) \cdot b$$

Vi lægger mærke til at $g(x)$ er en løsning på den kendte differentialligning $y'=b-a \cdot y$. (dog er $a$ og $b$ byttet rundt her) [[Linære førsteordensdifferentialligninger#3 Løsningsformel Newtons Afkølingslov]]

derfor må dette være sandt om $g(x)$ (bruger $K$ i stedet for $C$)

$$g(x) = \frac{a}{b} + K \cdot e^{-b \cdot x}$$

Da vi ved at $g(x) = \frac{1}{f(x)}$ må dette være sandt

$$\frac{a}{b} + K \cdot e^{-b \cdot x} = \frac{1}{f(x)} \arrows f(x)=\frac{1}{\frac{a}{b} + K \cdot e^{-b \cdot x}}$$

Vi forlænger nu brøken med $\frac{b}{a}$

$$f(x) =\frac{1 \cdot \frac{b}{a}}{\frac{\c{b}}{\c{a}} \cdot \frac{\c{a}}{\c{b}} + \frac{b}{a} \cdot K \cdot e^{-b \cdot x}} = \frac{\frac{b}{a}}{1+\frac{b}{a} \cdot K \cdot e^{-b \cdot x}}$$

Vi definerer en konstant $C=\frac{b}{a} \cdot K$

$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-b \cdot x}}$$

```

---

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
En løsning med en ubestemt konstant til sidst. Denne konstant er et produkt af [[integralregning]]. Det kan også være $C$, der eksempelvis er en del af denne løsning, på differentiallignenen $y'=k \cdot y$.

$$f(x)=C \cdot e^{k \cdot x}$$

Dette er den ***fuldstændige*** løsning og $C$ er i dette tilfælde en variabel, der kan være **alle** tal. For at visualsiere den fuldstændige funktions natur, kan man tegne et [[hældningsfelt]].

For at finde den ***partikulære*** løsning


---
#matematik 

