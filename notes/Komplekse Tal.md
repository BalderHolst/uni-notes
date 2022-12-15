# Komplekse Tal
[[Calculus 9th.pdf#page=1083]]

$$w = a + ib, \s i^2 = -1$$
Her er $a$ og $b$ **rigtige** tal.

Kan også skrives på [[#Polær Form]]

**BRUG ALDRIG $i = \sqrt{-1}$ SOM DEFINITION**

$$Re(w) = Re(a+ib)= a, \s Im(w) = Im(a+ib)  = b$$
*Intet $i$ i den imaginære del*


---

Tager udgangspunkt i [[Andengradspolynomier]] der har løsninger hvor diskriminanten er **negativ**.

$$x = \frac{-b \pm i \sqrt{-d}}{2a}$$

>[!Note]- Eksempel
>
>Dette er andengradsligninen
>$$2z^2 + 4z + 10 = 0$$
>
>Dette er så [[Andengradspolynomier#Diskriminanten|diskriminanten]]
>$$d = b^2 - 4ac= -64$$
>
>Altså er dette løsningen
>$$x = \frac{-b \pm i \sqrt{-(d)}}{2a} = -1 \pm 2i$$
### Den kompleks konjugerede
Hvis $z$ er et komplekst tal af form $z = a +ib$, så er den kompleks konjugerede $\bar{z} = a-ib$

Hvis et polynomium med reelle koeficienter, dvs $x^n + bx^{n-1} + \dots$ så $\{a,b, \dots\}$ alle er en del af $\R$. Har komplekse rødder, så forekommer disse altid som kompleks konjugerede par. (F.eks. i imaginære løsninger på andengradspolynomier).

### Mængden
Mængden af komplekse tal har symbolet $\C$.

### Addition
Hvis $z_1 = a+ib$ og $z_2 = c-id$, så er kan de *lægges sammen* sådan:
$$z_1 + z_2 = a + ib + c-id = a+c+i(b+d)$$

### Subtraktion
Hvis $z_1 = a+ib$ og $z_2 = c-id$, så er kan de *trækkes fra hinanden* sådan:
$$z_1 - z_2 = a + ib - c-id = a-c+i(b-d)$$

### Multiplikation
Hvis $z_1 = a+ib$ og $z_2 = c-id$, så er kan de *ganges sammen* sådan:

$$z_1 \cdot  z_2 = (a+ib)(c-id) = ac - iad + ibc + - i^2bd$$
$$ = ac + i^2bd + i(ac+bc)$$
Vi indfører $i^2 \rightarrow -1$

Dette er altså udtrykket
$$z_1 \cdot z_2 = ac - bd + i(ad+bc)$$

##### Multiplikation med [[#den kompleks konjugerede]]
$$z_1 \cdot  \bar{z_1} = (a+ib)(a-ib) = a^2 - i^2b^2 - \c{aib} + \c{aib} = a^2 + b^2$$
Resultatet er **reelt**!

### Division
Hvis $z_1 = a+ib$ og $z_2 = c+id$, så er kan de *divideres* sådan:
$$\frac{z_1}{z_2} = \frac{a + ib}{c + id}$$
**Forlæger men den kompleks konjugerede**
$$\frac{(a+ib)(c-id)}{(c+id)(c-id)}$$
Ganger ud
$$= \frac{ac -i^2bd + i(ab-ad)}{c^2-d^2} = \frac{ac+bd+i(bc+ad)}{c^2 + d^2}$$
Vi har nu en reel ($\R$) nævner

---

## Polær Form
Det komplekse tal $z = a+ib$ med $|z| = M$ og $arg(z) = \theta$ kan skrives på polær form.
$$z=M\cos(\theta) + iM\sin(\theta)$$
Eller vha. eksponentialfunktion.
$$z=M \cdot e^{i\theta}$$
Det kan nemt skrives som
$$z=M\angle\theta$$

##### Modulus
De komplekse tal $z=a+ib$ afbildeles i et Argand diagram . Afstanden fra orego til punktet kaldes modulus ($|z|$).

$$|z| = \sqrt{a^2 + b^2}$$
##### Argumentet
Linjen fra orego til punktet $(a,b)$ svarende til det komplekse tal $z = a+ib$ danner en vinkel med den positive del af den reelle akse (1. aksen). Vinklen ($\theta$) kaldes for *argumentet til $z$*
$$arg(z) = \theta$$
($\theta$ skal være i intervallet $[-\pi,\pi]$) 

Bestemmes således
$$arg(z)= \theta =\tan^{-1}\left(\frac{Im(z)}{Re(z)}\right) + p\pi, \s p \in \{-1,0,1\}$$



>[!Example]- Opgaver med polær form
>- [[Aflevering 1 - rettet.pdf#page=1]]
>- [[Aflevering 1 - rettet.pdf#page=4]]
>- [[Aflevering 1 - rettet.pdf#page=6]]

>[!note]- Operationer i Polær form
>### Multiplikation
$$z_1 \cdot z_2 = M_1 \cdot  e^{i\theta_1} \cdot  M_2 \cdot  e^{i\theta_2} = M_1 \cdot  M_2 \cdot  e^{i(\theta_1 + \theta_2)}$$
På den anden form:
$$M_1(\cos\theta_1 + i\sin\theta_1) \cdot M_2(\cos\theta_2 + i \sin\theta_2)$$
$$\Updownarrow$$
$$M_1M_2(\cos\theta_1 \cos\theta_2 - \sin \theta_1 \sin\theta_2 + i(\sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2))$$
$$\Updownarrow$$
$$M_1M_2(\cos(\theta_1 + \theta_2)+i \sin(\theta_1 + \theta_2))$$
>### Division
$$\frac{z_1}{z_2} = \frac{M_1 \cdot e^{i\theta_1}}{M_2 \cdot e^{i\theta_2}} = \frac{M_1}{M_2} \cdot e^{i(\theta_1-\theta_2)}$$
>### Eksponentiering
>$$z=M \cdot e^{i\theta}$$
>$$z^n = (M \cdot e^\theta)^n = M^n \cdot e^{i\theta \cdot n} = M^n (\cos(\theta n) + i\sin(\theta n))$$




### de Moivre's Formel
$$
\begin{align}
z^n = r^n \cdot (\cos(\theta) + i \cdot \sin(\theta))^n &\arrow \text{Flere løsninger}\\
z^n = r^n \cdot (\cos(n\theta) + i \cdot \sin(n\theta)) &\arrow \text{Én løsning}
\end{align}
$$
$\theta$ : Argumentet

##### Løs en ligningen



>[!Example]- Opgaver med de Moivre's Formel
>- [[Aflevering 1 - rettet.pdf#page=2]]
>- [[Aflevering 1 - rettet.pdf#page=4]]

>[!Note]- Bevis
>
>#### Bevis (induktion)
>
>##### Initialisering 
>$$n = 1,\s z = \cos(\theta) + i \sin(\theta)$$
>$$z^1= (\cos(\theta) + i \sin(\theta))^1 \arrow \text{sandt!}$$
>##### Induktions skridt
>*Antager*: [[#de moivre's formel]] er sand for tallet $k$.
>
>Altså
>$$z^k= (\cos(\theta) + i \sin(\theta))^k \arrow \text{Antages sandt}$$
>Lad nu $n = k +1$
>$$(\cos(\theta) + i \sin(\theta))^{k+1} \s=\s (\cos(\theta) + i \sin(\theta))^{k} \cdot (\cos(\theta) + i \sin(\theta))^{1}$$
>Bruger de Moivre (som er antaget sandt)
>$$= (\cos(k\theta) + \sin(k\theta)) \cdot (\cos(\theta) + i \sin(\theta))$$
>$$= \cos(k\theta) \cdot \cos(\theta) - \sin(k\theta) \cdot \sin(\theta) + i(\cos(k\theta) \cdot \sin(\theta) + \sin(k\theta) \cdot \cos(\theta))$$
>De to led kan omskrives således (blander cos og sin)
>$$\cos(k\theta+\theta)+i\sin(k\theta + \theta) \s=\s \cos((k+1)\theta) + i\sin((k+1)\theta)$$
>Altså (da $n = k +1$)
>$$\cos(n\theta) + i\sin(n\theta)$$
>


#### For rationelle tal
$$z^{\frac{p}{q}} = r^{\frac{p}{q}}\cdot (\cos((\frac{p}{q} \cdot \theta) + i \sin(\frac{p}{q} \cdot \theta))$$



---

### Komplekse løsninger
> *En ligning med kompleks løsning (eller med komplekse tal som indgår i ligningen*

Løsningers vinkel ($\theta$) vil altid være jævnt fordelt på den imaginære "cirkel".
![|220](https://i.stack.imgur.com/uOKmym.jpg)




>[!Note]- Eksempel: løs en ligning med [[#de Moivre's Formel]]
>
>##### Eksempel 1
>Løs dette som kompleks ligning
>$$z^2 = 4$$
>1. Bestem [[#Modulus]]
>$$|z^2| = |4| = \sqrt{4^2 + 0^2} = 4$$
>2. Bestem [[#Argumentet]]
>$$arg(z^2) = arg(4) = \tan^{-1}\left(\frac{0}{4}\right) = 0$$
>3. Opskriver løsningen på [[#Polær form]]
>$$z^2 = |z^2| (\cos(arg(z^2) + 2\pi p) + i\sin(arg(z^2)+2\pi p), \s p \in \Z$$
>Sætter argumentet og modulus ind i forml
>$$z^2 = 4(\cos(0 + 2\pi p) + i\sin(0+2\pi p), \s p \in \Z$$
>Hvis vi ser på [[#de Moivre's Formel]] må dette være sandt
>$$z^n = r^n (cos(n\theta) + i \sin(n\theta)) \arrows z^2 = r^2 (cos(2\theta) + i \sin(2\theta))$$
>Ved at sammenligne de to formler ser vi at de står på samme form. Vi kan altså nu aflæse værdier for $r^2$ og $2\theta$.
>$$r^2 = 4 \arrow r = 2$$
>Bemærk at $r$ *ikke kan være negativ*, da det er modulus for de komplekse løsninger.
>$$2\pi p = 2\theta \arrow \theta = \pi p$$
>Find værdier for $p$ der går at $\theta \in [-\pi, \pi]$
>$$p = 0: \s \theta_1 = \pi \cdot 0 = 0$$
>$$p = 1: \s \theta_2 = \pi \cdot 1 = \pi$$
>Dette er altså vores løsninger på [[#polær form]]:
>$$
>\begin{align}
>z_1 &= r \cdot e^{i \cdot \theta_1} = 2 \cdot e^{i \cdot 0} = 2\\
>z_2 &= 2 \cdot e^{i \cdot \pi}
>\end{align}
>$$
>
>

>[!Note]- Eksempel (gange med den reciprokke) 
>
>### Eksempel (gange med den reciprokke)
>$$z = \cos(\theta) + i\sin(\theta)$$
>$$z + \frac{1}{z} = z + z^{-1} = \cos(\theta) + {i\sin(\theta)} + \cos({-\theta}) + i\sin(-\theta) $$
>Cos er lige, sin er ulige
>$$\cos(\theta) + \c{i\sin(\theta)} + \cos({-\theta}) \c{- i\sin(\theta)} $$
>Altså
>$$z + \frac{1}{z} = 2\cos{\theta}$$
>
>

### Elektronik
Bruger $j$ i elektronik.

### Det Komplekse Plan
[[Det Komplekse Plan]]



---
#matematik 