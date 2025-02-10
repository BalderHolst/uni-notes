# Linarisering
En linearisering er tangenten i et punkt
$$L(x) = f(a)+f'(a) \cdot (x-a)$$
$a$: $x$-værdien i punktet.

Vi bruger denne tangent i stedet for den komplicerede funktion, til at estimere funktionen (bedst omkring punktet).

Dette er et førstegrads [[Taylorpolynomium]]

>[!example]- Eksempel
>Bestem en approksimativ værdi at $\sqrt{26}$ vha. linarisering af $f(x) = \sqrt{x}$ omkring $x=25$.
>$$f'(x) = \frac{1}{2\sqrt{x}}$$
>$$f'(25) = \frac{1}{10}$$
>$$f(25)=5$$
>Sætter ind i formlen
>$$L(x)=f(25)+f'(25)(a-25)=5+ \frac{1}{10} (x-25)$$
>
>$$L(26)=5+\frac{1}{10} (26-25)=5+ \frac{1}{10}=5.1 \arrow \sqrt{26} \approx 5.1$$
>
>#### Fejlvurdering
>
>$$L(26) = 5.10$$
>$$f'(x) = \frac{1}{2\sqrt{x}}$$
>$$f''(x) = \frac{-1}{4} \cdot \frac{1}{x\sqrt{x}}$$
>Fejlen
>$$|E(x)| \leq \frac{|f''(s_{maks})|}{2}(x-a)^{2}$$
>
>Plot af $f''(x)$:
>```mathpad
>plot(-1/4 * 1/(x*sqrt(x)))==?
>```
>
>Dvs. $|f''(s)|$ er størst ved små $s$.
>$$|f''(25)| > |f''(26)|$$
>og $f''(x)$ er voksende overalt
>
>Altså er dette størrelsen på fejlen
>$$|E(x)| \leq \frac{f''(25)}{2}(x-25)^{2} = \frac{1/500}{2}(x-25)^{2}$$
>Altså
>$$|E(26)| \leq \frac{1}{1000} (26-25)^{2} = \frac{1}{1000}$$
>##### Fortegn
>
>$f''(s) < 0$ for alle $s>0$.
>
>Altså er fejlen *negativ*:
>
>$$E(x) = f(x) - L(x) < 0 \arrows f(x) < L(x)$$
>Den sande værdi findes altså inden for dette interval:
>$$]L(26) - E(26),\  L(26)[ \s = \s ]5.09902, \  5.1[$$
>

---

## Fejlvurdering

$$
\begin{align}
E &= \text{sand værdi} - \text{approximeret værdi}\\ \\
E &= f(x)-L(x)
\end{align}
$$

Vi kan ikke vinde denne sandeværdi ($f(x)$).

Derfor bruger vi disse formler til at finde den maksimale fejl i intervallet

$$
\begin{cases}
|f''(s)| &\leq k \s s \in \  ]a;x[ \\ \\
|E(x)| &\leq \frac{k}{2}(x-a)^{2}
\end{cases} \arrow |E(x)| \leq \frac{|f''(s_{maks})|}{2}(x-a)^2
$$
$|E(x)|$ : Størrelsen på fejlen
$s_{maks}$ : Den $s$-værdi, der resulterer i den største $|f''(s)|$, hvor $s$ ligger i intervallet $[x,a]$ eller $[a,x]$.
$a$ : $x$-værdien som $f(x)$ er linariseret omkring.


#### Fortegn
$$
\begin{align}
f''(s) < 0 \s \forall s \in [x, a] &\arrow \text{\textit{positiv} fejl} \\
f''(s) > 0 \s \forall s \in [x, a] &\arrow \text{\textit{negativ} fejl}
\end{align}
$$

##### Sætning
Hvis $f''(x)$ eksisterer for alle $t$ i et interval indeholdende $a$ og $x$, så eksisterer der et punkt $s$ mellem $a$ og $x$, således at
$$E(x)= \frac{f''(s)}{2}(x-a)^{2} \s s\in \  [a,x]$$

Dette er en **lorteformel** og den kan ikke anvendes.

Vi kender aldrig værdien for $s$. Derfor finder vi worstcasefejlen. Vi maksimerer altså $|f''(s)|$.


---
#matematik #differentialer #approximation
