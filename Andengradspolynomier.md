# Andengradspolynomier
[[Parabeler]]
### Forskrift
$$f(x) = ax^2 + bx + c$$

$a$ = hældnings factor (bestemmer også retning af grafen, $a \neq 0$) 
$b$ = hældningen i $x = 0$
$c$ = skæringspunkt med $y$-aksen

Grafen som et andengradspolynomie beskriver kaldes en parabel

### Toppunktet
Punktet hvor hældingen er 0

**Formel**
$$\left( \frac{-b}{2a}, \frac{-d}{4a} \right)$$

```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

##### Bevis

Dette er funktionen for et andengradspolynomium
$$f(x) = ax^2+bx+c$$
Vi differentierer
$$f'(x)=2ax+b$$
Vi ved at hældningen skal være $0$ i toppunktet, derfor sætter vi $f'(x)$ til $0$
$$0 = 2ax+b$$
Isolerer $x$
$$x=\frac{-b}{2a}$$
Dette er altså toppunktets $x$-koordinat. 

Vi kan nu sætte dette ind i funktionsforskriften og finde toppunktets $y$-værdi

$$f(x)=a \cdot \left(\frac{-b}{2a} \right)^2 + b \cdot \left(\frac{-b}{2a} \right) + c$$
Simplificerer
$$f(x)=a \cdot \frac{(-b)^2}{2^2 \cdot a^2} + \frac{-b^2}{2a} + c \arrows f(x)=\cdot \frac{\c{a} \cdot b^2}{4a^\c{2}} + \frac{-b^2}{2a} +c$$
Det er nu sådan ud.
$$f(x)=\cdot \frac{b^2}{4a} + \frac{-b^2}{2a} + c$$
For at lægge ledene sammen skal de have fællesnævner
$$f(x)=\frac{b^2}{4a} + \frac{-2b^2}{4a} + \frac{4ac}{4a} = \frac{-b^2+4ac}{4a}$$
Dette er altså udtrykket for toppunktets $y$-koordinat

Vi kan nu omskrive $-b^2 +4ac$ til $-d$

Altså er dette udtryk for toppunktet:
$$\left(\frac{-b}{2a}, \frac{-d}{4a} \right)$$



```


### Diskriminanten
Diskriminanten angiver antallet af "rødder" parablen

$$d = b^2 - 4ac$$

Diskriminantens størrelse bestemmer antallet af nulpunkter/rødder

| d       | Rødder |
| ------- | ------ |
| $d < 0$ | $0$    | 
| $d = 0$ | $1$    |
| $d > 0$ | $2$    |

[[#Løsningsformlen]] kan brudes til at bestemme rødderme.



### Løsningsformlen
$$x = \frac{-b \pm \sqrt{d}}{2a}$$

se [[Bevis for Løsningsformlen|beviset]].

---
##### Se også
- [[Linære Funktioner]]
- [[Polynomier i Højere Grad]]

---
##### Tags
#matematik
#funktioner