# Logistic Regressions
Finds the *maximum likelihood* seperation line.

![[Pasted image 20260924122217.png|400]]
$$
z = Wx + b
$$

$z$ is a class.

$$
\hat{y} = \sigma(z) = \frac{1}{1 + e^{-(Wx + b)}}
$$
$\sigma$: [[Sigmoid|Sigmoid Activation Function]]

#### Gradients
We use the [[Binary Cross Entropy]] loss function.
$$
L = - \frac{1}{n} \sum \Big [
y_{i} \log(\hat{y}_{i}) + (1 - y_{i}) \log(1-\hat{y}_{i})
\big]
$$

Gradients can then be found to be:
$$
\begin{align}
\frac{\partial L}{\partial z} &= \frac{\partial L}{\partial \hat{y}} \frac{\partial \hat{y}}{\partial z} =\frac{1}{n} \sum_{i=1}^{n}(\hat{y}_{i} - y_{i}) \\
\frac{\partial L}{\partial W} &= \frac{\partial L}{\partial z} \frac{\partial z}{\partial W} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_{i} - y_{i}) x_{i} \\
\frac{\partial L}{\partial b} &= \frac{\partial L}{\partial z} \frac{\partial z}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_{i} - y_{i}) \cdot 1
\end{align}
$$

Closed form solution:
$$
W = (X^{T}X)^{-1} X^{T}y
$$

#### L1 and L2 loss function
We can also