# Perceptron
Simple classification algorithm. Linearly seperates bulk data. *Always* finds *a* line if one exists.


![[perceptron-plot.png|250]]

$$
z = w_{1}x_{1} + w_{2}x_{2} +b
$$
$w_{1}$: Weight 1
$w_{2}$: Weight 2
$b$: Bias

The *decision boundary* is at $z=0$:
$$
\begin{cases}
z \geq 0 \rightarrow \hat{y} = 1 \\
z < 0 \rightarrow \hat{y} = 0
\end{cases}
$$
$\hat{y}$: Class

## Update
> "Error is the sum of changes for evert datapoint that was classified wrong"

> [!warning] No the *best* line
> The resulting line will find *a* line that seperates the two datasets, but it will **not be the best**, just the first line found.

Setup:
$$
\begin{align}
w &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
b &= 0 \\
\end{align}
$$
Step 1:
$$
\hat{y} \leftarrow z
$$

Step 2:
$$
w \leftarrow \eta(y-\hat{y}) \cdot x + w
$$
$y$: Annotated data (ground truth)
$\eta$: Learning rate

##### As Matrix Multiplication
$$
z = \mathbf{x} \cdot W
=
\begin{bmatrix}
x_{1} & x_{2} & 1 \\
\vdots & \vdots & \vdots \\
\vdots & \vdots & \vdots
\end{bmatrix}
\begin{bmatrix}
w_{1} \\ w_{2} \\ b
\end{bmatrix}
$$

---
#machine-learning
