---
created: 2026-09-03
tags: [machine-learning]
---
# Perceptron
Simple classification algorithm. Linearly seperates bulk data. *Always* finds *a* line if one exists.


![[perceptron-plot.png|250]]

$$
z = w_{1}x_{1} + w_{2}x_{2} +b = W \cdot X + b
$$
$w_{1}$: Weight 1
$w_{2}$: Weight 2
$b$: Bias

The *decision boundary* is at $z=0$:
$$
\begin{cases}
z \geq 0 \to \hat{y} = 1 \\
z < 0 \to \hat{y} = 0
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
W &= \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
b &= 0 \\
\end{align}
$$
**Step 1**:
Go through every point, *every epoch*. For each, get its predicted class $\hat{y}$.
$$
\hat{y} \leftarrow z = W \cdot X + b
$$

**Step 2**:
For each datapoint $x$:
$$
w \leftarrow \eta(y-\hat{y}) \cdot x + w
$$
$y$: Annotated data (ground truth)
$\eta$: Learning rate

NOTE: $y-\hat{y}$ is $1$ or $-1$ if the point was misclassified.

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