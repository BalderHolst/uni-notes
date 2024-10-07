# Master Theorem
If
$$
T(n) = a \cdot T\left(\frac{n}{b}\right) + O(n^{d})
$$
then
$$
T(n) =
\begin{cases}
O(n^{d} \log(n)),  &\mathrm{if}\; a = b^{d} \\
O(n^{d})          &\mathrm{if}\; a < b^{d} \\
O(n^{\log_{b}(a)})          &\mathrm{if}\; a > b^{d}
\end{cases}
\;\;\;\;\;
\mathrm{where}\; a \geq 1,\; b > 1
$$
Where $a$, $b$ and $d$ are all constants.



---
#algorithms 