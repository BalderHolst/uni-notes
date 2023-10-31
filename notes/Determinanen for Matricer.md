## Determinanen for Matricer
Fortæller om en ($n\times n$) matrix $A$ har fuld [[Rang af Matrix|rang]]. The matrix **must be square**.

$$\det(A) \neq 0 \arrow \text{Fuld rang!}$$





#### For $2\times 2$ matricer
$$M=\left( {\begin{array}{cccc} a & b \\ c & d \\ \end{array} } \right)$$
$$det(M) = detM = |M| = ad-cb$$
#### For $3\times 3$ matricer
$$M=
\left( {\begin{array}{cccc}
a & b & c \\
d & e & f \\
g & h & i
\end{array} } \right)$$
$$det(M) = |M| = a \cdot \left|\left( {\begin{array}{cccc} e & f \\ h & i \\ \end{array} } \right)\right| - b \cdot  \left|\left( {\begin{array}{cccc} d & f \\ g & i \\ \end{array} } \right)\right| + c \cdot \left|\left( {\begin{array}{cccc} d & e \\ g & h \\ \end{array} } \right)\right|$$
$$= a \cdot e \cdot i + b \cdot f \cdot g + d \cdot h \cdot c - c \cdot e \cdot g - b \cdot d \cdot i - f \cdot h \cdot a$$
#### For $n\times n$ matricer
>[!tip] Nuller er nice!
> Hvis en række eller søjle *kun* har nuller, **er determinanten nul**. Dette kan nogen gange opnås med at lægge rækker til/trække rækker fra hinanden! 
> 
> Derudover er det smart at *følge rækker med mange nuller*.

$$D = \sum\limits_{j=1}^{n}(-1)^{j+k} \cdot A_{jk} \cdot D_{jk}$$
(Føljer $k$'te søjle)

Eller
$$D = \sum\limits_{k=1}^{n}(-1)^{j+k} \cdot A_{jk} \cdot D_{jk}$$
(Følger $j$'te række)

$D_{jk}$ : Determinanten af $A$ uden række $j$ og søjle $k$.

### Row Echelon form (det slapper!)
$$\left|\left(
\begin{array}{cccc}
 a & 1 & 2 & 3 \\
 0 & b & 1 & 2 \\
 0 & 0 & c & 1 \\
 0 & 0 & 0 & d \\
\end{array}
\right)\right| = abcd$$

### Determinanten og Rækkeoperationer

| **Operation**                             | **Betydning for Determinanten**       |
| ----------------------------------------- | ------------------------------------- |
| Ombyt rækker                              | Skifter fortegn                       |
| Lægge række til en anden                  | *intet*                               |
| Multiplikation a række med konstanten $c$ | Determinanden bliver $c$ gange større |

### Regneregler for Determinanten
Lad $c \in \R$ og $A_{n\times n}$ en matrix.
$$\det(A) =  c^{n} \cdot \det(A)$$
##### Transposition
$$\det(A) = \det(A^{T})$$

##### [[Linært Afhængige Vektorer|Linært Afhængige]] Rækker eller Søjler
$$\det(A) = 0$$

##### Multiplikation
$B_{n\times n}$ er nu en matrix

$$\det(A \cdot B) = \det(B \cdot A) = \det(A) \cdot \det(B)$$
Her er operationsrækkefølgen ligefølgen ligegyldig **IKKE** som at [[Matricer#Gange med matricer|gange med matricer]].

---
#matematik #matricer 