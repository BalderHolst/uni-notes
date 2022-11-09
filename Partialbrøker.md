# Partialbrøker
At splittet en stor brøk op i mindre brøker det nemmere kan [[Integralregning|integreres]].


### Eksempel

$$\frac{3x+7}{(x+2)(x+3)}$$

Deler den op
$$\frac{3x+7}{(x+2)(x+3)}= \frac{A}{x+2} + \frac{B}{x+3}$$
$$\Updownarrow \text{ganger med venste nævner}$$
$$3x+7 = A(x+3) + B(x+2)$$
Sætter $x=-3$ og $x=-2$ ind
$$x=-3 \arrow 3(-3) + 7=B(-3 + 2) \arrow B = 2$$
$$x=-2 \arrow 3(-2) +7 =A(-2 + 3) \arrow A = 1$$
##### Samle Koefficienter
$$
\begin{align}
x &: \s 3 = A+B \\
1 &: \s 7 = 3A+2B
\end{align}
$$

### Eksempel 2
$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)}$$
$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)} = \frac{A}{x+1} + \frac{B}{x+2} + \frac{C}{(x+1)^{2}}$$
Ganger med venstre nævner
$$x^{2}-3x+3 = A(x+1)(x+2) + B(x+1)^{2}+ C(x+2)$$
Sætter interessante værdier ind for $x$
$$
\begin{align}
x = -1 &\arrow C=7 \\
x = -2 &\arrow B=13 \\
x = 0 &\arrow 3 = 2A + B + 2C \arrow A = -12
\end{align}
$$
Altså kan vi omskrive udtrykket således
$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)} = \frac{-12}{x+1} + \frac{13}{x+2} + \frac{7}{(x+1)^2}$$
