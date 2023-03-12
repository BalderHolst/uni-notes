# Egenværdier og Egenvektorer
Egenværdi $\lambda$, og egenvektor $\vec{x}$.
$$A\vec{x} = \lambda\vec{x}, \s \vec{x} \neq \vec{0}$$

Opstil *den karakteristiske* ligning
$$\det(A_{}- \lambda I) = 0$$
$I$ : [[Specielle Matricer#Identitetsmartix|Identitetsmatrix]]

$$(A-I \lambda)\vec{x} = \vec{0}$$

For hver egenværdi ($\lambda$), findes en tilhørende egenvektor $\vec{x}$.

>[!example]- Eksempel
>
>$$
>A=
>\left(
>\begin{array}{cc}
 >-5 & 2 \\
 >2 & -2 \\
>\end{array}
>\right)
>$$
>
>Finder $\lambda$.
>
>$$\det(A-\lambda I) = 0 \arrow
>\lambda =
>\begin{cases}
>-1 \\
>-6
>\end{cases}
>$$
>
>
>For hver $\lambda$-værdi gør man dette
>
>$$(A-I \lambda)\vec{x} = \vec{0}$$
>$$A-I \lambda = 
>\left(
>\begin{array}{cc}
 >-5 & 2 \\
 >2 & -2 \\
>\end{array}
>\right)-
>\left(
>\begin{array}{cc}
 >\lambda  & 0 \\
 >0 & \lambda  \\
>\end{array}
>\right)
>$$
>
>Ganger $\vec{x}$ ind og bruger den første egenværdi ($\lambda_{1}$).
>$$\left(
>\begin{array}{cc|c}
 >0 & 0 & 0 \\
 >2 & -1 & 0 \\
>\end{array}
>\right) 
>\arrow
>\begin{cases}
>x_{1}=1 \\
>x_{2}=2
>\end{cases}
>$$
>Det samme gøres med den anden egenværdi.

---
#matematik #matricer 
