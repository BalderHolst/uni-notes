# IIR Filters
Infinite Impulse Response Filter. See [[lektion 8 - Introduktion til IIR filtre.pdf|slides]].

> *"Vi placerer **poler**"*
> \- Christoffer

Har *altid poler*.

### Procedure
1. Filtrets specifikationer opstilles (see [[Filters]])
2. Filtrets z-domæne overføringsfunktion opstilles med en z-transformation
- [[Notes/Matched z-transformation|Matched z-transformation]]
- [[Impule Inveriant z-transformation]]
- [[Notes/Bilineær z-transformation|Bilineær z-transformation]]
3. Der vælges optimal realisationsstruktur
4. Der fremstilles program til signalprocessor eller tegnes diagram for hardwareløsning

## Types of z-transformation
To create an IIR filter, the transfer function must be mapped into the z-domain. There are multiple ways of doing this.

Use *capital letters for coefficients in $s$-domain*.

- [[Matched z-transformation]]
- [[Impule Inveriant z-transformation]]
- [[Bilineær z-transformation]]

##### Differences in Frequency Response
![[Pasted image 20231107093021.png|center|300]]

##### Differences in Impule Response
![[Pasted image 20231107093152.png|center|300]]

---
#signalprocessing
