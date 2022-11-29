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

### Definitionsmængde

$$Dm(f(x_{1}, x_{2}, \dots, x_{n})) = \R^{n}\rightarrow \R$$


>[!example]- Eksempel med funktion
>$$f(x,y)=x \cdot y$$
>Definitionsmængden
>$$Dm(f) = \R \times \R$$
>Eksempel 2:
>$$g(x,y)=\sqrt{x} \cdot y$$
>$$dm(d)=[0;\infty[ \:\times\: \R$$

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
$$

### Skæringer med fladen
- [[Niveaukurver]]
- [[Snitkurver]]

### Grænseværdier
Når $f(x)$ nærmer sig $L$ for $(x,y) \to (a,b)$ , så
$$\lim_{(x,y)\to(a,b)}f(x) = L$$
Hvis "omegnen" af $(a,b)$ tilhører def-mængden $Dm(f)$.

a) Hver omegn af ($a$, $b$) indeholder åunkter i def-mængden $Dm(f)$.
b) For ethvert positivt tal $\epsilon$, eksisterer der et positivt tal $\delta = \delta(\epsilon)$, således at 
$$|f(x,y) - L| < \epsilon$$
er sandt når ($x$, $y$) er i def-mængden for $f$ og opfylder
$$0< \sqrt{(x-a)^{2}+(y-b)^{2}}$$

#### Fremgangsmåde til Opgaveløsning
- Kan vi komme til punktet $(a,b)$ fra forskellige sider, så skal det give det samme. 

##### Eksempel
$$\lim_{x}$$

---
#matematik #funktioner 
