# [[Isaac Newton|Newtons]] Afkølingslov

$$T' = \frac{dT}{dt} = -k \cdot (T-T_{omg})$$
Som kan omskrives til:
$$T'(t) = -k \cdot (T(t)-T_{omg})$$

$T$ / $T(t)$  : Temperaturen som funktion af tid.
$T_{omg}$ : Temperaturen af omgivelserne.
$k$: [[#k -værdien|Proportionalitetskonstanten]].

---
### Afkølingsloven og differentialligninger
Denne model passer på differentialligningen $y'=b-a \cdot y$. (se [[Linære førsteordensdifferentialligninger#3 Løsningsformel Newtons Afkølingslov]])

Dette kan vi se hvis vi ganger parantesen ud

$$T' = -k \cdot (T-T_{omg}) \arrows T' = -k \cdot T + k \cdot T_{omg} \arrows T' = k \cdot T_{omg} -k \cdot T$$
$T$  : Temperaturen som funktion af tid.
$T_{omg}$ : Temperaturen af omgivelserne.
$k$: [[#k -værdien|Proportionalitetskonstanten]].

Da løsningen til den gennerelle differentialligning er $f(x) =  \frac{b}{a} + C  \cdot e^{-ax}$, ved vi at $T$ kan regnes således:

$$T = T_{omg}+C \cdot e^{-kt} \arrows T = \frac{b}{a}+C \cdot e^{-at}, \s \text{hvor } a=k \text{ og } b=k \cdot T_{omg}$$
$a$ : en konstant, der er lig $k$.
$b$ : en anden konstant der er lig $k \cdot T_{omg}$-


>[!Note]- Udledning af løsning med a og b
>
>$$a = k, \s\s b = k \cdot T_{omg}$$
>$$T = \frac{b}{a} + C  \cdot e^{-at} = \frac{\cancel{k} \cdot T_{omg}}{\cancel{k}}+C \cdot e^{-kt} = T_{omg} + C \cdot e^{-kt}$$
>
>Vi kan altså finde $T(t)$ ved at bruge denne formel.
>

##### $k$-værdien

$k$-værdien er en proportionalskonstant, der beskriver hvor hurtigt elementet optager eller afgiver varme. Jo højere $k$, jo hurtigere ændre temperaturen sig.

### Afkøling og Hældningsfelt
Vi kan se hvordan temperaturen går mod omgivelsernes temperatur, hvis vi tegner et [[Hældningsfelt]] for differentialligningen $T' = -k \cdot (T-T_{omg})$

![[Newtons Afkølingslov Hældningsfelt.png|300]]

---
#matematik 