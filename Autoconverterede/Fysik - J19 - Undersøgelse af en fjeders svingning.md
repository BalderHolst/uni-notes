# Formål

Dette forsøg går ud på at undersøge en såkaldt harmonisk svingning, for
at bestemme svingningens amplitude, vinkelhastighed, faseforskydning og
forskydningskonstant.

# Teori

Stedfunktionen, $x(t)$, for en harmonisk svingning kan beskrives ud fra
forskriften:

$x(t) = A \cdot \sin\sin\ (\omega \cdot t + \phi)\  + B$

Hvor *A* er amplituden, $\omega$ er vinkelfrekvensen, $\phi$ er
faseforskydningen, og *B* er forskydningskonstanten.

Vinkelfrekvensen er også givet ved:

$\omega = \frac{2\pi}{T}$

Hvor *T* er perioden.

For et lod ophængt i en fjeder, der foretager en harmonisk svingning,
gælder også:

$\omega =$

Hvor *k* er fjederkonstanten, og *m* er massen af loddet.

# Metode

## Fremgangsmåde

Fjederen med lod spændes op i et stativ som vist nedenunder. Lige under
loddet i en passende afstand placeres den elektroniske afstandsmåler,
som kobles til computeren.

LoggerPro sættes til at foretage 20 -- 25 målinger i sekundet af
afstanden fra afstandsmåleren til loddet. Sørg for at loddet ikke kommer
tættere på afstandsmåleren end 20 cm. Der måles i ca. 5 sekunder, eller
2 -- 3 perioder.

*der var et billede her engang*
height="2.914009186351706in"}

## Databehandling

I loggerPro vises en (*t,x)*-graf (altså loddets position, *x*, som
funktion af tiden, *t*).

a)  Der laves nu regression med regressionsforskriften:
    > $x(t) = A \bullet \sin\sin\ (B \bullet t + C)\  + D$.

*der var et billede her engang*
> height="3.4990944881889763in"}
>
*der var et billede her engang*
> height="3.5866699475065618in"}

b)  Parametrene A, B, C og D aflæses. Forklar hvilken fysisk betydning
    > de fire parametre har.

A er amplituden som er på 0,1823 , B er vinkelfrekvensen på 5,207, C er
faseforskydningen som er 5, 749 og D 0,6571 er forskydnings konstanten.

c)  Aflæs perioden på grafen og udregn vinkelhastigheden med følgende
    > formel:

$\omega = \frac{2\pi}{T}$

og sammenlign værdien af denne, som du har fundet i b).

T er lig 1,15 sekunder.

$\omega = \frac{2\pi}{T}$

$\omega = \frac{2\pi}{1,15} = 5,46$

d)  Beregn ved hjælp af regressionsforskriften loddets position til
    > tiden 10 s.

Vi har en funktionsforskrift som er følgende:

$x(t) = 0,1823*sin\ (5,207 \cdot t + 5,749)\  + 0,6571$

Vi sætter dermed vores t-værdi til 10 i forskriften og får dermed
positionen til 10 sekunder.

$x(10) = 0,1823*sin\ (5,207 \cdot 10 + 5,749)\  + 0,6571$

e)  I loggerPro vises hastighedsgrafen. Aflæs hastigheden i
    > yderpositionerne og i hvilepositionen.

f)  Lav sinus-regression for hastighedsgrafen og nedskriv forskriften:

> *v(t)* =

g)  Beregn loddets hastighed til tiden 10 s.

h)  Beregn fjederkonstanten, *k*, ud fra følgende formel:

$\omega =$

*der var et billede her engang*
> height="1.9305555555555556in"}
>
> Sammenlign med *k* bestemt ud fra Hookes Lov.

fjederkonstanten er 3,4N/m. udfra hookes lov.

$k = 5,4{6^{2}*0,1 = 2,99N/m}^{}$
