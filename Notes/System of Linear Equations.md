# System of Linear Equations
> *"Vi vil gerne have noget der er linært, for så er det nemt at regne på"*
> \- Preben

Can be solved with the [[#Extended Matrix]].

$m$ equations with $n$ unknowns.

$a_{ij}$: Coefficients
$x_{i}$: Variables
$b_{i}$: Constants

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
## Linear Algebra Notes
```dataview 
list
from #linearalgebra 
sort file.name
```
---

### Extended Matrix
Write the system of equation by omitting the variable vector.

$$\tilde{A} = \left(
\begin{array}{cccc|c}
 a_{11} & a_{12} & \dots  & a_{1n} & b_1 \\
 \vdots  & \vdots  & \ddots  & \vdots & \vdots  \\
 a_{m1} & a_{m2} & \dots  & a_{mn} & b_n\\
\end{array}
\right)$$

Every row is an equation.

### Solutions for Systems of Linear Equations
See [[Rank of Matrix]].

$m$ equations and $n$ unknowns: 

There are one **or more** solutions if (and only if):
$$\mathrm{rank}(A) = \mathrm{rank}{(\tilde{A})}$$

**Only one** solution exists if (and only if):
$$\mathrm{rank}(A)=\mathrm{rank}(\tilde{A})=n$$

An ***infinite amount** of solutions exist if:
$$\mathrm{rank}(A) < n \s \text{og} \s \mathrm{rank}{(A)} = \mathrm{rank}(\tilde{A})$$


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
