## Digital Realisation Structures
A representation of a digital filter that could be implemented in a programming language. See [[lektion 7 - Digitale realisationsstrukturer.pdf|slides]].

$$
\begin{align}
H(z) &= \frac{Y(z)}{X(z)} = \frac{ \sum_{i=0}^{N} a_{i}z^{-i} }{ 1 + \sum_{i=1}^{N} b_{i} z^{-i} } \\ \\
y(n) &= \sum_{i=0}^{N}  a_{i} \cdot x(n-i) - \sum_{i=1}^{N}b_{i} \cdot y(n-1)
\end{align}
$$
$n$: time step
$x(n)$: input in the discrete time domain
$y(n)$: output in discrete time domain

>[!tip]- Implementing a Transfer Function
>1. Seperate $X(z)$ and $Y(z)$ terms the their own sides of the equation.
>2. Take the [[Notes/z-transformation#Inverse z-transform|inverse z-transformation]] of each part of the equation.
>3. Isolate $y(n)$
>4. Find constants and draw the realisationsstructure

#### Direct Type 1
See [[lektion 7 - Digitale realisationsstrukturer.pdf#page=35|slides]].

This is the intuitive way to implement a discrete transfer function.
![[Pasted image 20231229141244.png|center|350]]

#### Direct Type 2
See [[lektion 7 - Digitale realisationsstrukturer.pdf#page=46|slides]].

>[!tip]- How?
>We split up the transfer funktion with an intermediate function $W(z)$. Note that this does not change the transfer function.
>$$
>H(z) =
>\frac{W(z)}{X(z)} \cdot \frac{Y(z)}{W(z)} =
>\underbrace{\frac{1}{1 + \sum_{i=1}^{N} b_{i}z^{-1}}}_{H_{1}}
>\cdot
>\underbrace{\sum_{i=0}^{N} a_{i} z^{-i}}_{H_{2}}
>$$
>The new transfer functions can be described as follows:
>$$
>\begin{align}
>H_{1}(z) &= \frac{W(z)}{X(z)} = \frac{1}{1 + \sum_{i=1}^{N} b_{i}z^{-1}} \\
>H_{2}(z) &= \frac{Y(z)}{W(z)} = \sum_{i=0}^{N} a_{i} z^{-i}
>\end{align}
>$$
>
>These two transfer functions can be realised like this:
>![[Pasted image 20231229142917.png|center|400]]
>
>The memory xells ($z^{-1}$) now share the same values and can be combined:
>![[Pasted image 20231229143502.png|center|400]]


This is the **better way** of implementing a filter, as it stores half as many values resulting in a less expensive filter implementation.
![[Pasted image 20231229141938.png|center|350]]


---
#signalprocessing
