# Algoritmer og datastrukturer
- [Github link](https://github.com/thorehusfeldt/algoritmer-og-datastrukturer/blob/master/ad-book.pdf)
- [[Algoritmer og datastrukturer.pdf|PDF link]]

## Algoritme analyse
[[Algoritmer og datastrukturer#page=24]]

>"vi interessere os for maksimale, minimale og gennemsnitlige kørselstider"

Når vi analyserer algoritmer interesserer vi os for både den minimale, maksimale 
 og gennemsnitlige køretid (se formel (s. 25)). 

 ##### Hvornår bruger vi de forskellige køretider?
 1. **Maksimal**: Bruges oftest, da den viser os in sikker værdi for algoritmens køretid
 2. **Minimum**: Holdes op mod den maksimale for at vise *variansen* i køretiden
 3. **Gennemsnitlige**: Hvis denne varians er meget stor, kan den gennemsnitlige værdi fortælle os hvor hurtigt vi kan forvente at algoritmen kører.

### Asymptotisk analyse
Lader os bestemme en algoritmes køretid der afhænder at en maskinafhænig konstant. ([[Algoritmer og datastrukturer.pdf#page=25]] )



Vi ser på hvad funktionerne for $T(I_n)$ gør når $n$ bliver meget stort.

Vi interesserer os her ikke for de specifikke $T(I_n)$-værdier, men for deres vækstrater, og dermed deres asymptoter. 

##### Regner for sammenligning af vækstrate for $f(x)$ og $g(x)$
$c$ og $d$ er (positive?) konstanter. #spørg

Disse udtryk **skal** være sande når $n$ bliver meget stort
- *Samme* vækstrate: $c \leq \frac{f(n)}{g(n)} \leq d$
- $f(n)$ vokser *hurtigere* end $g(n)$: $c \cdot g(n)\leq f(n)$

### Store-O-notation
Notation for [[#Asymptotisk analyse]]

definition: #spørg



### Stirlings formel
https://brilliant.org/wiki/stirlings-formula/



---
#informatik
#tekst