# Optimering

Gøre noget så småt som muligt eller så stort som muligt.

Det vigtige er at stille formler op der beskriver forskellige relationer mellem variablerne.

```ad-example # Admonition type. See below for a list of available types.
title:                  **Eksempel**
collapse:               # Create a collapsible admonition.

Eksempeltekst

```

### Eksempel 1:
Det hegn på 200m skal optimeres til at omramme det størst mulige areal

Hegnet et x langt og y bredt

Omkredsen
$$o = 200$$

Vi ved at arealet af et rektangel kan beskrives således
$$A = y \cdot x$$


Læg mærke til at $2y + 2x = 200$ beskriver længderne på hegnets sider. Fordi der kun er to variabler, kan vi omskrive y, sådan:
y = 100 - x




y := 100 - x;


A := x -> y*x;


A(x);
 = 
                          (100 - x) x




plot(A(x), x = 0 .. 100);

xo := solve(diff(A(x), x) = 0);
 = 
                            xo := 50





A(50);
 = 
                          5000 - 50 x

