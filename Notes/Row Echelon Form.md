# Row Echelon Form

> The Pivot-element is always to the left of the Pivot-element in the row above.


*Pivot-element*: The first non-zero in a row.


>[!Example]- Examples
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

##### Requirements
- Row Echelon form
- All Pivot-elements are $1$
- All numbers *above* the Pivot-element are $0$.

>[!Example]- Example
>$$
>\left(
>\begin{array}{ccccc}
> 1 & 0 & 0 & 0 & -1 \\
> 0 & 1 & 2 & 0 & -4 \\
> 0 & 0 & 0 & 1 & -1 \\
>\end{array}
>\right)
>$$

---
#matematik #matricer
