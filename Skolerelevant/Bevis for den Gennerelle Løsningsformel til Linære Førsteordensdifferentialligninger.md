### Bevis for den Gennerelle Løsningsformel til [[Linære førsteordensdifferentialligninger]]

Vi beviser at $f(x) = e^{-A(x)} \cdot \int b(x)  \cdot e^{A(x)}dx$ er en løsning på differentialligningen $y' = a(x)$

Hvis $f(x)$ er en løsning til $y' + a(x) \cdot y = b(x)$, må det gælde at $f'(x) + a(x) \cdot f(x) = b(x)$.

**God ide:** gang med $e^{A(x)}$ på begge sider.

$$f'(x) \cdot e^{A(x)} + a(x) \cdot f(x) \cdot e^{A(x)} = b(x) \cdot e^{A(x)}$$

**Anden god ide:** nu ser vi på hjælpefunktionen $g(x) = e^{A(x)}$

Vi differentierer hjælpefunktionen (det er to funktiner, se [[Differentialregning Regneregler#Differentiation af sammensatte funktioner]])

$$\left(g(x)  \cdot  e^{A(x)}\right)' = g'(x) \cdot e^{A(x)} + g(x) \cdot e^{A(x)} \cdot a(x)$$

Vi kan nu se at dette differentierede udtryk, er præcis det samme som venstresiden i vores ligning. Derfor kan vi omskrive ligningen således.

$$\left(f(x)  \cdot  e^{A(x)}\right)' = b(x) \cdot e^{A(x)}$$

Nu integrerer vi (differentialet går ud med integralet)
$$\int  \left(f(x)  \cdot  e^{A(x)}\right)'dx = \int b(x) \cdot e^{A(x)}dx \arrows f(x)  \cdot  e^{A(x)} = \int b(x) \cdot e^{A(x)}dx$$

Isolerer $f(x)$
$$f(x) = \frac{1}{e^{A(x)}} \cdot \int b(x) \cdot e^{A(x)}dx$$

Omskriver $\frac{1}{e^{A(x)}}$ til $e^{-A(x)}$

$$f(x) = e^{-A(x)} \cdot \int b(x) \cdot e^{A(x)}dx$$

Dette er altså løsningen på differentialligningen.

---
#matematik 