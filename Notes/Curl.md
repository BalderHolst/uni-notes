# Curl
A measure of average rotation around points in a [[Vector Fields|vector field]].

$$\mathbf{curl}\ \vec{v}(x,y) = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y},\ \text{where}\ \vec{v}(x,y) = 
\begin{bmatrix}
P(x,y) \\  Q(x,y)
\end{bmatrix}
$$

$$
\begin{cases}
\mathbf{curl}\ \vec{v}(x,y) > 0 &\Rightarrow &\text{counter clockwise flow} \\
\mathbf{curl}\ \vec{v}(x,y) < 0 &\Rightarrow &\text{clockwise flow} \\
\mathbf{curl}\ \vec{v}(x,y) = 0 &\Rightarrow &\text{no rotation}
\end{cases}
$$

>[!video]- 2D-curl
>![](https://www.youtube.com/watch?v=qF9Kz37Ksq0&list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7&index=56)

### 3-Dimensions

$$
\vec{v}(x,y,z) =
\begin{bmatrix}
f_1(x,y,z) \\
f_2(x,y,z) \\
f_3(x,y,z)
\end{bmatrix}
$$
$$\mathbf{curl}\ \vec{v}(x,y,z) = \nabla \times \vec{v}(x,y,z) = 
\begin{bmatrix}
\frac{\partial}{\partial x} \\
\frac{\partial}{\partial y} \\
\frac{\partial}{\partial z}
\end{bmatrix}
\times
\begin{bmatrix}
P(x,y,z) \\
Q(x,y,z) \\
R(x,y,z)
\end{bmatrix}
=
\det
\begin{bmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
f_{1} & f_2 & f_3
\end{bmatrix}
$$
$$
=
\begin{align}
\left(\frac{\partial f_{3}}{\partial y} - \frac{\partial f_{2}}{\partial z}\right) i +
\left(\frac{\partial f_{1}}{\partial z} - \frac{\partial f_{3}}{\partial x}\right) j +
\left(\frac{\partial f_{2}}{\partial x} - \frac{\partial f_{1}}{\partial y}\right) k
\end{align}
$$


>[!video]- 3D-curl
>![](https://www.youtube.com/watch?v=a_49iMi10kg&list=PLSQl0a2vh4HC5feHa6Rc5c0wbRTx56nF7&index=62)

---
#multivariablemath #vectorfields