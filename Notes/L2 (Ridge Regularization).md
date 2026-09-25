# L2 (Ridge Regularization)
Called "Ridge Regularization" in linear models and "L2" in logistic regressions and other contexts.

L2 (Ridge) is a loss function. It introduces the $\lambda$ hyperparameter. This should be tuned using validation data.

Here, the number of paremeters in the model and their magnitude are punished.

$$
L_{\mathrm{Ridge}} = \frac{1}{n} \sum_{i=1}^{n} (y - \hat{y})^{2} + \lambda \sum^{W}_{j=1} W_{j}^{2}
$$
$\lambda$: How much to punish complexity. Tunable hyperparameter (use validation data for this).
$W$: Weights.
$n$: Number of samples
$y$: Actual sample values
$\hat{y}$: Predicted (by current model) sample values

### Closed form Solution for Linear Regressions


$$
W = (X^{T}X + \lambda I)^{-1} X^{T}y
$$
Where $I$ is an identity matrix that is $0$ for its last element, as the bias should not be effected by $\lambda$.
$$
I =
\begin{bmatrix}
1 & 0 & \cdots & \cdots & 0 \\
0 & 1 & \cdots &  \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\vdots & \vdots &  \vdots & 1 & \vdots \\
0 & 0 & \cdots & \cdots & 0 \\
\end{bmatrix}
$$

$W$: Weight vector
$X$: Data vector
$\lambda$: Ridge hyperparameter
$y$: Actual sample values

---
#machine-learning