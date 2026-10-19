---
created: 2026-10-19
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 6 slides.pdf|Lektion 6 slides]]"
---

# Extended Kalman Filter
A [[Kalman Filter|kalman filter]] based on a *non-linear* model. We linearize around this function at the currently predicted states, which works well for small deviations, but also means that the filter can diverge.

$$
\begin{align}
x_{k} &= f(x_{k-1}, v_{k-1}, w_{k-1}) \\
z_{k} &= h(x_{k-1}) + v_{k-1}
\end{align}
$$

$f$: Non-linear system function. This should be known.
The system noise is usually additive: $f(x_{k-1}, v_{k-1}) + w_{k-1}$

$h$: Non-linear output function.
$k$: Time step
$x_{k}$: States as a given time step
$w_{k}$: Noise


### Procedure

**Predict**
Our best guesses are the predicted values from last step.

Predicted State:
$$
\hat{x}_{k}^{-} = f(\hat{x}_{k-1}, v_{k-1}, 0)
$$
Predicted Output:
$$
\hat{z}_{k}^{-} = h(\hat{x}_{k}^{-}, 0)
$$
**Find *deviations***

$$
\underbrace{(x_{k} - \hat{x}_{k}^{-})}_{\Delta x_{k}} =
A_{k}
\underbrace{(x_{k-1} - \hat{x}_{k-1})}_{\Delta x_{k-1}}
  + W_{k}
\underbrace{(w_{k-1} - 0)}_{\Delta w_{k-1}}
$$
State Jacobians:
$$
\begin{align}
A_{k} &= \Big\{
\frac{\partial f_{i}}{\partial x_{j}}
\Big\}_{ij} {\Huge|}_{
\begin{pmatrix}
\hat{x}_{k-1} \\
v_{k-1} \\
0
\end{pmatrix}
}
=
{\tiny
\begin{bmatrix}
\frac{\partial f_{1}}{\partial x_{1}} &  \cdots & \frac{\partial f_{1}}{\partial x_{n}} \\
\frac{\partial f_{2}}{\partial x_{1}} &  \cdots & \frac{\partial f_{2}}{\partial x_{n}} \\
\vdots & \vdots &  \vdots \\
\frac{\partial f_{n}}{\partial x_{1}} &  \cdots & \frac{\partial f_{n}}{\partial x_{n}} \\
\end{bmatrix}
}
{\Huge |}_{
\tiny
\begin{pmatrix}
\hat{x}_{k-1} \\
v_{k-1} \\
0
\end{pmatrix}
} \\

W_{k} &= \Big\{
\frac{\partial f_{i}}{\partial w_{j}}
\Big\}_{ij} {\Huge|}_{
\begin{pmatrix}
\hat{x}_{k-1} \\
v_{k-1} \\
0
\end{pmatrix}
}
=
{\tiny
\begin{bmatrix}
\frac{\partial f_{1}}{\partial w_{1}} &  \cdots & \frac{\partial f_{1}}{\partial w_{n}} \\
\frac{\partial f_{2}}{\partial w_{1}} &  \cdots & \frac{\partial f_{2}}{\partial w_{n}} \\
\vdots & \vdots &  \vdots \\
\frac{\partial f_{n}}{\partial w_{1}} &  \cdots & \frac{\partial f_{n}}{\partial w_{n}} \\
\end{bmatrix}
}
{\Huge |}_{
\tiny
\begin{pmatrix}
\hat{x}_{k-1} \\
v_{k-1} \\
0
\end{pmatrix}
}
\end{align}
$$
And output deviation
$$
\underbrace{(z_{k} - \hat{z}_{k}^{-})}_{\Delta z_{k}} = H_{k} \underbrace{(x_{k} - \hat{x}_{k}^{-})}_{\Delta x_{k}} + V_{k} \underbrace{(v_{k} - 0)}_{\Delta v_{k}}
$$
Output Jacobians

$$
\begin{align}
H_{k} &= \Big\{
\frac{\partial h_{i}}{\partial x_{j}}
\Big\}_{ij} {\Huge|}_{
\begin{pmatrix}
\hat{x}_{k-1} \\
0
\end{pmatrix}
}
=
{\tiny
\begin{bmatrix}
\frac{\partial h_{1}}{\partial x_{1}} &  \cdots & \frac{\partial h_{1}}{\partial x_{n}} \\
\frac{\partial h_{2}}{\partial x_{1}} &  \cdots & \frac{\partial h_{2}}{\partial x_{n}} \\
\vdots & \vdots &  \vdots \\
\frac{\partial h_{m}}{\partial x_{1}} &  \cdots & \frac{\partial h_{m}}{\partial x_{n}} \\
\end{bmatrix}
}
{\Huge |}_{
\tiny
\begin{pmatrix}
\hat{x}_{k-1} \\
0
\end{pmatrix}
} \\

V_{k} &= \Big\{
\frac{\partial h_{i}}{\partial v_{j}}
\Big\}_{ij} {\Huge|}_{
\begin{pmatrix}
\hat{x}_{k-1} \\
0
\end{pmatrix}
}
=
{\tiny
\begin{bmatrix}
\frac{\partial h_{1}}{\partial v_{1}} &  \cdots & \frac{\partial h_{1}}{\partial v_{m}} \\
\frac{\partial h_{2}}{\partial v_{1}} &  \cdots & \frac{\partial h_{2}}{\partial v_{m}} \\
\vdots & \vdots &  \vdots \\
\frac{\partial h_{m}}{\partial v_{1}} &  \cdots & \frac{\partial h_{m}}{\partial v_{m}} \\
\end{bmatrix}
}
{\Huge |}_{
\tiny
\begin{pmatrix}
\hat{x}_{k-1} \\
0
\end{pmatrix}
} \\
\end{align}
$$

In case of additive noise
$$
V_k = I_{(m \times m)}
$$
