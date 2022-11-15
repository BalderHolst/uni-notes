#### Logistisk vækst

$$y'=y \cdot (b-ay) \arrows y'=ay \cdot (M-y), \text{ hvor } M = \frac{b}{a} \arrows y' = k \cdot y \left(1+ \frac{y}{M}\right)$$

##### Løsning
$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}} \arrows f(x)=\frac{M}{1+C \cdot e^{-bx}}$$

**Variabler**
$M$: grenseværdien/bærekapaciteten

Den maksimale væksthastighed er ved $f(x) = \frac{M}{2}$



>[!Note]- Plot
>
>Plot af en [[#Fuldstændig og partikulær løsning|partikulær løsning]]
>
>![[Logistisk Vækst.png]]
>
>[[Hældningsfelt]]
>
>![[Logistisk Hældnningsfelt.png]]
>


>[!Note]- Bevis
>
> Bevis for at dette er løsningen på differentialligningen
> 
> $$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}}, \s f(x) \ne 0$$
>
>Hvis $f(x)$ er en løsning til differentialligningen $y'=y \cdot (b-ay)$, må dette gælde (har bare sat $f(x)$ ind på $y$'s plads)
>
>$$y'=y \cdot (b-ay) \arrows f'(x)=f(x) \cdot (b-a \cdot f(x))$$
>
>Ganger $f(x)$ ind i parantesen
>
>$$f'(x)=f(x) \cdot b-a \cdot f(x)^2$$
>
>**God ide:** ganger med $-\frac{1}{f(x)^2}$ på begge sider
>
>$$-\frac{1}{f(x)^2} \cdot f'(x)=-\frac{1}{f(x)^{\c{2}}} \cdot \c{f(x)} \cdot b-\left(-\frac{1}{\c{f(x)^2}}\right) \cdot a \cdot \c{f(x)^2}$$
>
>$$-\frac{1}{f(x)^2} \cdot f'(x) = -\frac{1}{f(x)} \cdot b +a \arrows -\frac{1}{f(x)^2} \cdot f'(x) = a-\frac{1}{f(x)} \cdot b$$
>
>**Anden gode ide:** vi definerer en funktion $g(x) = \frac{1}{f(x)}$
>
>Vi differentierer $g(x)$, og opdager at $\frac{1}{f(x)}$, er en sammensat funktion. Derfor bruger vi [[Differentialregning Regneregler|regnereglen for sammensatte funktioner]].
>
>$$g'(x) = \left(\frac{1}{f(x)}\right)' = -\frac{1}{(f(x))^2} \cdot f'(x)$$
>
>Vi lægger nu mærke til at venstre side af vores ligning kan omskrives til $g'(x)$,  og at en del af andet led kan omskrives til $g(x)$.
>
>$$g'(x)=a-g(x) \cdot b$$
>
>Vi lægger mærke til at $g(x)$ er en løsning på den kendte differentialligning $y'=b-a \cdot y$. (dog er $a$ og $b$ byttet rundt her) [[Linære førsteordensdifferentialligninger#3 Løsningsformel Newtons Afkølingslov]]
>
>derfor må dette være sandt om $g(x)$ (bruger $K$ i stedet for $C$)
>
>$$g(x) = \frac{a}{b} + K \cdot e^{-b \cdot x}$$
>
>Da vi ved at $g(x) = \frac{1}{f(x)}$ må dette være sandt
>
>$$\frac{a}{b} + K \cdot e^{-b \cdot x} = \frac{1}{f(x)} \arrows f(x)=\frac{1}{\frac{a}{b} + K \cdot e^{-b \cdot x}}$$
>
>Vi forlænger nu brøken med $\frac{b}{a}$
>
>$$f(x) =\frac{1 \cdot \frac{b}{a}}{\frac{\c{b}}{\c{a}} \cdot \frac{\c{a}}{\c{b}} + \frac{b}{a} \cdot K \cdot e^{-b \cdot x}} = \frac{\frac{b}{a}}{1+\frac{b}{a} \cdot K \cdot e^{-b \cdot x}}$$
>
>Vi definerer en konstant $C=\frac{b}{a} \cdot K$
>
>$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-b \cdot x}}$$
>

---
#matematik #differentialligninger 