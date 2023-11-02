# IIR Filters
Infinite Impulse Response Filter. See [[lektion 8 - Introduktion til IIR filtre.pdf|slides]].

> *"Vi placerer **poler**"*
> \- Christoffer

Har *altid poler*.

### Procedure
1. Filtrets specifikationer opstilles
2. Filtrets z-domæne overføringsfunktion opstilles
3. Der vælges optimal realisationsstruktur
4. Der fremstilles program til signalprocessor eller tegnes diagram for hardwareløsning

## Types of z-transformation
To create an IIR filter, the transfer function must be mapped into the z-domain. There are multiple ways of doing this.

Use *capital letters for coefficients in $s$-domain*.
#### Matched z-transformation
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=11|slides]].

Poler og nulpunkter overføres direkte til z-domænet med formlen:
$$z = e^{sT}$$

---
#signalprocessing