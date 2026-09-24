# L1 (Lasso Regularization)
Called "Lasso Regularization" in linear models and "L1" in logistic regressions and other contexts.

Another loss function to punish model complexity in the model. This uses a simple *absolute value*, which results in a non-continuous derivative due to the use of $\mathrm{sign}$.
$$
L_{\mathrm{Lasso}} = \frac{1}{n} \sum_{i=1}^{n}(y_{i}-\hat{y}_{i})^{2} + \lambda \sum_{j}|W_{i}|
$$
##### Gradient
$$
\frac{\partial L}{\partial W} = \frac{-2}{n} \sum_{i=1}^{n} x_{i}(y_{i} - \hat{y}_{i}) + \sum_{j} \lambda\ \mathrm{sign}(w_{j})
$$


---
#machine-learning