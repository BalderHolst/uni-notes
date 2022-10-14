# Koblede Førsteordensdifferentialligninger


### Eksempel

$$\frac{dy}{dt} = k_1x+k_2y$$
$$\frac{dx}{dt} = k_3x+k_4y$$

Differentierer $x$ i den første differentialligning
$$x = \frac{1}{k_1} \frac{dy}{dt}-\frac{k_2}{k_1}$$

Vi differentierer med henhold til $x$
$$\frac{dx}{dt} = \frac{1}{k_1} \frac{d^2y}{dt^2}-\frac{k_2}{k_1}\frac{dy}{dt}$$

Indsæt $x$ og $\frac{dx}{dt}$ i ligning $2$.
$$\frac{1}{k_1} \frac{d^2y}{dt^2}-\frac{k_2}{k_1}\frac{dy}{dt} = k_3\left(\frac{1}{k_1} \frac{dy}{dt}-\frac{k_2}{k_1}y \right) - k_4y$$

Simplificerer
$$\frac{1}{k_1} \frac{d^2y}{dt^2} - \frac{dy}{dt} \left(\frac{k_2}{k_1} + \frac{k_3}{k_1} \right) + y\left(\frac{k_2 k_3}{k_1} +k_4\right) = 0$$
$$\Updownarrow$$
$$\frac{d^2y}{dt^2} - \frac{dy}{dt}(k_2+k_3) + y(k_2k_3+k_1k_4) = 0$$
Du kan det løses med [[Linære førsteordensdifferentialligninger#1 Generel løsningsformel|denne]] formel.

---
#matematik 