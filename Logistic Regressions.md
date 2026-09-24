# Logistic Regressions
Finds the *maximum likelihood* seperation line.

![[Pasted image 20260924122217.png|400]]
$$
z = wx + b
$$

$z$ is a class.

$$
\hat{y} = \sigma(z)
$$
$\sigma$: [[Sigmoid|Sigmoid Activation Function]]

#### Gradients
$$
\begin{align}
\frac{\partial L}{\partial z} &= \frac{\partial L}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial z} =\frac{1}{n} \sum_{i=1}^{n}(\hat{y}_{i} - y_{i}) \\
\frac{\partial L}{\partial w} &= \frac{\partial L}{\partial z} \frac{\partial z}{\partial w} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_{i} - y_{i}) x_{i} \\
\frac{\partial L}{\partial b} &= \frac{\partial L}{\partial z} \frac{\partial z}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_{i} - y_{i}) \cdot 1
\end{align}
$$


---
#machine-learning