# Rotational Matrices

A way to translate rotation between [[Frames|frames]].

Assuming that we are working in three dimensions, the rotational matrix will always be in $\R^{3 \times 3}$ space.

$$^A_BR = \left(
\begin{array}{ccc}
 r_{11} & r_{12} & r_{13} \\
 r_{21} & r_{22} & r_{23} \\
 r_{31} & r_{32} & r_{33} \\
\end{array}
\right)$$

The *columns* describe the axes of $\{B\}$ in reference frame $\{A\}$.
The *rows* describe the axes of $\{A\}$ in rotated frame $\{B\}$.

### Properties
[[Den Inverse af en Matrix|The inverse]] and the [[Matricer#Transponering|transposed]] both swap reference.
$$^A_BR^{-1} = ^A_BR^{T} = \,^B_AR$$


### Rotating Points


$$^AP = \, ^A_BR \cdot \,^BP$$


This opertation is **NOT PERMITTED**.
$$\bcancel{\cancel{^AP = \, ^B_AR \cdot \,^BP}}$$

## Using Angles

>[!video]- Derivation
><iframe width="560" height="315" src="https://www.youtube.com/embed/gkyuLPzfDV0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

>[!tip]- Rotation around the $x$-axis
>$$R = \left(
>\begin{array}{ccc}
>   1 & 0 & 0 \\
>   0 & \cos\theta & -\sin\theta \\
>   0 & \sin\theta & \cos\theta \\
>\end{array}
>\right)$$


---
#matematik #matricer #kinematik