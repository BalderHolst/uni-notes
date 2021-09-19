Redegør: Forklar med matematiske beviser el.lign.

Forklar: Forklar som du vil, f.eks. med eksempler

# Polynomier og andengradsligninger

> Gør rede for andengradspolynomiets graf og nulpunkter. Udled formlen
> til løsning af andengradsligninger.

Forskrift: $y = ax^{2} + bx + c$

$a$ angiver om hvorledes parablen er 'sur' eller 'glad'. Som positiv er
parablen 'glad' og negativ som 'sur'. $\text{a\ }$angiver desuden også,
hvor meget afstand der er mellem parablen sider. Jo længere $a$ er fra
$0$, jo stejlere bliver grafen.

$b$ angiver hældningen af parablen i skæringspunktet på y-aksen, men
også stedet hvor toppunktet er. Jo mere positiv, jo mere til venstre og
omvendt. Hvis $b = 0$, er ligger toppunktet på y-aksen, altså hældningen
på y-aksen er lig 0.

$c$ angiver skæringen på y-aksen. Hvis $c$ skærer y-aksen under 0 er $c$
neagtiv og omvendt.

"Argument for $c$: Når $x = 0$, er $y = c$, så $(0,c)$.

$$f(0) = a \cdot 0^{2} + b \cdot 0 + c = c$$

$$(0,c)$$

"Argument" for $b$.

$a$ differentieres ikke med, da det er en konstant for sig selv.

$$f^{'}(x) = a \cdot 2x + b + 0 = 2ax + b$$

$$f^{'}(0) = 2 \cdot a \cdot 0 + b = b$$

Rødder findes ved: $ax^{2} + bx + c$

Løsning til andengradsligning: $x = \frac{- b \pm \sqrt{d}}{2a}\ $, hvor
$d = b^{2} - 4ac$

Bevis for: $f(x) = ax^{2} + bx + c$

$$4aax^{2} + 4a \cdot bx + 4a \cdot c = 0$$

$$= 4a^{2}x^{2} + 4abx + 4a \cdot c = 0$$

God idé: Læg $(b^{2} - 4ac)\ $til på begge sider

$$4a^{2}x^{2} + 4abx + 4ac + b^{2} - 4ac = b^{2} - 4ac$$

$4a^{2}x^{2} + 4abx + b^{2} = b^{2} - 4ac,\ $det er jo det samme som
diskriminaten

$$= 4a^{2}x^{2} + 4abx + b^{2} = d$$

*Bruger kvadratsætning:*
Kvadratkomplettering:$(a + b)^{2} = a^{2} + b^{2} + 2ab$
$b^{2} - 4\text{ac} = d$

$(2ax + b)^{2} = b^{2} - 4\text{ac}$ ($x$ isoleres)

ó

$$2ax + b = \pm \sqrt{b^{2} - 4ac} - b$$

ó

$$2ax = - b \pm \sqrt{d}$$

ó

$$x = \frac{- b \pm \sqrt{d}}{2a}\ \blacksquare\ Q.E.D.$$

$$d = b^{2} - 4 \cdot a \cdot c$$

$d\  < \ 0$ (Hvis *d* er mindre end 0, er der ingen muligheder for $x$)

$d\  = \ 0$ (Hvis *d* (diskriminanten) er lig med 0, er der kun én
mulighed for *x*)

$d\  > \ 0$ (Hvis *d* er større end 0 er der 2 muligheder for *x*)

# Vektorer

Gør rede for vektorbegrebet, og udled formlen for projektion af vektor
på vektor.

En vektor har to egenskaber: En længde og en retning.

Placeringen af vektoren er ligegyldig, bare man ikke begynder at ændre
på længden og retningen, men kun ændrer dens placering.

Pilen i en bestemt længde og retning er repræsentant for en vektor:
$\begin{pmatrix}
a \\
b \\
\end{pmatrix}$

*der var et billede her engang*
height="2.0555555555555554in"}

Projektion af vektor på vektor:

$${\overrightarrow{a}}_{\overrightarrow{b}} = \frac{\left( \overrightarrow{a} \cdot \overrightarrow{b} \right)}{\left| \overrightarrow{b} \right|^{2}} \cdot \overrightarrow{b} = \frac{\left( \overrightarrow{a} \cdot \overrightarrow{b} \right)}{\left( \sqrt{\left( b_{1} \right)^{2} + \left( b_{2} \right)^{2}} \right)^{2}} \cdot \overrightarrow{b}$$

${\overrightarrow{a}}_{\overrightarrow{b}}$ er parallelle med
$\overrightarrow{b}$.

Når dette er tilfældet, ved jeg:
${\overrightarrow{a}}_{\overrightarrow{b}} = K \cdot \overrightarrow{b}$

Jeg skal altså finde et udtryk for $K$. Jeg indfører hjælpevektoren
$\overrightarrow{c}$.

Jeg observerer, at
${\overrightarrow{a}}_{\overrightarrow{b}} + \overrightarrow{c} = \overrightarrow{a} \Leftrightarrow \overrightarrow{c} = \overrightarrow{a} - {\overrightarrow{a}}_{\overrightarrow{b}}$

Jeg observerer også, at $\overrightarrow{c}\bot\overrightarrow{b}$, dvs.
$\overrightarrow{c} \cdot \overrightarrow{b} = 0$

$$\overrightarrow{c} \cdot \overrightarrow{b} = 0$$

$$= \left( \overrightarrow{a} - {\overrightarrow{a}}_{\overrightarrow{b}} \right) \cdot \overrightarrow{b} = 0$$

$$= \left( \overrightarrow{a} - K \cdot \overrightarrow{b} \right) \cdot \overrightarrow{b} = 0$$

$$= \overrightarrow{a} \cdot \overrightarrow{b} - K \cdot \overrightarrow{b} \cdot \overrightarrow{b} = 0$$

$\Leftrightarrow$
$\overrightarrow{a} \cdot \overrightarrow{b} - K \cdot \left| \overrightarrow{b} \right|^{2} = 0$

$\Leftrightarrow$
$\frac{\overrightarrow{a} \cdot \overrightarrow{b}}{\left| \overrightarrow{b} \right|^{2}} = K$

Hvis vi indsætter i
${\overrightarrow{a}}_{\overrightarrow{b}} = K \cdot \overrightarrow{b}$
får vi formlen, vi ville bevise. $\blacksquare\ Q.E.D.$

Dette bevis gælder dog ikke, hvis
$\overrightarrow{a} \parallel \overrightarrow{b}$, da det bare bliver
til ét punkt.

# Vektorer

> Udled parameterfremstillingen for en ret linje, og gør rede for
> skæringen mellem linjer.\
> Bestem skæringen mellem en linje givet ved en parameterfremstilling og
> en linje givet ved en ligning.

*der var et billede her engang*
height="3.0083333333333333in"}Parameterfremstilling for en linje.
$\begin{pmatrix}
x \\
y \\
\end{pmatrix} = \begin{pmatrix}
x_{0} \\
y_{0} \\
\end{pmatrix} + t \cdot \begin{pmatrix}
r_{1} \\
r_{2} \\
\end{pmatrix}$

$(x_{0},y_{0})$ er et punkt på linjen.

$\begin{pmatrix}
r_{1} \\
r_{2} \\
\end{pmatrix}$ er en retningsvektor for linjen.

# *Bevis for* $\begin{pmatrix}
\mathbf{x} \\
\mathbf{y} \\
\end{pmatrix}\mathbf{=}\begin{pmatrix}
\mathbf{x}_{\mathbf{0}} \\
\mathbf{y}_{\mathbf{0}} \\
\end{pmatrix}\mathbf{+ t \cdot}\begin{pmatrix}
\mathbf{r}_{\mathbf{1}} \\
\mathbf{r}_{\mathbf{2}} \\
\end{pmatrix}$

$P$ ligger på linjen

$$\Leftrightarrow$$

$$\overrightarrow{P_{0}P}\  \parallel \overrightarrow{r}$$

$$\Leftrightarrow$$

$$\overrightarrow{P_{0}P} = t \cdot \overrightarrow{r}$$

$$\Leftrightarrow$$

$$\overrightarrow{OP_{0}} + \overrightarrow{P_{0}P} = \overrightarrow{OP_{0}} + t \cdot \overrightarrow{r}$$

$$\Leftrightarrow$$

$$\overrightarrow{\text{OP}} = \overrightarrow{\text{OP}_{0}} + t \cdot \overrightarrow{r}$$

$$\Leftrightarrow$$

$$\begin{pmatrix}
x \\
y \\
\end{pmatrix} = \begin{pmatrix}
x_{0} \\
y_{0} \\
\end{pmatrix} + t \cdot \begin{pmatrix}
r_{1} \\
r_{2} \\
\end{pmatrix}\blacksquare$$

***At finde skæringspunktet mellem to linjer:*** Med forskellige
ligninger

$y = ax + b$ og $y = ax + B$

$$\Updownarrow$$

$$ax + b = \alpha x + Β$$

$$a\left( x - x_{0} \right) + b\left( y - y_{0} \right) = 0$$

$$\begin{pmatrix}
x \\
y \\
\end{pmatrix} = \begin{pmatrix}
x_{0} \\
y_{0} \\
\end{pmatrix} + t \cdot \begin{pmatrix}
r_{1} \\
r_{2} \\
\end{pmatrix}$$

Løs tre ligninger med tre ubekendte: Bedst at bruge eksempler. Hvis bare
dette ene eksempel

$$a\left( x - x_{0} \right) + b\left( y - y_{0} \right) = 0$$

$$x = x_{1} + t \cdot r_{1}$$

$$y = y_{1} + t \cdot r_{2}$$

Vi kan finde $x$ og $y$, så vi kun har den ene ubekendte $t$. Så er det
lige pludselig ikke så svært.

# Differentialregning

*der var et billede her engang*
> height="2.2895833333333333in"}Gør rede for begrebet
> differentialkvotient. Udled differentialkvotienten for mindst én
> simpel funktion ved brug af tretrinsreglen.

Det handler om, hvordan man kan finde hældningen i et bestemt punkt.

Dette kan gøres ved at sætte sekantens punkt, så tæt som muligt på dét
punkt, hvor jeg skal finde hældningen/tangenten til dét punkt.

Vi vil gerne finde tangentens hældning.

Først finder vi en sekant, og gør derefter afstanden $h$ så lille som
mulig. $h$ kan dog ikke være 0, så der vil altid være en lille
usikkerhed, i forhold til at sekanten ikke præcis vil ligge, hvor vores
punkt er.

***Nu til metoden: [Tretrinsreglen]{.ul}***

**Trin 1:** Find funktionstilvæksten/forskellen,
$f\left( x_{0} + h \right) - f(x_{0})$

**Trin 2:** Find differenskvotienten/sekantens hældning,
$a = \frac{y_{2} - y_{1}}{x_{2} - x_{1}} =$

$$\frac{f\left( x_{0} + h \right) - f\left( x_{0} \right)}{\left( x_{0} + h \right) - x_{0}}$$

$$=$$

$$\frac{f\left( x_{0} + h \right) - f\left( x_{0} \right)}{h}\ $$

**Trin 3:** Find grænseværdien. Jo mindre *h* bliver, jo tættere kommer
vi på tangenten, altså punktets hældning.
$\lim_{h \rightarrow 0}\left( \frac{f\left( x_{0} + h \right) - f\left( x_{0} \right)}{h} \right) = f'(x_{0})$.
lim (limited) står får grænse.

(Det vil sige "Grænseværdien for sekanten hældning, når $h$ går mod 0,
er tangentens hældning")

Sekantens hældning (differenskvotienten: står for forskel) går mod
tangentens hældning ($f'(x)$/differentialkvotienten: står for brøk) for
$h \rightarrow 0$.

*Eksempel på tretrinsreglen:*

*Find* $f'(x)$*, når* $f(x) = x^{2}$*.*

***Trin 1:***
$f\left( x_{0} + h \right) - f\left( x_{0} \right) = \left( x_{0} + h \right)^{2} - \left( x_{0} \right)^{2}$

*I dette næste trin, gøres der brug af kvadratsætningen.*

$$= \left( x_{0} \right)^{2} + h^{2} + 2 \cdot x_{0} \cdot h - \left( x_{0} \right)^{2}$$

$$= h^{2} + 2x_{0}h$$

***Trin 2:** Find differenskvotienten:*
$\frac{f\left( x_{0} + h \right) - f\left( x_{0} \right)}{\left( x_{0} + h \right) - x_{0}} = \frac{h^{2} + 2x_{0}h}{h} = h + 2x_{0}$

***Trin 3:** Find grænseværdien:*
$\lim_{h \rightarrow 0}\left( h + 2x_{0} \right) = 2x_{0} = f'(x_{0})$

*Når man differentierer* $x^{2}$*, får man* $2x_{0} = f'(x_{0})$

# Differentialregning

*der var et billede her engang*
> height="2.0194444444444444in"}Gør rede for regneregler ved
> differentiation af sum og differens. Forklar sammenhængen mellem
> monotoniforholdene for en funktion og fortegnet for den afledte
> funktion.

Differentiation af sum og differens:

$$\left( f(x) \pm g(x) \right)^{'} = \left( f(x) \right)^{'} \pm \left( g(x) \right)^{'}$$

Bevis: Vi skal bevise at de to er ens.

*Venstresiden:*

$$\left( f(x) \pm g(x) \right)^{'} = \lim_{h \rightarrow 0}\left( \frac{\left( f\left( x_{0} + h \right) \pm g\left( x_{0} + h \right) \right) \pm \left( f\left( x_{0} \right) \pm g\left( x_{0} \right) \right)}{h} \right)$$

*Højresiden:*

$$\left( f(x) \right)^{'} \pm \left( g(x) \right)^{'} = \lim_{h \rightarrow 0}\left( \frac{f\left( x_{0} + h \right) - f\left( x_{0} \right)}{h} \pm \frac{g\left( x_{0} + h \right) - g\left( x_{0} \right)}{h} \right)$$

$$= \lim_{h \rightarrow 0}\left( \frac{f\left( x_{0} + h \right) - f\left( x_{0} \right) \pm g\left( x_{0} + h \right) - g\left( x_{0} \right)}{h} \right) = \lim_{h \rightarrow 0}\left( \frac{\left( f\left( x_{0} + h \right) \pm g\left( x_{0} + h \right) \right) - \left( f\left( x_{0} \right) \pm g\left( x_{0} \right) \right)}{h} \right)$$

De giver altså det samme. Der er nu bevist at man kan tage det led for
led.

*der var et billede her engang*
height="1.9198403324584428in"}

$$\lim_{h \rightarrow 0}\left( \frac{\left( f\left( x_{0} + h \right) - f(x_{0}) \right)}{h} \right)$$

$f(x) \pm g(x) = i(x)$ $\Leftrightarrow$
$\frac{i\left( x_{0} + h \right) - i\left( x_{0} \right)}{h}$

Når vi har $f(x)$ skal vi aflede til $f^{'}(x) = 0$.

Da der står forklar, kan man bruge et eksempel med tal.

  ---------------------------------------------------------------------------------------------
  $$x$$       $$x < 3$$      $$3$$             $$3 < x < 8$$   $$8$$             $$x > 8$$
  ----------- -------------- ----------------- --------------- ----------------- --------------
  $$f'(x)$$   $$+$$          $$0$$             $$-$$           $$0$$             $$+$$

  $$f(x)$$    $$\nearrow$$   $$\rightarrow$$   $$\searrow$$    $$\rightarrow$$   $$\nearrow$$
  ---------------------------------------------------------------------------------------------

Fortegnet for den afledte funktion, handler om monotonitabellen, om den
er stigende eller faldende.

# Sandsynlighedsregning og statistik

> Gør rede for begreberne sandsynlighed og stokastisk variabel. Forklar
> binomialfordelingen og hvordan denne anvendes.

$P(X = 4)$. (Hvad er sandsynligheden for at $X = 4$.)

Stokastisk variabel $X$; Variabel med tilfældig værdi.

$X\sim b(n,p)$ (Betyder at $X$ er binomialfordelt)

$X\sim N(\mu,\sigma)$ (Betyder at $X$ er normalfordelt)

$\mu$ er middelværdi $\sigma$ er spredning

Binomialfordelingen:

Antalsparameter ($n$)

Sandsynlighedsparameter ($P$)

Basiseksperiment; det "eksperiment" vi udfører $n$ gange

Der må kun være to muligheder; Succes og ikke succes.

$K(n,r)$ (At udvælge $r$ mellem $n$ elementer)

$P(X = r) = K(n,r) \cdot p^{r} \cdot (1 - P)^{n - r}$ (Formel for
binomialfordelingen)

Vi skal bare forklare hvordan man bruger den og hvordan den ser ud og
hvad de forskellige faktorer gør. Snakke om hvad $K$ gør

# Trigonometriske funktioner

*der var et billede her engang*
height="2.5833333333333335in"}Gør rede for de trigonometriske
funktioner. Forklar harmoniske svingninger.

Omkreds af en cirkel:
$2 \cdot \pi \cdot r = 2 \cdot \pi \cdot 1 = 2 \cdot \pi$

I en cosinus funktion, er bølgetop til bølgetop, én cirkel.

En halv omgang i enhedscirklen er lig én $\pi$.

Grader: Måler størrelsen på en vinkel.

Radianer: Angiver længden af cirkelbuen.

Omregning af radianer ($k$) og grader ($v)$:
$k = v \cdot \frac{\pi}{180} \Leftrightarrow v = k \cdot \frac{180}{\pi}$

Så $90{^\circ}$ svarer til $0,5\pi$ radianer, da omkredsen cirklen er
$2 \cdot \pi$.

$$P\left( \cos(v),\sin(v) \right)$$

De kan maksimalt gå fra $- 1$ til $1$.

Vi ser på en harmonisk svingning:
$f(x) = A \cdot \sin(\omega \cdot x + \phi) + d$

$A$ er amplituden og angiver højden på bølgen fra $x$-aksen og op/ned
til bølgetoppen eller -dalen.

$\omega$ er omega og angiver længden på bølgen,
svingningstiden/perioden. $T = \frac{2\pi}{\omega}$. Des større omega
bliver, des kortere vil bølgen være og des hurtigere vil bølgen foregå.

$x$ er radianer, og angiver hvor langt om cirklen der bevæges.

$\phi$ angiver for sinus den vandrette linje, faseforskydningen, altså
hvor langt bølgen forskydes vandret.

$d$ angiver for sinusfunktioner, den vandrette linje, som bølgen svinger
om, midterlinjen for bølgen.

Faseforskydningen udregnes som: $- \frac{\phi}{\omega}$

Evt. tale om tangens i forhold til det.
