# Maximum Likelihood Estimation
"Fit" a distribution to data; Choose the distribution that is most likely to have caused the observed samples.

It is the **most optimal** estimator.

### Calculating
Calculating MLE given samples $X = \set{X_{1}, X_{2}, \dots, X_{n}}$.

1. Calculate the *likelihood* function.
$$L(\theta | x) = \prod_{i=1}^{n} f(\theta, x_{i})$$
$\theta$: Parameter we are estimating (the same for all samples)
$x$: The given data (usually a list of samples)
2. Calculate the *log-likelihood* function.
$$\ell(\theta | x) = \log \left(\prod_{i=1}^{n} f(\theta, x_{i})\right) = \sum_{i=1}^{n} \log(f(\theta, x_{i}))$$
*Make sure to use the properties of logarithms to make as many small terms as possible.* This makes the derivative easier to find.

3. Get the derivative ([[Score Function]])
$$
\ell'(\theta | x) =  \sum_{i=1}^{n} \frac{\mathrm{d}}{\mathrm{d\theta}} \log(f(\theta, x_{i}))
$$
4. Find maximum.
$$
\ell'(\theta | x) = 0
$$
Solve this equation for $\theta$. This is your MLE estimater $\hat{\theta}$.

---

>[!video]- Videos
>![](https://www.youtube.com/watch?v=XepXtl9YKwc)
>![](https://www.youtube.com/watch?v=66FqSpf1trA)

---

>[!video]- MLE for Exponential Distribution
>![](https://www.youtube.com/watch?v=p3T-_LMrvBc)

>[!video]- MLE for Binomial Distribution
>![](https://www.youtube.com/watch?v=4KKV9yZCoM4)

---
#statistics 