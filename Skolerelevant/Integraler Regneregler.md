# Integraler Regneregler
---
Husk at lægge $k$ til alle ubestemte integraler

### Integration af Led
led er sepereret af $+$

| $$f(x)$$                     | $$\int f(x)\,dx$$                                   |
| -------------------------- | ------------------------------------------------- |
| $$a$$                        | $$a \cdot x$$                                       |
| $$ln(x)$$                    | $$x \cdot ln(x)-x$$                                 |
| $$e^x$$                      | $$e^x$$                                             |
| $$e^{k\cdot x}$$             | $$\frac{1}{k}e^{k\cdot x}$$                         |
| $$x^a$$                      | $$\frac{1}{a+1}x^{a+1}$$                            |
| $$\frac{1}{x} = x^{-1}$$     | $$ln \lvert x \rvert$$                              |
| $$\sqrt{x}=x^{\frac{1}{2}}$$ | $$\frac{2}{3}x\sqrt{x}=\frac{2}{3}x^{\frac{3}{2}}$$ |
| $$cos(x)$$                   | $$sin(x)$$                                          |
| $$sin(x)$$                   | $$-cos(x)$$                                                  |

### Brugbare sætninger (ubestemt integrale) 

| Sætning                                                             | Forklaring                                                                       |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| $$\int f(x)\,dx = F(x) + k$$                                        | Husk $k$!                                                                        |
| $$\int k \cdot f(x)\,dx = k \cdot \int f(x)\,dx$$                   | Man kan sætte alt man ganger med uden for integralet, og gange det ind bagefter. |
| $$\int (f(x) + g(x))\,dx = \int f(x)\,dx + \int g(x)\,dx$$          | Integraler kan deles op over '$+$' (og '$-$')                                    |
| $$\int f(g(x))\cdot g'(x)\,dx = \int f(t)\,dt\text{, hvor }t=g(x)$$ | Sætning til [[Integration med Substidution]]                                     |                                                                              |

### Brugbare sætninger (bestemt integrale) 

| Sætning                                                                                      | Forklaring                                                    |     |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --- |
| $$\int_{a}^{b} f(x) \,dx = F(b) - F(a)$$                                                     | Finder hvor meget $f(x)$ er vokest i intervallet $a < x < b$. |     |
| $$\int_{a}^{b}f(x)\,dx = \int_{a}^{c}f(x)\,dx + \int_{c}^{b}f(x)\,dx$$                       | Man kan dele integralet op                                    |     |
| $$\int_{a}^{b} k \cdot f(x)\,dx = k \cdot \int_{a}^{b} f(x)\,dx$$                            | Ligesom det bestemte integrale                                |     |
| $$\int_{a}^{b} (f(x) + g(x))\,dx = \int_{a}^{b} f(x)\,dx + \int_{a}^{b} g(x)\,dx$$           | Bestemte integraler kan også deles op over '$+$' (og '$-$')   |     |
| $$\int_{a}^{b} f(g(x))\cdot g'(x)\,dx = \int_{g(a)}^{g(b)} f(t)\,dt \text{, hvor }  t=g(x)$$ | Sætning til [[Integration med Substidution]]                  |     |




---
##### Se også
- [[Integralregning]]



---
##### Tags
#matematik 