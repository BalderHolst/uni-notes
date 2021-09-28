
# Differentialligninger
Har altid en funktion som løsning.

En ligning der indeholder en afledt funktion

---

### Løsninger

```ad-example # Admonition type. See below for a list of available types.
title:                  Eksempel med *Fuldstændig* og *Partikulær* løsning
collapse:               # Create a collapsible admonition.

En simpel differentialligning kunne for eksempel være $y'=8$. Måden vi løser sådan en ligning, er ved at integrere på begge sider af ligningen. Hvis vi gør det, ser ligningen ud sådan
.
$$y=8x$$

Dette er dog ikke den eneste løsning, for man kan faktisk lægge en vilkårlig konstant til $y$, og differentialligningen vil stadig være sand, fordi de reelle y-værdier går tabt, når man differentiere. Den *fuldstændige* løsning kan altså skrives således.

$$y=8x+c$$

Vi kan nu vælge at definere vores $c$-værdi for at finde den *partikulære* løsning. Eksempelvis: $y=8x+10$. En grund til at definere $c$ kunne være at man på forhånd kender et punkt, som funktionen skærer, for så kan man indsætte punktet i formlen og isolere $c$. Hvis vi for eksempel ved, at $y$ skærer punktet $(-2,5)$,  kan vi skrive formlen op på denne måde.
$$5=8 \cdot (-2) + c \s 5=-16 + c \s 21=c $$
Vi har nu fundet vores $c$-værdi, og kan sætte den ind i vores funktion. Funktionen ender altså med at hedde: 
$$y=8x+21$$.

```

---

### At Gøre Prøve

At gøre prøve er en måde at teste om en bestemt funktion, er en løsning for en given differentialligning gørePrøve. Eksempelvis kunne man spørge: er $f(x) = 2e^{16x}$ en gyldig løsning på differentialligningen $y' = 16y$? Det første skridt mod at besvare spørgsmålet er at differentiere funktionen.


$$f'(x)=32e^{16x}$$

Vi kan nu sætte vores $f(x)$ og $f'(x)$ ind i differentialligningen

$$y = 16y  \s f'(x) = 16 \cdot f(x) \s 32e^{16x} = 16 \cdot 2e^{16x} \s 32e^{16x} = 32e^{16x}$$

Her kan det ses at funktionen $f(x) = 2e^{16x}$ er en løsning på differencialligningen $y'=16y$, fordi at at vi ender med et sandt udtryk. På den måde kan man afgøre om en funktion er en løsning på en given differentialligning, ved at gøre prøve.

---
#matematik 

