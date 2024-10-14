# Matrices
A matrix with $m$ rows and $n$ columns.

$$ A_{m\times n} =
\left( {\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}\\
\end{array} } \right)$$

---

## Noter om Matricer
```dataview 
list
from #matricer 
sort file.name
```


---

### Scalar Multiplication
Multiply all elements by the a constant.

$$
M \cdot c
$$

### Matrix Multiplication
$$c_{ij} = \sum_{k=1}^n a_{ik} \cdot b_{kj}$$
$c_{ij}$ is the dot-product of row $i$ of $A$ and column $j$ of $B$.

The number of rows of $A$ must be equal to the number of columns of $B$.
$$A_{a\times b} \cdot B_{b\times c}\s\checkmark$$

Always multiply columns with rows.


##### Non-commutative!
The **order matters**! (Event when the dimensions are the same).

$$A \cdot B \neq B \cdot A$$
##### Associativ
$$A \cdot (B \cdot C) = (A \cdot B) \cdot C$$

##### Resultat
$$C_{n\times p} = A_{n\times m} \cdot B_{m\times p}$$


>[!video]- Multiplying Matrices
>![](https://www.youtube.com/watch?v=vzt9c7iWPxs)


### Addition
- Must have the same dimensions
- Addition happens element-wise

$$A + B = B + A$$

### Kvadratiske matricer
En matrix er kvadratisk hvis den har **lige mange rækker og kolonner**.

### Transposition

$$ A_{m\times n}^T =
\left( {\begin{array}{cccc}
a_{11} & a_{21} & \cdots & a_{1m}\\
a_{11} & a_{22} & \cdots & a_{2m}\\
\vdots & \vdots & \ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{mn}\\
\end{array} } \right) $$
$$\left(A^T\right)^T = A$$

>[!tip] Transposition distributes!
>$$(A \cdot B)^{T} = B^{T} \cdot A^{T}$$

##### Symmetric Matrices
Matrix $A$ is symmetric if $A^T = A$.

All symmetric matrices are quadratic.


---
#matematik #linearalgebra 
