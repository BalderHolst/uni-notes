# Linarisering
En linearisering er tangenten i et punkt
$$L(x) = f(a)+f'(a) \cdot (x-a)$$
$a$: $x$-værdien i punktet 

Vi bruger denne tangent i stedet for den komplicerede funktion, til at estimere funktionen (bedst omkring punktet).

>[!example]- Eksempel
>Bestem en approksimativ værdi at $\sqrt{26}$ vha. linarisering af $f(x) = \sqrt{x}$ omkring $x=25$.
>$$f'(x) = \frac{1}{2\sqrt{x}}$$
>$$f'(25) = \frac{1}{10}$$
>$$f(25)=5$$
>Sætter ind i formlen
>$$L(x)=f(25)+f'(25)(a-25)=5+ \frac{1}{10} (x-25)$$
>
>$$L(26)=5+\frac{1}{10} (26-25)=5+ \frac{1}{10}=5.1 \arrow \sqrt{26} \approx 5.1$$

---

## Fejlvurdering

$$
\begin{align}
E &= \text{sand værdi} - \text{approximeret værdi}\\ \\
E &= f(x)-L(x)
\end{align}
$$

Vi kan ikke vinde denne sandeværdi ($f(x)$).

##### Sætning
Hvis $f''(x)$ eksisterer for alle $t$ i et interval indeholdende $a$ og $x$, så eksisterer der et punkt $s$ mellem $a$ og $x$, således at
$$E(x)= \frac{f''(s)}{2}(a-x)^{2}$$

Vi kender aldrig værdien for $s$. Derfor finder vi worstcasefejlen. Vi maksimerer altså $|f''(s)|$.

Hvis $|f''(s) \leq k|$ for alle $s \in \, ]a;x[$, så er $|E(x)| \leq \frac{k}{2}(x-a)^{2}$.

---
#matematik #differentialer 
