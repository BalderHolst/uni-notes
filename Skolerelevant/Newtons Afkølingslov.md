# [[Isaac Newton|Newtons]] Afkølingslov

$$T' = \frac{dT}{dt} = -k \cdot (T-T_{omg})$$

$$\Updownarrow$$

$$T'(t) = -k \cdot (T(t)-T_{omg})$$

$T$ ($T(t)$) er temperaturen
$T_{omg}$ er temperaturen af omgivelserne
$k$ er en konstant

---
### Afkølingsloven og differentialligninger
Denne model passer på [[Differentialligninger#Løsningsformel 2|differentialligningen]] $y'=b-a \cdot y$.

Dette kan vi se hvis vi ganger parantesen ud

$$T' = -k \cdot (T-T_{omg}) \arrows T' = -k \cdot T + k \cdot T_{omg}$$

Da løsningen til den gennerelle differentialligning er $f(x) =  \frac{b}{a} + C  \cdot e^{-ax}$, kan ved vi at $T$ kan regnes således:

$$a = k, \s\s b = k \cdot T_{omg}$$

$$T = \frac{b}{a} + C  \cdot e^{-at} = \frac{\cancel{k} \cdot T_{omg}}{\cancel{k}}+C \cdot e^{-kt} = T_{omg} + C \cdot e^{-kt}$$

Vi kan altså finde $T(x)$ ved at bruge denne formel.

##### $k$-værdien

$k$-værdien er en proportionalskonstant, der beskriver hvor hurtigt elementet optager eller afgiver varme. Jo højere $k$, jo hurtigere ændre temperaturen sig.

### Afkøling og Hældningsfelt
Vi kan se hvordan temperaturen går mod omgivelsernes temperatur, hvis vi tegner et [[Hældningsfelt]] for differentialligningen $T' = -k \cdot (T-T_{omg})$

![[Newtons Afkølingslov Hældningsfelt.png]]

```ad-example # Admonition type. See below for a list of available types.
title:                  Maple udregninger
collapse:

![[Newtons Afkølingslov Hældningsfelt Udregning.png]]

```

---
#matematik 