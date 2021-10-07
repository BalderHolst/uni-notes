
# Differentialligninger
Har altid en funktion som løsning.

En ligning der indeholder en [[Differentialregning|afledt funktion]]

---
## Løsningsformel 1

$$y' = k \cdot y \arrows f(x)=C \cdot e^{k \cdot x}$$

Løsningerne til differentialligningen vil altid være [[Eksponentielle Funktioner]].

$y'$ er ligefrem proportional med $y$. 

##### $k$-værdien

$k$ er en konstant, og kan derfor ikke indeholde $x$. Den har altid enheden $\frac{1}{[\text{tidsenhed}]}$.

$$\frac{y'}{y} = k$$

Dette er den relative væksthastighed. Viser hvor stor væksthastigheden er i forhold til 

**Eks.**
Smittemodel : $s(t)$

$$\frac{s'(3)}{s(3)} = 0.25 \arrows \frac{s'(t)}{s(t)} = 0.25$$

hver person smitter $0.25$ personer.

---

### Løsninger

```ad-example # Admonition type. See below for a list of available types.
title:                  Eksempel 1
collapse:               # Create a collapsible admonition.

En simpel differentialligning kunne for eksempel være $y'=8$. Måden vi løser sådan en ligning, er ved at [[Integralregning|integrere]] på begge sider af ligningen. Hvis vi gør det, ser ligningen ud sådan
.
$$y=8x$$

Dette er dog ikke den eneste løsning, for man kan faktisk lægge en vilkårlig konstant til $y$, og differentialligningen vil stadig være sand, fordi de reelle y-værdier går tabt, når man differentiere. Den *fuldstændige* løsning kan altså skrives således.

$$y=8x+c$$

Vi kan nu vælge at definere vores $c$-værdi for at finde den *partikulære* løsning. Eksempelvis: $y=8x+10$. En grund til at definere $c$ kunne være at man på forhånd kender et punkt, som funktionen skærer, for så kan man indsætte punktet i formlen og isolere $c$. Hvis vi for eksempel ved, at $y$ skærer punktet $(-2,5)$,  kan vi skrive formlen op på denne måde.
$$5=8 \cdot (-2) + c \s 5=-16 + c \s 21=c $$
Vi har nu fundet vores $c$-værdi, og kan sætte den ind i vores funktion. Funktionen ender altså med at hedde: 
$$y=8x+21$$.

```


```ad-example # Admonition type. See below for a list of available types.
title:                  Eksempel 2
collapse:               # Create a collapsible admonition.

**Find den _fuldstændige_ _løsning_ til $f'(x) = 3,5 \cdot f(x)$**

Vi bruger [[#Løsningsformlen|løsningsformlen]] til at finde $k$ of opstille en forskrift for $f(x)$ 

$$k = 3,5$$

Med denne $k$-værdi kan vi opskrive $f(x)$

$$f(x) = C \cdot e^{3,5x}$$

Dette er den *fuldstændige løsning*

---

**Find den _partikulære løsning_ til $f'(t) = -0.12 \cdot f(t), \text{idet} f(0) = 20$ Tegn løsningskurven.**

Igen bruger vi [[#Løsningsformlen|løsningsformlen]] til af finde $f(x)$

$$f(x) = C \cdot e^{-0.12x}$$

For at finde den fuldstændige løsning sætter vi punktet $(0,20)$ ind i formlen

$$20 = C \cdot e^{-0.12 (0)} = C \cdot e^0 = C \s \Leftrightarrow \s C = 20$$

Ved at sætte $C$ ind i formlen for $f(x)$ får vi den *patikulære løsning*

$$f(x) = 20 \cdot e^{-0.12x}$$

```

---

### At Gøre Prøve

At gøre prøve er en måde at teste om en bestemt funktion, er en løsning for en given differentialligning. Eksempelvis kunne man spørge: er $f(x) = 2e^{16x}$ en gyldig løsning på differentialligningen $y' = 16y$? Det første skridt mod at besvare spørgsmålet er at [[Differentialregning|differentiere]] funktionen.


$$f'(x)=32e^{16x}$$

Vi kan nu sætte vores $f(x)$ og $f'(x)$ ind i differentialligningen

$$y = 16y  \s f'(x) = 16 \cdot f(x) \s 32e^{16x} = 16 \cdot 2e^{16x} \s 32e^{16x} = 32e^{16x}$$

Her kan det ses at funktionen $f(x) = 2e^{16x}$ er en løsning på differencialligningen $y'=16y$, fordi at at vi ender med et sandt udtryk. På den måde kan man afgøre om en funktion er en løsning på en given differentialligning, ved at gøre prøve.


```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

![[Bevis for differentialligninger]]

```

           
---
## Løsningsformel 2

$$y'=b-a \cdot y \Arrows f(x) =  \frac{b}{a} + C  \cdot e^{-ax}, \s a \neq0$$

$f(x)$ vil altid gå mod $y$-værdien $\frac{b}{a}$, retningen er forekellig alt efter forteget på $a$.

$$\lim\limits_{x \to \infty}(f(x)) =  \frac{b}{a}, \s 0<a$$

$$\lim\limits_{x \to -\infty}(f(x)) =  \frac{b}{a}, \s a<0$$


```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

#### Bevis
**Fuldstændig løsning:** $f(x)=\frac{b}{a} + C \cdot e^{-ax}$

$a$, $b$ og $c$ er konstanter og $a \neq 0$



Hvis $f(x)$ er løsning til differentialligningen $y'=b-a \cdot y$, så må dette være sandt

$$f'(x) = b-a \cdot f(x)$$

vi sætter $a$ uden for parantesen

$$f'(x) = -a \left(f(x)-\frac{b}{a} \right)$$

God ide

$$g(x) = f(x) - \frac{b}{a}, \s \text{der kan differentieres til } f'(x)$$

Vi sætter $g(x)$ ind i stedet for $f(x) - \frac{b}{a}$

$$g'(x) = -a \cdot g(x)$$

Hvis vi siger at $-a = k$, kan vi se at $g(x)$ er løsningen på differentialligningen $y'=k \cdot y$.

Den fuldstændige løsning på differentialligningen ([[#Løsningsformel 1]]) er $g(x) = C \cdot e^{-ax}$

Vi vender tilbage til den gode ide

$$g(x) = f(x) - \frac{b}{a}$$

Nu kan vi erstatte det med løsningen for $g(x)$

$$C \cdot e^{-ax} = f(x) - \frac{b}{a}$$

vi isolerer $f(x)$

$$f(x) = \frac{b}{a} + C \cdot e^{-ax}$$

```

---

#matematik 

