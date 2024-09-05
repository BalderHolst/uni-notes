# Rotational Matrices

A way to translate rotation between [[Frames|frames]].

Assuming that we are working in three dimensions, the rotational matrix will always be in $\R^{3 \times 3}$ space.

$$^{A}_{B} R = \left[^{A}\hat{X}_{B} \,\,^{A}\hat{Y}_{B}  \,\, ^{A}\hat{Z}_{B} \right] = \left(
\begin{array}{ccc}
 r_{11} & r_{12} & r_{13} \\
 r_{21} & r_{22} & r_{23} \\
 r_{31} & r_{32} & r_{33} \\
\end{array}
\right)$$

The *columns* are the unit vectors of $\set{B}$ seen from $\set{A}$.

### Properties
[[Den Inverse af en Matrix|The inverse]] and the [[Matrix#Transponering|transposed]] both swap reference. Because of this we usually prefer to transpose the matrix.
$$^A_BR^{-1} =\ ^A_BR^{T} = \ ^B_AR$$


### Rotating Points


$$^AP = \  ^A_BR \cdot \ ^BP$$


This opertation is **NOT PERMITTED**.
$$\bcancel{\cancel{^AP = \  ^B_AR \cdot \ ^BP}}$$

## Using Angles

>[!video]- Derivation
>![](https://www.youtube.com/watch?v=gkyuLPzfDV0)

>[!tip]- Rotation around the x-axis
>$$R = \left(
>\begin{array}{ccc}
>   1 & 0 & 0 \\
>   0 & \cos\theta & -\sin\theta \\
>   0 & \sin\theta & \cos\theta \\
>\end{array}
>\right)$$


---
#matematik #matricer #kinematics
