# Jævn Cirkelbevægelse

---

## Kurvekørsel og Loop

### Vejsving uden hældning
![[Pasted image 20211007102139.png]]

Bilen accelereres mod midten af cirkelbuen. Derfor må den resulterende kraft peje ind mod midten.

$$F_\mu = F_{res}$$

For at blive i en vis kurve skal bilen kunne generere en [[Gnidning|gnidnningskraft]] ($F_{\mu}$), der mindst er lig [[Centripetalkraft|centripetalkraften]] ($F_c$) i kurven.

$$F_{\mu} \le F_c \arrows m \cdot  \frac{v^2}{r} \le \mu_s \cdot m \cdot g \arrows v^2 \le \mu_s \cdot r \cdot g$$

Hvis dette udtryk ikke er opfyldt skrider køretøjet ud.

Derfor må $v_{maks}$ kunne findes således:

$$v_{maks} = \sqrt{\mu_s \cdot r \cdot g}$$

---
### Bejsving med hældning
![[Pasted image 20211007104426.png]]

Vi begynder med at opdele alle [[Vektorer|vektore]] i deres vandrette og lodrette komposanter.

$$F_{N_x} = F_N \cdot sin(\alpha) \s \text{og} \s F_{N_y} = F_N \cdot cos(\alpha)$$

$$F_{\mu_x} = \mu \cdot F_N \cdot cos(\alpha) \s \text{og} \s F_{\mu_y} = \mu \cdot F_N \cdot sin(\alpha)$$

Da den resulterende kraft skal pege mod midten af svinget, må krafterne i $y$-retningen gå ud med hinanden.

$$F_g + F_{\mu_y} - F_{N_y} = 0$$

Vi sætter variabler ind. ([[Tyngdekraften]],[[Gnidning]])
$$m \cdot g + \mu \cdot F_N \cdot sin(\alpha) - F_N \cdot cos(\alpha)$$

Normalkraften kan altså beskrives således 

$$F_N =  \frac{m \cdot g}{cos(\alpha) - \mu \cdot sin(\alpha)} $$

Og den resulterende kraft, må være resultanten af krafterne i $x$-retningen.

$$F_{N_x} + F_{\mu_x} = F_{res}$$

variabler sættes ind: 

$$F_N \cdot sin(\alpha) + \mu \cdot F_N \cdot cos(\alpha) = F_{res}$$

Vi kan nu sætte $F_N$ ind i formlen for $F_{res}$

$$F_N \cdot sin(\alpha) + \mu \cdot F_N \cdot cos(\alpha) = F_{res}$$