# Asymptotic Relative Efficiency
Compare sample efficiency between parameter estimators.

Let $U_{n}$ and $T_{n}$ be estimators of some parameter where
$$
U_{n} \rightsquigarrow \mathcal{N}\left(\theta, \frac{u^{2}}{n}\right),
\quad
T_{n} \rightsquigarrow \mathcal{N}\left(\theta, \frac{t^{2}}{n}\right)
$$
then
$$
\mathrm{ARE}(U_{n}, T_{n}) = \frac{t^{2}}{u^{2}}
$$

##### Example
$$
\mathrm{ARE}(\mathrm{Median}, \mathrm{MLE}) = 0.63
$$
Median estimator has a sample efficiency of $63\%$ compared with [[Maximum Likelihood Estimation (MLE)|MLE]]; Using [[Maximum Likelihood Estimation (MLE)|MLE]] you need $63\%$ of the samples compared to median estimator, to get the same variance for the estimated parameter.



---
#statistics