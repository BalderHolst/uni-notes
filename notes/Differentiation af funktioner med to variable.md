# [[Differentialregning|Differentiation]] af [[Funktioner af flere Variable]] / Partielle Afledte
Lad $f(x,y)$ være en funktion, så er  førsteordens partielle afledte:
$$
\begin{align}
\frac{\partial f}{\partial x} &= f_{1}(x,y) = \frac{f(x+h_{1} \cdot  y)-f(x,y)}{h}\\
\frac{\partial f}{\partial x} &= f_{2}(x,y) = \frac{f(x+h_{2} \cdot  y)-f(x,y)}{h}
\end{align}
$$

---



**Partiels afledt:** en funktion der er differentieret *enten* med hensyn til $x$ eller $y$.

### Praksis
$$
\begin{align}

\frac{\partial f}{\partial x} &\s \to \s
\begin{cases}
\text{Opfat $x$ som \emph{variabel}} \\
\text{Opfat $y$ som \textbf{konstant}}
\end{cases} \s \to \s \text{Differentier i forhold til $x$}
\\ \\
\frac{\partial f}{\partial y} &\s \to \s
\begin{cases}
\text{Opfat $x$ som \textbf{konstant}} \\
\text{Opfat $y$ som   \emph{variabel}}
\end{cases} \s \to \s \text{Differentier i forhold til $y$}

\end{align}
$$
![[Differentieret funktion af to variable - plot.png|center|400]]

---

### Skrivemåde
Differentieret med hensyn til $x$: $f_x'(x,y)$ (hældningen i $x$-retningen given $x$ og $y$)


#### Dobbeltafledt
$$f_{xy}'(x,y)$$
*Rækkefølgen er ligegyldig*



>[!Example]- Eksempel
>
>Bestem $f_x'(x,y)$ og $f_y'(x,y)$, når $f(x,y)=x^2+x \cdot y+\frac{y}{3}-8$ 
>
>Differentierer med hensyn til $x$. $y$ bliver behandlet som en konstant.
>$$f_x'(x,y)=2x+1 \cdot y+ 0 + 0 = 2x+y$$
>Differentierer med hensyn til $y$. $x$ bliver her behandlet som en konstant.
>$$f_y'(x,y)=0+x+\frac{1}{3}+0=x+\frac{1}{3}$$
>
>

---
#matematik #differentialer #funktionerafflerevariable