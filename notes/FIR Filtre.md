# FIR Filtre
See [[lektion 10 - Introduktion til FIR filtre.pdf|slides]].

Ingen tilbagekobling: Afhænder kun a det nuværende og tidligere input

$M$: Orden

![[Pasted image 20231109085155.png|300]]
## Lineær fase

#### Nulpunkter

Nulpunker skal ligge i par således
$$z_{1} = r\angle \phi, \s z_{2} = r/1\ \angle\phi$$
Dette resulterer i nulpunkter der kunne ligge således.
![[Pasted image 20231109083436.png|center|250]]

#### Symetri
Et FIR filter med lineær fase er altid spejlet over midterste sample:
![[Pasted image 20231109083656.png|center|400]]

**Koefficienterne er symmetriske.**

## Filtre med Fouré Koefficienter
See [[lektion 10 - Introduktion til FIR filtre.pdf#page=54|slide]].
$$H(z) = \sum_{i=0}^{2M} a_{i} \cdot z^{-i}$$

![[Pasted image 20231109094441.png]]
#### Slides
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=59|lavpas]]
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=66|højpas]].
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=70|båndpas]].
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=75|båndstop]].

### Using a [[Window Functions|window function]]
To get the windowed fourier koefficients we simply multiply the fourier constants with the window samples.
$$c_{m}' = c_{m}w_{n}$$
In this case we find $a_{i}$ like this
$$a_{i} = c'_{M-i}$$

## Design af FIR filter
See [[lektion 11 - Design af FIR filtre.pdf#page=37|slides]].


#### Bestem specifikation
1. Afskæringsfrekvensen $f_a$.
2. Maksimal tilladelig bredde af overgangsområde $\Delta f_{a}$.
3. Maksimal tilladelig stopbåndsforstærkning $H_{s}$.
4. Maksimal tilladelig pasbåndsripple $H_{r}$.

#### Bestem filter
Konstruktionen af et FIR-filter kan forløbe efter følgende procedure
1. Vælg vinduesfunktion. Dette valg foretagespå baggrund af specificerede stopbånds- og pasbåndsripple.
2. Bestem ordenstal. Ordenstallet $2M$ bestemmes ud fra overgangsområde $\Delta f_{a}$.
![[Pasted image 20231124105848.png]]
$$M = \frac{B_{n} \cdot f_{s}}{2 \Delta f}$$
$\Delta f$: Overgangsområde
$B_{n}$: Den normerede main lobe bredde

Begge findes i tabellen ovenfor.

3. Beregn filterkoefficienter. Filterkoefficienterne udregnes som
$$a_{i} = c_{M−i}w_{M−i}$$
4. Verifikation. Filtrets amplitudekarakteristik kontrolleres og om nødvendigt redesignes filtret ($M$-værdi korrigeres).

---
#signalprocessing
