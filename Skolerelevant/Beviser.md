# Beviser
[[How to Bevis.pdf]]


## Konnektiver
$$p \land q, \s \text{"og/konjunktion"}$$
$$p \:\lor\: q, \s \text{"eller/disjunktion"}$$
$$p\Rightarrow q,\s \text{"medfører/implikation"}$$
$$p \arrows q, \s\text{"biimplikation"}$$
$$\lnot p, \s\text{"ikke/negation"}$$



## Udsagn
Et udsagn kan enten være sandt eller falskt.  

$$5=6$$
$$4>3$$
$$10 \cdot 4 = 20  \cdot 2 \arrows 1=1$$


## Prædikater
Et udsagn der bruger en *fri variabel*. Vi kan derfor ikke sige om prædikater er sande eller falske, da det afhænger af variablen.

$$p(x): x < 10$$

## Kvantorer

Eksistenskvantor: "Der findes": $\exists$ 
Alkvantor: "Alle": $\forall$ 

**Eksempler:**
"der findes et x der er et reelt tal, for hvilket prædikatet $p(x)$ gælder"
$$\exists x \in \R:$$


## Bevisstrategier

### Modstridsbevis
Man antager der modsatte af det man vil bevise, og viser at det vil lede til en *modstrid*.

**Eksempel:** $\sqrt{2}$ er irrational

Vi antager det modsatte:  $\sqrt{2}$ er rational

altså må man kunne sige dette
$$\sqrt{2} = \frac{m}{n} \arrows 2 = \frac{m^2}{n^2} \arrows 2n^2 = m^2$$
$\frac{m}{n}$ skal være en uforkortelig brøk.

Vi kan her se at $m$ må være lige, og kan skrives således: $m=2p$, hvor $p$ er et helt tal

Vi kan nu skrive således
$$2n^2=(2p)^2 = 4p^2$$
Vi kan nu se at $p$ også må være et lige tal.

Da både $m$ og $n$ er lige tal, kan brøken $\frac{m}{n}$ forkortes. Dette er en modstrid! $\sqrt{2}$ må derfor være irrational.

### Induktionsbevis
Handler om naturlige tal.

Induktionsstart (vis $p(1)$). Viser at prædikatet i hvert fald gælder i ét tilfælde. 

Induktionsskrittet (antager $p(m)$). Vi antager at antagelsen $p(m)$ medfører at $p(m+1)$ også er sandt. 


---
#matematik 