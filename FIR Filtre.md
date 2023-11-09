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

## Filtre

![[Pasted image 20231109094441.png]]
#### Slides
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=59|lavpas]]
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=66|højpas]].
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=70|båndpas]].
- [[lektion 10 - Introduktion til FIR filtre.pdf#page=75|båndstop]].

---
#signalprocessing
