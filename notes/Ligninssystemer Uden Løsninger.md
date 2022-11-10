# [[Linære Ligninssystemer|Ligninssystemer]] Uden Løsninger

Når koefficient-delen og højresiden af den [[Linære Ligninssystemer#Den udvidede Matrix|udvidede]] matrix har *forskellig* [[Rang af Matrix|rang]], så har ligningssystemet ingen løsninger. 
$$\rang(A) \neq \rang(\tilde{A}) \arrow \text{Ingen løsninger!}$$

### Eksempel
$$
\begin{cases} 
3x_{1} + 2 x_{2} + x_{3} &= 3  \\
6x_{1} + 3x_{2} + 3x_{3} &= 0 \\
6x_{1} + 2x_{2} + 4x_{3} &= 6
\end{cases} 
\arrow 
\left(
\begin{array}{ccc|c}
 3 & 2 & 1 & 3 \\
 0 & -1 & 1 & -6 \\
 0 & -2 & 2 & 0 \\
\end{array}
\right) 
\sim
\left(
\begin{array}{ccc|c}
 3 & 2 & 1 & 3 \\
 0 & -1 & 1 & -6 \\
 0 & 0 & 0 & 12 \\
\end{array}
\right) 
\s \text{VRØVL!}
$$

---
#matematik 