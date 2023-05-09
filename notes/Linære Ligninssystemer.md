# Linære Ligningssystemer
> *"Vi vil gerne have noget der er linært, for så er det nemt at regne på"*
> \- Preben

Kan løses enten med [[#Den udvidede Matrix|den udvidede matrix]] eller [[Den Inverse af en Matrix#Løs ligningssystem med den Inverse Matrix|den inverse matrix]].

$m$ ligninger med $n$ ubekendte.

$a_{ij}$ : koefficienter
$x_{i}$ : variable
$b_{i}$ : konstanter

$$
\begin{cases} 
 a_{11} \cdot  x_{1}+a_{12} \cdot x_{2} + \dots + a_{1n} + x_{n}=b_{1}  \\
 a_{21} \cdot  x_{1}+a_{22} \cdot x_{2} + \dots + a_{2n} + x_{n}=b_{2}   \\
 \s\s\vdots \\
a_{m1} \cdot  x_{1}+a_{m2} \cdot x_{2} + \dots + a_{mn} + x_{n}=b_{m}  
\end{cases}
$$
$$\Downarrow$$
$$
\left(
\begin{array}{cccc}
 a_{11} & a_{12} & \dots  & a_{1n} \\
 \vdots  & \vdots  & \ddots  & \vdots  \\
 a_{m1} & a_{m2} & \dots  & a_{mn} \\
\end{array}
\right)
\cdot
\left(
\begin{array}{c}
 x_1 \\
 \vdots  \\
 x_n \\
\end{array}
\right) = 
\left(
\begin{array}{c}
 b_1 \\
 \vdots  \\
 b_n \\
\end{array}
\right)
$$

---
## Noter
```dataview 
list
from #linæralgebra  
sort file.name
```
---

### Den udvidede Matrix
En nemmere måde at opskrive ligningssystemer, hvor den variable undlades.
$$\tilde{A} = \left(
\begin{array}{cccc|c}
 a_{11} & a_{12} & \dots  & a_{1n} & b_1 \\
 \vdots  & \vdots  & \ddots  & \vdots & \vdots  \\
 a_{m1} & a_{m2} & \dots  & a_{mn} & b_n\\
\end{array}
\right)$$
Her repræsenterer hver række hver ligning.


### Løsninger af Linære Ligningssystemer
$m$ ligninger og $n$ ubekendte: 

Der er én eller ***flere*** løsninger hvis kun hvis (se [[Rang af Matrix]]):
$$\rang(A) = \rang{(\tilde{A})}$$
Der er ***én*** løsning hvis og kun hvis
$$\rang(A)=\rang(\tilde{A})=n$$

Der eksisterer ***uendelig mange*** løsninger hvis:
$$\rang(A) < n \s \text{og} \s \rang{(A)} = \rang(\tilde{A})$$


### Homogene Linære Ligningssystemer

$$A\vec{x} = \vec{0}$$
Har **altid** mindst *én* løsning: $\vec{x}=\vec{0}$ (den trivielle løsning).

### Regler for Løsning af Ligningssystemer
I almindelige linære ligningssystemer må vi
- Bytte om på rækkefølgen af to ligninger.
- Lægge en ligning (eller et multiplum heraf) til en anden ligning.
- Gange en ligning med en konstant (hvis $k\neq 0$)

##### Gauss  Elimination
De samme regneregler bare for ligningssystemet på [[#Den udvidede Matrix|matrixform]].
- Bytter to rækker med hinanden.
- Lægge en række (eller et multiplum heraf ) til en anden række.
- Gange en række med en konstant (hvis $k\neq 0$)

---
#matematik #subject