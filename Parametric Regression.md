# Parametric Regression
> *"We are trying to fit into the dataset"*
> \- Ela

We are fitting the line $\widehat{y} = wx + b$ to the data.

![[Pasted image 20260917122445.png|300]]

x: Input (can my multi-dimensional)
y: Output / Target

Error:
$$
\begin{align}
e &= y - \hat{y} \\
&= (y - (wx + b))
\end{align}
$$

### Loss Functions Gradients

#### Mean Square Error ([[Mean Square Error (MSE)|MSE]]):
$$
\nabla L = \left( - \frac{2}{n} \sum x_{i}e_{i}m,\ - \frac{2}{n} \sum e_{i}\right)
$$
**Closed from MSE**:

$$
X =
\begin{bmatrix}
x_{1} & x_{2} & \dots & x_{m} & 1 \\
\vdots &  \vdots & \vdots & \vdots & 1
\end{bmatrix}
\quad
W =
\begin{bmatrix}
w_{1} \\
\vdots \\
w_{n} \\
b
\end{bmatrix}
\quad
Y =
\begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots \\
y_{n} \\
\end{bmatrix}
$$

$m$: Number of dimensions
$n$: Number of Samples
$X$: Cases as rows, features + 1 as columns
$W$: Column vector of weights and single bias
$Y$: Output / Target values in the dataset

Optimized weights:
$$
w = (X^{T}X)^{-1} X^{T}Y
$$
#### Mean Absolute Error ([[Mean Absolute Error (MAE)|MAE]]):
$$
\nabla L = (- \frac{1}{n} \sum \mathrm{sign}(e)x,\ \frac{1}{n} \mathrm{sign}(e))
$$
A closed form solution *does not exist*.


---
#machine-learning