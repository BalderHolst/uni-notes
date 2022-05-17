# Lineære førsteordensdifferentialligninger
[[Differentialligninger]]

**Førsteordensdifferentialligninger** = ligninger hvor der altid kun er *et* mærke (eks $y'$ og ikke $y''$)

**Linæredifferentialligninger** = alle differentialligninger, der kan beskrives med den [[#1 Gennerel løsningsformel|generelle løsningsformel]].

---

## 1. Generel løsningsformel

$$y' + a(x)  \cdot y = b(x) \arrows y' = b(x) - a(x) \cdot y$$



**Variabler** *(disse funktioner kan godt være konstanter)*
$a(x)$: en funktion af $x$
$b(x)$: en anden funktion af $x$


#### Løsningsformel
$$f(x) = e^{-A(x)} \cdot \int e^{A(x)} \cdot b(x)dx$$

***Husk integrationskonstanten når du integrere***

**Variabler**
$A(x)$: **en** stamfunktion for $a(x)$


```ad-example # Admonition type. See below for a list of available types.
title:                  Bevis
collapse:               # Create a collapsible admonition.

![[Bevis for den Gennerelle Løsningsformel til Linære Førsteordensdifferentialligninger]]

```


```ad-example # Admonition type. See below for a list of available types.
title:                  Eksempler
collapse:               # Create a collapsible admonition.

##### Eksempel  1
$$y' = \frac{1}{x} \cdot y = 5x^3$$

*Løsning:*

$a(x) = \frac{1}{x}$
$b(x) = 5x^3$

Jeg skal finde $A(x)$, hvilket jeg gør ved at integere $a(x)$
$$A(x) = \int \frac{1}{x}dx = ln(x)$$

Sætter $A(x)$ ind
$$f(x) = e^{-ln(x)} \cdot \int e^{ln(x)} \cdot 5x^3dx$$

Simplificerer første led:
$e^{-ln(x)} = \frac{1}{e^{ln(x)}} = \frac{1}{x}$

Sætter det ind
$$f(x) = \frac{1}{x} \cdot \int e^{ln(x)} \cdot 5x^3dx$$

Reducerer andet led:
$e^{ln(x)} = x$

$$f(x) = \frac{1}{x} \cdot \int x \cdot 5x^3dx \Arrows f(x) = \frac{1}{x} \cdot \int 5x^4dx$$

Integrerer
$$\frac{1}{x}  \cdot (x^5 + k) \s = \s x^4 + \frac{k}{x}$$

Altså er løsningen
$$f(x) = x^4 + \frac{k}{x}$$

##### Eksempel 2
$$\frac{dy}{dx} - \frac{2}{x} \cdot y = e^x$$

##### Eksempel 3
$$y' = sin(x) - 5y$$


```


---
## 2. Løsningsformel

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
## 3. Løsningsformel ([[Newtons Afkølingslov]])

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

**God ide**

$$g(x) = f(x) - \frac{b}{a}, \s \text{der kan differentieres til } f'(x)$$

Vi sætter $g(x)$ ind i stedet for $f(x) - \frac{b}{a}$

$$g'(x) = -a \cdot g(x)$$

Hvis vi siger at $-a = k$, kan vi se at $g(x)$ er løsningen på differentialligningen $y'=k \cdot y$.

Den fuldstændige løsning på differentialligningen ([[#2 Løsningsformel]]) er $g(x) = C \cdot e^{-ax}$

Vi vender tilbage til den gode ide

$$g(x) = f(x) - \frac{b}{a}$$

Nu kan vi erstatte det med løsningen for $g(x)$

$$C \cdot e^{-ax} = f(x) - \frac{b}{a}$$

vi isolerer $f(x)$

$$f(x) = \frac{b}{a} + C \cdot e^{-ax}$$

```

---

### 4. løsningsformel - Separation af de variable
Man "separerer" $x$ og $y$.

Kan bruges når en differentialligning har formen $\frac{dy}{dx} = g(x) \cdot h(y)$.


```ad-example # Admonition type. See below for a list of available types.
title: 			Eksempler
collapse:               # Create a collapsible admonition.

##### Eksemper på egnede differentialligninger
$y'=3 \cdot y \cdot sin(x)$
$y'=x \cdot y-\sqrt{x} \cdot y = y  \cdot (\cdot x-\sqrt{x})$

**ikke-eksempler**
$y'=x^2-2y$
$y'=cos(x-y)$

##### Eksempelløsning
Løs differentialligningen $y'=e^{-y} \cdot 2x$ (da der ikke er noget punkt eller lignende, finder jeg den fuldstændige løsning).

Vi sætter *alt* med $y$ over på ventre, og *alt* med $x$ til højre.

$$y'=e^{-y} \cdot 2x \arrows dy = \frac{1}{e^y} \cdot 2x \cdot dx \arrows e^y \cdot dy = 2x \cdot dx$$

Vi kan nu integrere på begge sider 

$$\int e^y \cdot dy = \int 2x \cdot dx \arrows e^y + k_1 = x^2 + k_2 \arrows e^y = x^2+k_1-k_2$$

Laver en ny konstant $c$ der summen af de andre konstanter

$$c=k_1-k_2$$

Sætter $c$ ind og reducerer videre

$$e^y = x^2+c = ln(e^y) = ln(x^2+c) \arrows y = ln(x^2+c)$$

```

---

#matematik 