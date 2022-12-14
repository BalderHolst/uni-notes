# Partialbrøker
At splittet en stor brøk op i mindre brøker det nemmere kan [[Integraler|integreres]].

Brøken ***skal*** være [[Rationelle Funktioner#Ægte eller Uægte Polynomiumsbrøk|ægte]].

$$\frac{P(x)}{(x-a)(x-b)^{2}(x^{2}+cx+d)} = \frac{A}{x-a} + \frac{B}{x-b} + \frac{C}{(x-b)^{2}}+ \frac{D}{x^{2}+cx+d}$$
$P(x)$ : Et polymonium

>[!video]- Opsplitning i partial brøker - Video
><iframe width="560" height="315" src="https://www.youtube.com/embed/dDjz_PXA_6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

>[!video]- Omskrivning af uægte brøk til ægte - Video
><iframe width="560" height="315" src="https://www.youtube.com/embed/acCslvFwbts" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Integration af Rest-brøken
$$
\begin{align}
\int \frac{1}{ax+b} dx &= \frac{1}{a} \ln|ax+b|+k \\ \\
\int \frac{x}{x^{2}+a^{2}}dx &= \frac{1}{2} \ln(x^{2}+ a^{2})+ k \\ \\
\int \frac{x}{x^{2}- a^{2}} dx &= \frac{1}{2}\ln|x^{2} - a^{2}| + k
\end{align}
$$

>[!note]- Henrik viser og differentierer disse udtryk
><iframe width="560" height="315" src="https://www.youtube.com/embed/47PmQ5NJBnI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
 
>[!example]- Eksempel 1
>$$\frac{3x+7}{(x+2)(x+3)}$$
>
>Deler den op
>$$
>\begin{align}
>\frac{3x+7}{(x+2)(x+3)}&= \frac{A}{x+2} + \frac{B}{x+3} \\ \\
>&\Updownarrow \s \text{ganger med venstre nævner} \\ \\
>3x+7 &= A(x+3) + B(x+2)
>\end{align}
>$$
>Sætter $x=-3$ og $x=-2$ ind
>$$x=-3 \arrow 3(-3) + 7=B(-3 + 2) \arrow B = 2$$
>$$x=-2 \arrow 3(-2) +7 =A(-2 + 3) \arrow A = 1$$
>##### Samle Koefficienter
>$$
>\begin{align}
>x &: \s 3 = A+B \\
>1 &: \s 7 = 3A+2B
>\end{align}
>$$

>[!example]- Eksempel 2
>$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)}$$
>$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)} = \frac{A}{x+1} + \frac{B}{x+2} + \frac{C}{(x+1)^{2}}$$
>Ganger med venstre nævner
>$$x^{2}-3x+3 = A(x+1)(x+2) + B(x+1)^{2}+ C(x+2)$$
>Sætter interessante værdier ind for $x$
>$$
>\begin{align}
>x = -1 &\arrow C=7 \\
>x = -2 &\arrow B=13 \\
>x = 0 &\arrow 3 = 2A + B + 2C \arrow A = -12
>\end{align}
>$$
>Altså kan vi omskrive udtrykket således
>$$\frac{x^{2}-3x+2}{(x+1)(x+2)(x+1)} = \frac{-12}{x+1} + \frac{13}{x+2} + \frac{7}{(x+1)^2}$$

---
#matematik #integraler 