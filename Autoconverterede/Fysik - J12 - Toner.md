# Formål

Formålet med forsøgene er at undersøge egenskaber ved lydtoner vha.
lydsensor og LoggerPro.

# Teori

Læs s. 200-203 i Basis Fysik C eller s. 307-310 i Basis Fysik B.

Eksperimenter lidt med at sammensætte forskellige frekvenser i
simulatoren:
<https://phet.colorado.edu/sims/normal-modes/normal-modes_da.html>

-   Hvad sker der, når flere forskellige frekvenser sættes sammen?

Opstil en hypotese for, hvordan du forventer, at grafen for henholdsvis
en stemmegaffel og en sunget tone ser ud.

# Metode

## Materialer

Stemmegaffel og resonanskasse, lydsensor til LoggerPro, computer med
LoggerPro.

## Fremgangsmåde

-   Indstil *LoggerPro* til 'Timebased':

> 10000 målinger/s og en måletid på 0.5 s.

*der var et billede her engang*
height="1.5136734470691164in"}

-   Start med at måle på en stemmegaffel i en resonanskasse, f.eks.
    440Hz.

-   Når I har en ren tone, skal I bestemme perioden *T* ud fra (*Time*,
    *Pres*) -grafen. Se eksemplet til venstre

> nedenfor. Benyt dette til at bestemme frekvensen *f* vha. formlen
> $f = \frac{1}{T}$.

$$T = 0,002296$$

$$f = \frac{1}{0,002296} \approx 435,5401$$

-   Konstruér derefter en *FFT*-graf [^1]^)^: Insert \| Additional
    Graphs \| FFT Graph.

-   Tilføj "Gaussian"-regression ved at trykke på "Curve Fit" og scrolle
    ned.

*der var et billede her engang*
> angiver nu frekvensen.

$$f = 439.9$$

Eksempler på målegrafer:

  ---------------------------------------------------------------------------------------------------------
*der var et billede her engang*
  height="1.7291666666666667in"}                       height="1.7291666666666667in"}
  ---------------------------------------------------- ----------------------------------------------------
                                                       

  ---------------------------------------------------------------------------------------------------------

-   Prøv derefter at synge eller fløjte en ren tone og undersøg denne
    måling på samme måde som ovenfor.

> Syng også mindst 3 af vokalerne: A, E, I, O, U, Y, Æ, Ø, Å. Lav
> *FFT*-grafer af disse.
>
> **A-tone:**

$$T = 0.002333$$

$$f = \frac{1}{0.002333} \approx 428,6327$$

*der var et billede her engang*
> height="2.5965277777777778in"}

-   Grafen her viser den tone som passer bedst, og den viser 437,3 hz.

# Diskussion

-   Hvordan passer din hypotese om graferne med det observerede?

```{=html}
<!-- -->
```
-   *Vores hypotese var at vi ville få en frekvens på 440hz, men vi
    ramte ikke helt præcis det vi ville grundet fejlkilder såsom
    baggrundstøj og måleusikerhed.*

```{=html}
<!-- -->
```
-   Hvordan passer frekvenserne beregnet med $f = \frac{1}{T}$ og *FFT*
    med hinanden og med den trykte værdi på stemmegaflen? Beregn
    procentvis afvigelse.

```{=html}
<!-- -->
```
-   *Den afveg en smule 9,975% og da vi selv lavede en tone, afveg den
    med 7,16%*

$$\frac{400 - 439.9}{400} \cdot 100 \approx - 9,975\%$$

$$\frac{400 - 428,6327}{400} \cdot 100 = - 7,16\%$$

-   Hvorfor bliver ikke alle lydbilleder lige "pæne"? Overvej, hvad en
    ren tone egentlig er.

> *Pga. fejlkilder, og en ren tone er en tone, som hele tiden har den
> samme frekvens.*

-   Sørg for at kommentere alle grafer ud fra teorien.

-   Kommenter usikkerheder og fejlkilder.

> *Usikkerheder:*

-   Måleredskaberne

-   Målinger pr. sekund

> *Fejlkilder:*

-   Baggrundsstøj

-   Målepræcision

[^1]: ^)^ *FFT*: [F]{.ul}ast [F]{.ul}ourier [T]{.ul}ransformation.
