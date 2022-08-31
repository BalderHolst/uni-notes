# Binomialfordelingen
[[Normalfordelingen]] i steps

### Formel
$$p(x=r)=K(n,r) \cdot p^r \cdot (1-p)^{n-r}$$
$p$: sandsynligheden for succes
$r$: "$x$-værdien"
$n$: antal test

##### Plot i maple
`pindediagramBIN(n, p)`

### Konfidensintervaller
ved et input i procent og n (elementer) er vi 95% sikker på at den sande sansynlighed ligger mellem de to outputs.

```ad-example # Admonition type. See below for a list of available types.
title:                  Maple
collapse:               # Create a collapsible admonition.

![[Konfidensintervaller.png]]

```

### Binomialtest
Vi tester om vi er bladt de 5% (i 5% signifikansniveau)

`binomialTest(n, p, s, tosidet)`

$n$: antal test
$p$: chancen for succes
$s$: signifikansniveau

### Binomialkoefficienten ([[kombinatorik]])
antal måder at vælge $r$ blandt n elementer

Ligegyldig rækkefølge (denne bruger vi i binomialfordelingen)
$$K(n,r)=\frac{n!}{(n-r)! \cdot r!}$$
Når rækkefølgen ikke er ligegyldig (der eksisterer både [1,2] og [2,1])
(kan ikke finde formel lige nu)

---
#dansk 