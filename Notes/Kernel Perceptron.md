---
created: 2026-10-22
tags:
  - machine-learning
---
# Kernel Perceptron
A [[Perceptron|perceptron]] with a different [[Kernel Methods|kernel]].

Here we redefine the meaning of weights and biases.
$$
\begin{align}
W &= \sum_{i=1}^{u}\alpha_{i} (y_{i} - \hat{y}_{i}) x_{i} \\
b &= \sum_{i=1}^{u}\alpha_{i} (y_{i} - \hat{y}_{i})
\end{align}
$$
$\alpha_{i}$: How many times this point was misclsssified.
$u$: Number of datapoints

We train the same was as the [[Perceptron|normal perceptron]], but here we use another [[Kernel Methods|kernel]]:
$$
z = f(x) = W x + b = \sum_{i=1}^{u} \alpha_{i}\ y_{i}\ K(x_{i}, x) + \sum_{i=1}^{u} \alpha_{i} y_{i}
$$

##### Collapsing into a Weight Vector
If the lifting function $\phi(x)$ can be found, we can calculate weights and biases **after training**, to minimize the data we have to carry when classifying points. This is for example noe possible using the [[Kernel Methods#RBF - Radial Bases Function Kernel|RBF kernel]].
$$
\begin{align}
W &= \sum_{i=1}^{u}\alpha_{i} y_{i}\phi(x_{i}) \\
b &= \sum_{i=1}^{u}\alpha_{i} y_{i}
\end{align}
$$


