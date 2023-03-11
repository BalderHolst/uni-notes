# Funktioner af flere Variable

>[!definition] 
>En funktion $f$ af $n$ reelle variable er en regel som tildeler ét unikt tal $f(x_{1}, x_{2}, \dots, x_{n})$ til hvert punkt $(x_{1}, x_{2}, \dots, x_{n})$ for en mængde $Dm(f)$.

I stedet for at en funktion afhænger af *en* variabel som $f(x)$, så afhænger disse funktioner af *flere* **uafhængige** variable.
$$f(x,y)$$
Her er de to uafhængige variabler $x$ og $y$. 

**HUSK**
$y$ er nu en **uafhængig** variabel. 

Funktionsværdien ($f(x,y)$) hedder som udgangspunkt $z$.


>[!Example]- Eksempler
>
>### Eks. 1
>Eksempel på en funktion af to variable
>$$f(x,y)=z=\sqrt{x} \cdot y$$
>
>### Eks. 2
>En funktion for volumet af en kasse med kvadratisk base
>$$V=h \cdot b^2$$
>$$\Updownarrow$$
>$$V(h,b)=h \cdot b^2$$
>
>

>[!Note]-  Differentiation
>
>![[Differentiation af funktioner med to variable]]
>

---

## Noter
```dataview 
list
from #funktionafflerevariable  
sort file.name
```

---


### Definitionsmængde

$$Dm(f(x_{1}, x_{2}, \dots, x_{n})) = \R^{n}\rightarrow \R$$


>[!example]- Eksempel med funktion
>$$f(x,y)=x \cdot y$$
>Definitionsmængden
>$$Dm(f) = \R \times \R$$
>Eksempel 2:
>$$g(x,y)=\sqrt{x} \cdot y$$
>$$dm(d)=[0;\infty[ \ \times\  \R$$

### Plot 
Funktioner af to variable skal tegnes i **3 dimensioner**

>[!Example]- Eksempel med Tabel
>$$
>\begin{array}{c|cccccc}
 x & 0 & 0 & 0 & 3 & \sqrt{3} & \sqrt{3} \\
 \hline
 y & 0 & -3 & 3 & 0 & -\sqrt{3} & \sqrt{3} \\
 \hline
 z & 3 & 0 & 0 & 0 & \sqrt{3} & \sqrt{3} \\
\end{array}
>$$

### Grænseværdier
Når $f(x)$ nærmer sig $L$ for $(x,y) \to (a,b)$ , så
$$\lim_{(x,y)\to(a,b)}f(x) = L$$
Hvis "omegnen" af $(a,b)$ tilhører def-mængden $Dm(f)$.

a) Hver omegn af ($a$, $b$) indeholder åunkter i def-mængden $Dm(f)$.
b) For ethvert positivt tal $\epsilon$, eksisterer der et positivt tal $\delta = \delta(\epsilon)$, således at 
$$|f(x,y) - L| < \epsilon$$

er sandt når ($x$, $y$) er i def-mængden for $f$ og opfylder
$$0< \sqrt{(x-a)^{2}+(y-b)^{2}} < \delta $$

En grænseværdi *eksisterer hvis den findes en relation* mellem $\delta$ og $\epsilon$.
$$\delta = f(\epsilon)$$


>[!tip]- God ide
>$$y^{2} \leq x^{2} + y^{2}$$
>Måske
>$$\delta = \epsilon $$



#### Fremgangsmåde til Opgaveløsning

##### Vis at Grænseværdien IKKE eksisterer
Kan vi komme til punktet $(a,b)$ fra forskellige sider, så skal det give det samme. Ellers eksisterer grænseværdien ikke.

>[!Example]- Eksempel
>$$\lim_{(x,y)\to(0,0)} = \frac{2xy}{x^2+y^2}$$
>1. $f$ er defineret for alle $(x,y)$ pånær $(0,0)$
>2. lad $(x,y)$ gå mod $0$ langs $y=x$ og $y=x^{2}$
>$y=x$
>$$f(x,x)= \frac{2xx}{x^{2}+ x^{2}} = \frac{2x^{2}}{2x^{2}} = 1$$
>$y=x^2$
>$$f(x,x^{2}) = \frac{2xx^{2}}{x^{2}+x^{2^{2}}} = \frac{2x}{1+x^{2}}= \frac{2}{\frac{1}{x} + x} = 0$$
>
>Da disse svar ikke er det samme, har punktet $(0,0)$ ikke defineret.

##### Vis at Grænseværdien EKSISTERER
Relater $\epsilon$ og $\delta$ med formlerne
$$|f(x,y) - L| < \epsilon$$
og
$$0< \sqrt{(x-a)^{2}+(y-b)^{2}} < \delta $$

---
#matematik #funktioner #emne 
