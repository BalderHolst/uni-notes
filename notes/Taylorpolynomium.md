# Taylorpolynomium
$n$'te grads taylorpolynomium udvikles om $x = a$.
$$P_{n}(x) = f(a) + \frac{f'(a)}{1!}(x-a)^{1}+ \frac{f''(a)}{2!}(x-a)^{2}+ \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$

[[Linarisering]] benytter et førstegrads taylorpolynomium

Hvis man tager nok led med kan man i ***nogle*** tilfælde finde et præcist udtryk for funktionen.

## Fejlvurdering (Taylors Sætning)

##### Maksimal fejl
$$|E(x)| \leq \frac{|f^{(n+1)}(s_{maks})|}{(n+1)!}(x-a)^{n+1}$$
$s_{maks}$ : Den $s$-værdi, der giver den største fejl.

##### Fortegn for fejl
Check fortegnet på $|f^{(n+1)}(s)| \cdot (x-a)^{n+1}$. Dette er fortegnet på fejlen.

##### Generel formel
Hvis $f^{(n+1)}(t)$ eksisterer for alle $t$ i et interval indeholdende $a$ og $x$, og hvis $P_{n}$ er et $n$'te grad polynomium $P_{n}(x)$ for $f(x)$ omkring $x=a$, så er
$$E_{n}(x) = \frac{|f^{(n+1)}(s)|}{(n+1)!}(x-a)^{n+1} \s s \in \,]a,x[$$
***$s$ kan og skal ikke findes***

#### Metode
1. Plot $f^{(n+1)}(s)$
2. Find den $s$ der giver maksimal fejl ($s_{maks}$)
3. Set $s_{maks}$ in på $s$'s plads i formlen, og beregn fejlen
4. Lav eventuelt inverval for den sande værdi

>[!example]- Eksempel - Taylorpolynomium om et punkt
>Tredjeordens taylorpolynomiun for $f(x) = e^{x}$ om $x=0$, vurder fejlen i $x=1$.
>
>$$P_{3}=\frac{f'(a)}{1!}(x-a)^{1}+ \frac{f''(a)}{2!}(x-a)^{2} + \frac{f'''(a)}{3!}(x-a)^{3}$$
>$$= \frac{f'(0)}{1!}(x-0)^{1}+ \frac{f''(0)}{2!}(x-0)^{2} + \frac{f'''(0)}{3!}(x-0)^{3}$$
>$$= 1 + x + \frac{1}{2} x^{2}+ \frac{1}{6} x^{3}$$
>Finder approximation i punktet $x=1$
>$$P_{3}(1) = 1 + 1 + \frac{1}{2} + \frac{1}{6} \approx 2.66667$$
>
>##### Fejl
>$$E_{3} = \frac{f''''(s)}{4!}(x-0)^4$$
>$$|E_{3}(x)| \leq \frac{|f''''(s)|}{24}x^{4}$$
>$f''''(x)$ er *voksende* overalt
>$f''''(x)$ er *positiv* overalt
>
>$e^{1} < e^{0}$, dvs. $s=1$ maksimerer $e^{s}$ i intervallet $[0,1]$.
>
>$$|E_{3}(x)| \leq \frac{e}{24}x^{4}$$
>$$|E_{3}(1)| \leq \frac{e}{24} \cdot 1^{4} = \frac{e}{24} \approx 0.11326$$
>
>Er fejlen positiv eller negativ?
>$$(x-0)^{4} > 0 \s \text{og} \s f''''(s) = e^{s} > 0$$
>Fejlen er positiv

---
#matematik #approximation
