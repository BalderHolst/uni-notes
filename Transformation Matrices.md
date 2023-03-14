# Transformation Matrices

$$
\left(
\begin{array}{cccc}
 r_{11} & r_{12} & r_{13} & p_x \\
 r_{21} & r_{22} & r_{23} & p_y \\
 r_{31} & r_{32} & r_{33} & p_z \\
 w_x & w_y & w_z & s \\
\end{array}
\right)
$$

In kinematics we only interested in rotation and translation. Shering is therefore disabled.

$$
\left(
\begin{array}{cccc}
 r_{11} & r_{12} & r_{13} & p_x \\
 r_{21} & r_{22} & r_{23} & p_y \\
 r_{31} & r_{32} & r_{33} & p_z \\
 0 & 0 & 0 & s \\
\end{array}
\right) 
=
\left(
\begin{array}{cc}
 ^A_BR & ^Ap_{org} \\
 0^{3 \times 1} & 1 \\
\end{array}
\right)
$$

### Pure Rotation

$$
\left(
\begin{array}{cccc}
 1 & 0 & 0 & p_x \\
 0 & 1 & 0 & p_y \\
 0 & 0 & 1 & p_z \\
 0 & 0 & 0 & s \\
\end{array}
\right) 
$$

### Pure Translation

$$
\left(
\begin{array}{cccc}
 r_{11} & r_{12} & r_{13} & 0 \\
 r_{21} & r_{22} & r_{23} & 0 \\
 r_{31} & r_{32} & r_{33} & 0 \\
 0 & 0 & 0 & s \\
\end{array}
\right) 
$$

### The Inverse Transformation Matrix

$$
\left(
\begin{array}{cc}
 \left(^A_BR^T\right) & -\left(^A_BR^T\right)^Ap_{Borg} \\
 0^{3 \times 1} & 1 \\
\end{array}
\right)
$$


## Combining Rotation and Translation

We use [[Rotational Matrices|rotational matrixes]] for rotations, and vectors for translations.

$$
\begin{align}
^{A}P &=\ ^A_{B}R \ ^BP +\ ^AP_{Aorg} \\ \\
^{A}P &=\ ^A_{B}R^{-1} \ ^BP -\ ^AP_{Borg}
\end{align}
$$

![[Pasted image 20230314084221.png|center|400]]

This is easy enough if we only have two or three frames, but becomes quite complicated if we have more frames.

---
#kinematik 
