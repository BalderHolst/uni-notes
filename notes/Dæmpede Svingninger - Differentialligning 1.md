# Dæmpede Svingninger

$$a \cdot y'' + b \cdot y' + c \cdot y = 0 \arrows (a \cdot r^2 + br + c) \cdot e^{rt} = 0$$

>[!note]- Udledning
>### Udledning 
>
>$$a \cdot y'' + b \cdot y' + c \cdot y = 0$$
>Gæt på løsning
>$$\begin{align}
>y(t) & = e^{rt} \\
>y'(t) & = r \cdot  e^{rt} \\
>y''(t) & = r^2 \cdot e^{rt}
>\end{align}$$
>
>Sætter ind
$$a \cdot r^2 \cdot e ^{rt} + b \cdot r \cdot e^{rt} + c \cdot e^{rt} = 0$$
>
>Sætter $e^{rt}$ uden for parentes
$$(a \cdot r^2 + br + c) \cdot e^{rt} = 0$$
>
>Parentesen er et [[Andengradspolynomier|andengradspolynomie]]. 

#### Rødder, dæmpningstype og løsninger

*Variabler*
$A$ : Den første integrationskonstant.
$B$ : Den anden integrationskonstant.
$r$ : rod/rødder.

**Overdæmpet**: to reelle (eller imaginære) rødder.
$$y(x) = A \cdot e^{r_1x} + B \cdot e^{r_2x}$$

**Kritisk Dæmpet**: én dobbeltrod.
$$y(x) = A \cdot e^{rx} + B \cdot x \cdot e^{rx}$$

**Underdæmpet**: Når der kun er [[Komplekse Tal|imaginære]] løsninger.
$$y(x) = A \cdot e^{kx} \cdot \cos(\omega x) + B \cdot  e^{kx} \cdot \sin(\omega x)$$
$$r = k \pm \omega i$$
$k$ : det reelle komponent af $r$.
$w$ : det imaginære komponent af $r$.

---
#matematik #differentialligninger 