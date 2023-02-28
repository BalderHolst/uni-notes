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

$$R_{\theta}= \left( {\begin{array}{cc} \cos{\theta} & -\sin{\theta} \\ \sin\theta & \cos{\theta} \\ \end{array} } \right)$$
### Rotation around Point
$$p_{roteret} = R_{\theta} \bullet p \s \text{hvor} \s p = \v{x}{y}$$

>[!Example]-  Example
>$$\theta = \frac{\pi}{2}, \s p = \v{1}{0}$$
>$$R_{\frac{\pi}{2}} \bullet p = \left( {\begin{array}{cccc} \cos{\frac{\pi}{2}} & -\sin{\frac{\pi}{2}} \\ \sin\frac{\pi}{2} & \cos{\frac{\pi}{2}} \\ \end{array} } \right) = \left( {\begin{array}{cccc} 0 & -1 \\ 1 & 0 \\ \end{array} } \right) \bullet \v{1}{0} = \v{0}{1}$$

---
#matematik #matricer #kinematik
