# Perceptron
Simple classification algorithm. Linearly seperates bulk data.

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
Error

Setup:
$$
\begin{align}
w_{1} &= 0 \\
w_{2} &= 0 \\
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


---
#machine-learning
