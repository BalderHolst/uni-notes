# Eigen-values and Vectors
Eigen-value $\lambda$, and eigen-vector $\vec{x}$.
$$A\vec{x} = \lambda\vec{x}, \s \vec{x} \neq \vec{0}$$

The characteristic formula:
$$\det(A_{}- \lambda I) = 0$$
$I$ : [[Specielle Matricer#Identitetsmartix|Identity Matrix]]

$$(A-\lambda I)\vec{x} = \vec{0}$$
For ever eigen-value ($\lambda$), a corresponding eigen-vector ($\vec{x}$) exists.

>[!example]- Example of finding eigen-values and vectors
>
>$$
>A=
>\left(
>\begin{array}{cc}
 >-5 & 2 \\
 >2 & -2 \\
>\end{array}
>\right)
>$$
>
>Finding $\lambda$.
>
>$$\det(A-\lambda I) = 0 \arrow
>\lambda =
>\begin{cases}
>-1 \\
>-6
>\end{cases}
>$$
>
>
>For every $\lambda$, do this:
>
>$$(A-I \lambda)\vec{x} = \vec{0}$$
>$$A-I \lambda = 
>\left(
>\begin{array}{cc}
 >-5 & 2 \\
 >2 & -2 \\
>\end{array}
>\right)-
>\left(
>\begin{array}{cc}
 >\lambda  & 0 \\
 >0 & \lambda  \\
>\end{array}
>\right)
>$$
>
>Multiplying with $\vec{x}$ and using the first eigen-value.
>$$\left(
>\begin{array}{cc|c}
 >0 & 0 & 0 \\
 >2 & -1 & 0 \\
>\end{array}
>\right) 
>\arrow
>\begin{cases}
>x_{1}=2 \\
>x_{2}=-1
>\end{cases}
>$$
>
>The same should be calculated for the other eigen-value.

>[!video]- Video
>![](https://www.youtube.com/watch?v=PFDu9oVAE-g)

---
#matematik #matricer #linearalgebra 
