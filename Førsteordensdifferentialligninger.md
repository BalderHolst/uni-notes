# Førsteordensdifferentialligninger	
[[Linære førsteordensdifferentialligninger]]

#### Eksempel
$$y' - 2y = 6x$$
Her er $x$ den uafhængige variabel og $y$ den afhængige.

### Seperable Diff-ligninger
Generel Førsteordens diff-lign.
$$\frac{dy}{dx} = h(x,y)$$
Ligningen er *seperabel* hvis det gælder at
$$h(x,y)=g(y) \cdot f(x)$$
Den løses ved at dividere med $g(y)$.
$$\frac{dy}{dx} =g(y) \cdot f(x) \arrows \frac{1}{g(y)} \frac{dy}{dx} = f(x)$$
Vi tager integralet.
$$\int \frac{1}{g(y)} \cdot \frac{dy}{\c{dx}} \cdot  \c{dx}=\int f(x)dx$$
Altså er må dette være sandt
$$\int f(x)= \int \frac{1}{g(y)}dy$$
```ad-example # Admonition type. See below for a list of available types.
title:                  Eksempel
collapse:               # Create a collapsible admonition.

##### Eksempel
$$\frac{dy}{dx} = \frac{x}{y}$$
Før $y$'erne over på venstre side
$$y \cdot dy= x \cdot dx$$
Integrerer
$$\int y \cdot dy= \int x \cdot dx \arrows \frac{1}{2}y^2= \frac{1}{2}x^2+c$$

Isolerer $y$
$$y^2=x^2+2c \arrows y=\pm \sqrt{x^2+2c}$$

Vi kunne nu sætte et punkt in for at finde den *partikulære* løsning.
```

---
#matematik
