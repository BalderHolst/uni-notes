# Den Inverse af en Matrix
$$A^{-1} \cdot A = I$$
$I$ : [[Specielle Matricer#Identitetsmartix|Identitetsmatrix]]

---

Udgangspunkt: [[Linære Ligninssystemer|ligningssystem]]
$$A\vec{x} = \vec{b}$$
"Dividerer med $A$" ($A^{-1}$ eksisterer kun hviss $\det(A) \neq 0$)
$$A^{-1} \cdot A\vec{x} = A^{-1} \cdot  \vec{b}$$
$$I\vec{x} = A^{-1} \cdot \vec{b} \arrow \vec{x} = A^{-1}\cdot \vec{b}$$

---

### At finde den Inverse
$$
A^{-1} =\left(
\begin{array}{cccc}
 a_{11} & a_{12} & a_{13} & a_{14} \\
 a_{21} & a_{22} & a_{23} & a_{24} \\
 a_{31} & a_{32} & a_{33} & a_{34} \\
 a_{41} & a_{42} & a_{43} & a_{44} \\
\end{array}
\right)^{-1}
$$
$$\Downarrow$$
$$
\left(
\begin{array}{cccc|cccc}
 a_{11} & a_{12} & a_{13} & a_{14} & 1 & 0 & 0 & 0 \\
 a_{21} & a_{22} & a_{23} & a_{24} & 0 & 1 & 0 & 0 \\
 a_{31} & a_{32} & a_{33} & a_{34} & 0 & 0 & 1 & 0 \\
 a_{41} & a_{42} & a_{43} & a_{44} & 0 & 0 & 0 & 1 \\
\end{array}
\right) \s = \s
\left(
\begin{array}{cccc|cccc}
 1 & 0 & 0 & 0 & b_{11} & b_{12} & b_{13} & b_{14} \\
 0 & 1 & 0 & 0 & b_{21} & b_{22} & b_{23} & b_{24} \\
 0 & 0 & 1 & 0 & b_{31} & b_{32} & b_{33} & b_{34} \\
 0 & 0 & 0 & 1 & b_{41} & b_{42} & b_{43} & b_{44} \\
\end{array}
\right)
$$
$$\Downarrow$$
$$A^{-1} = \left(
\begin{array}{cccc}
 b_{11} & b_{12} & b_{13} & b_{14} \\
 b_{21} & b_{22} & b_{23} & b_{24} \\
 b_{31} & b_{32} & b_{33} & b_{34} \\
 b_{41} & b_{42} & b_{43} & b_{44} \\
\end{array}
\right)$$

---
#matematik #matricer 