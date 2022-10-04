# Bevis for Løsningsformlen

Vi starter med forskriften for et [[Andengradspolynomier|andengradspolynomie]] og sætter det lig $0$ for at finde rødderne.

$$f(x) = ax^2+bx+c = 0$$

*God ide:* vi ganger med $4a$

$$4a^2x^2 + 4abx + 4ac = 0$$

*Anden god ide:* vi lægger [[Andengradspolynomier#Diskriminanten|diskriminanten]] til begge sider.

$$4a^2x^2 + 4abx + 4ac + b^2 - 4ac = b^2  - 4ac $$

Bruger [[Kvadratsætninger|kvadratsætningen]]: $(a+b)^2 = a^2 +b^2 + 2ab$

Først omskriver vi *venstre* side af udtrykket så det passer på højre side af regnereglen

$$\text{venstre:}\s 4a^2x^2 + b^2 + 4abx$$
Her er $a$ og $b$

$$a=2ax,\, b=b$$
Vi kan med regnereglen omskrive udtrukket således
$$\text{venstre: } \s (2ax+b)^2$$

Vi kan nu igen indrage den højre side af ligningen

$$(2ax+b)^2 = b^2 -4ac$$

Vi definerer vi $d$ til at være lig $b^2-4ac$

$$d = b^2-4ac$$

Nu kan vi så skrive ligningen således

$$(2ax+b)^2 = d$$

Til sidst kan vi bare isolere $x$

$$(2ax+b)^2 = d \arrows 2ax+b = \sqrt{d} \arrows 2ax = \sqrt{d} - b \arrows x = \frac{\sqrt{d} - b}{2a}$$

Når man tager kvadratroden af et tal får man for det meste faktisk *to* svar: et negativt og et positivt. Derfor kan vi sætte $\pm$ foran kvadratroden.

Derudover kan vi rykke $-b$ ud foran kvadratroden for at få udtrykket til at lige det i [[Formelsamling.pdf|formelsamlingen]].

$$x = \frac{-b \pm \sqrt{d}}{2a}$$

---
##### Tags
#matematik 
#bevis 