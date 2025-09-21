# Axis Angle (Euler Vector)
A way of defining a rotation with an axis and an angle. See [[Lecture 5 - Other Orientation Representations.pdf#page=30|slides]].

![[Axis-Angle-Euler-Vector.png|300]]

Can be given seperately or combined:
$$
\theta, \, \hat{K} = \begin{bmatrix} k_x \\ k_y \\ k_z \end{bmatrix} 
\s \text{or} \s
K = \theta \hat{K} = \begin{bmatrix} \theta k_x \\ \theta k_y \\ \theta k_z \end{bmatrix} 
$$

>[!video]- Video
>![](https://www.youtube.com/watch?v=zrDCI89bSp4)

### Rodrigues' formula
Calculate the equivalent rotation matrix.

$$
^A_BR(\ ^AK, \theta\ ) = I \cos(\theta) + KK^{-1} (1 - \cos(\theta)) + \hat{K} \sin(\theta)
$$




---
#kinematics 
