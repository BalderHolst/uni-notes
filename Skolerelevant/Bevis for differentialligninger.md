
# Bevis
Dette bevis er baseret på videoen "MatA - Differential-ligninger"

Vi skal bevise at følgende er sandt:

   $$f'(x) = y' = k \cdot y \s f(x) = y = C \cdot e^{kx} $$

Vi kan starte med at se på den første af de to ligninger.

$$f'(x) = k \cdot y$$

Vi sætter $y$ over på den anden side, ved at dividere med $y$ på begge sider, men fordi $y$ er en variabel, så kan den jo være 0. Og hvis $y$ er 0, så må vi ikke dividere med den. Det leder jo til spørgsmålet: hvad så hvis $y$ er 0? Jo, hvis $y$ er 0, ser ligningen sådan ud.

$$\begin{align*}
f'(x) = k \cdot0 \s f'(x) = 0 \s f(x) = y = 0
\end{align*}$$

Her ser vi at $y = 0$ er en løsning. Dette kalder vi den trivielle nulløsning. \\ \\
Nu ved vi så hvad der sker hvis $y = 0$, derfor kan vi fra nu af finde ud af hvad der sker hvis $y \ne 0$. Fordi $y$ ikke længere kan være 0, kan vi nu dividere med $y$ på begge sider således.

$$\begin{align*}
f'(x) = k \cdot y ,\s y \ne 0 \\
\frac{1}{y} \cdot f'(x) = k ,\s y \ne 0
\end{align*}$$

Det næste vi skal, er at bemærke et eksempel på en anden [[Differntialregning|differentieret]] ligning. Nemlig ligningen $f(x) = ln(g(x))$. Det gør vi med regnereglen for differentiering af sammensatte funktioner.

$$f(g(x))' = f'(g(x)) \cdot g'(x) ,\s y \ne 0$$

Med den regneregel [[Differntialregning|differentierer]] vi vores funktion.

$$ln(g(x))' = \frac{1}{g(x)} \cdot g'(x) ,\s y \ne 0$$

Det interessante ved den højre side af formelen er at den har samme form som den venstre side af vores tidligere ligning. Derfor kan vi omskrive ligningen sådan.

$$\frac{1}{y} \cdot f'(x) = k \s ln|y|' = k ,\s y \ne 0 $$
 
Læg mærke til at vi ikke kan tage $ln$ til noget der er negativt, så derfor tager vi den absolutte værdi af $y$ først. Efter denne omskrivning kan vi [[Integralregning|integrere]] på begge sider for at ophæve mærket.

$$\int ln|y|' = \int k \s ln|y| = kx + c ,\s y \ne 0 $$

Herefter ophæver vi logaritmen på venstre side således.


$$e^{ln|y|} = e^{kx + c} \s |y| = e^{kx + c} ,\s y \ne 0$$


Vi kan nu omskrive det på højre side sådan.

$$|y| = e^{kx} \cdot e^c ,\s y \ne 0$$
Det nye led ($e^c$) er en konstant, da både $e$ og $c$ er konstanter. Vi ved dog at $e$ er positiv, og derfor også at ledet som helhed er positivt. Dette led kalder vi $K$.

$$K = e^c$$
$$|y|=K \cdot e^{kx},\s y \ne 0 \:\: \cup \:\: K > 0$$

For at isolere $y$ helt, bliver vi nødt til at ophæve den absolutte værdi. Det gør vi ved at sætte $\pm$ foran på begge sider.

$$y= \pm K \cdot e^{kx},\s y \ne 0 \:\: \cup \:\: K > 0$$

Vi kan nu lave en ny konstant, der består af $\pm K$. Dette kan vi fordi, vi ved at $K$, kun kan være positiv. Denne konstant kalder vi $C$. $C$ kan være både positiv og negativ.

$$y= C \cdot e^{kx},\s y \ne 0$$

Vi har nu bevist vores ligning. Noget interessant er, at vi kan inddrage vores nulløsning, for hvis $y = 0$, så kan vi tillægge $C$ værdien 0, så ligningen går op.

$$0 = 0 \cdot e^{kx}$$

Det betyder at vi kan opskrive ligningen uden nogle betingelser.

$$y= C \cdot e^{kx}$$

---

#matematik 
