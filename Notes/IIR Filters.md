---
created: 2025-09-21
tags: [signalprocessing]
---
# IIR Filters
See [[lektion 8 - Introduktion til IIR filtre.pdf|slides]].

Infinite Impulse Response Filter. Infinite because the use the *previus output to calculate the next*, creating a recursive dependency on previous outputs. This is also why IIR filters **can be unstable**.

> *"Vi placerer **poler**"*
> \- Christoffer

Har *altid poler*.

### Order
How many previously estimated outputs do i need to find the current output.

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
![[IIR-Filters-Differences-in-Frequency-Response.png|center|300]]

##### Differences in Impule Response
![[IIR-Filters-Differences-in-Impule-Response.png|center|300]]