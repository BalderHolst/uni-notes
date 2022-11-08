# Row Echelon Form
> Pivot-elementet i en række er altid til højre for pivot elementet i rækken over.

*Pivot-element*: første ikke-nul i en række.
*Ønske*: altid nuller under og under-til-venstre.


>[!Example]- Eksempler
>$$
>\left(
>\begin{array}{cccc|c}
> 2 & 1 & -2 & 3 & 1 \\
> 0 & 1 & 2 & 2 & 2 \\
> 0 & 0 & 0 & 1 & 3 \\
>\end{array}
>\right)
>$$
>$$\left(
>\begin{array}{ccc}
> 2 & 3 & 1 \\
> 0 & -1 & 2 \\
> 0 & 0 & 1 \\
>\end{array}
>\right)$$
>Dette er også ok
>$$\left(
>\begin{array}{cccc}
> 1 & 2 & 3 & 4 \\
> 0 & 5 & 6 & 7 \\
> 0 & 0 & 0 & 0 \\
>\end{array}
>\right)$$
>
>Dette er ***ikke*** row echelon form!
>$$
>\left(
>\begin{array}{ccc|c}
> 1 & 2 & 3 & 4 \\
> 0 & 1 & 2 & 3 \\
> 0 & 2 & 1 & 1 \\
> 0 & 0 & 1 & 2 \\
>\end{array}
>\right)
>$$

### Reduceret Row Echelon form
##### Krav
- Row Echelon form
- *Alle* pivot elementer er $1$.
- Alle tal **OVER** pivot-elementet er *nul*.

>[!Example]- Eksempel på reduceret row echelon form
>$$
>\left(
>\begin{array}{ccccc}
> 1 & 0 & 1 & 0 & -1 \\
> 0 & 1 & 2 & 0 & -4 \\
> 0 & 0 & 0 & 1 & -1 \\
>\end{array}
>\right)
>$$

---
#matematik #matricer