# Tretrinsraketten
En metode til at differentiere funktioner i hånden der gør brug af [[Differentialregning#Definition af et Differentiale|definitionen af en differentieret funktion]].

I dette eksempel vil jeg bruge funktionen $f(x) = 3x^2$

## Trin 1
find $f(x_0 + h) - f(x_0)$

$$f(x_0 + h) - f(x_0) = 3 (x_0+h)^2-3x_0^2 = 3 \cdot (h^2 + 2 \cdot h \cdot x_0 + x_0^2)-3x_0^2 = 3 \cdot h^2 + 6 \cdot h \cdot x_0 + \bcancel{3 \cdot x_0^2} - \bcancel{3 \cdot x_0^2}$$

Til sidst bliver det til

$$f(x_0 + h) - f(x_0) = 3h^2 + 6 h x$$

## Trin 2
Find $\frac{f(x_0 + h) - f(x_0)}{h}$


$$\frac{f(x_0 + h) - f(x_0)}{h} = \frac{3h^{\bcancel{2}} + 6 \bcancel{h} x}{\bcancel{h}} = 6x + 3h$$

## Trin 3
Find grænseværdien $\lim_{h\to 0} \left(  a=\frac{f(x_0+h)-f(x_0)}{h} \right)$

$$\lim_{h\to 0} (6x+3h)$$

Fordi at $h$ er uendelig lille kan vi antage at hvis det ganges med noget, så bliver det så tæt på $0$ at det er ubetydeligt. Derfor kan vi undlade alle led der ganges med $h$.

$$f'(x) = 6x$$


---

Dette er en ret besværlig måde at regne differentialer ud i hånden, man kan med fordel bruge [[Differentialregning Regneregler|regneregler]] i stedet.












---
##### Tags
#matematik