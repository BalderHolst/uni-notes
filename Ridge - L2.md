# Ridge / L2
Loss function where the number of paremeters in the model and their magnitude are punished.

$$
L_{\mathrm{Ridge}} = \frac{1}{n} \sum_{i=1}^{n} (y - \hat{y})^{2} + \lambda \sum^{W}_{j=1} W_{j}^{2}
$$
$\lambda$: How much to punish complexity. Tunable hyperparameter (use validation data for this).
$W$: Weights.
$n$: Number of samples
$y$: Actual sample values
$\hat{y}$: Predicted (by current model) sample values