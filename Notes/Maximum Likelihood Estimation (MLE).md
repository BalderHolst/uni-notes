# Maximum Likelihood Estimation
"Fit" a distribution to data; Choose the distribution that is most likely to have caused the observed samples.

It is the **most optimal** estimator.


## For [[Multivariate Normal Distribution|MVN]]

$$
L(\mu, \Sigma) = \prod_{j=1}^{n} f_{X}(x_{j}|\mu, \Sigma)
$$
We maximise this function to find the correct values of $\mu$ and $\Sigma$.

$$
\vec{\nabla} L = \vec{0} \quad\Rightarrow\quad

\hat{\mu}_{ML} = \bar{X} = \frac{1}{n} \sum_{j=1}^{n}X_{j} \sim N_{p}(\mu, \Sigma/n)
$$
This is an *unbiased* estimator of $\mu$:
$$
E[\hat{\mu}_{ML}] = \mu
$$
Uncertainty decreases with number of samples $n$, it is *consistent*, of the estimate is given by:
$$
\mathrm{Cov}[\hat{\mu}_{ML}] = \frac{\Sigma}{n}
$$

$$
\begin{align}
\hat{\Sigma}_{ML} &= \frac{1}{n} \sum_{j=1}^{n}(x_{j}-\mu)(x_{j} - \mu)^{T} \quad \Rightarrow \quad E[\hat{\Sigma}_{ML}] = \Sigma \quad \mathrm{unbiased!} \\

\hat{\Sigma}_{ML} &= \frac{1}{n} \sum_{j=1}^{n}(x_{j}-\bar{x})(x_{j} - \bar{x})^{T} \quad \Rightarrow \quad E[\hat{\Sigma}_{ML}] = \frac{n-1}{n} \Sigma \quad \mathrm{biased\ (not\ good)}
\end{align}
$$
We usually don't have access to the correct mean, so we use an estimate instead:
$$
\hat{\Sigma}_{ML} = \frac{1}{n} \sum_{j=1}^{n}(x_{j}-\bar{x})(x_{j} - \bar{x})^T
$$
$\bar{x}$: Sample average

We define the sample average $S_{p \times p}$ as follows:
$$
S_{(p\times p)} = \hat{\Sigma} = \frac{n}{n-1} \hat{\Sigma}_{ML} \sim \frac{1}{n-1} W_{p}(\Sigma, n-1)
$$
$W_{p}$: Wishart distribution

$$
E[S] = \Sigma \quad \Rightarrow \quad \mathrm{unbiased :)}
$$

### Calculating
Calculating MLE given samples $X = \set{x_{1}, x_{2}, \dots, x_{n}}$. These are [[IID|iid]] from the same population.

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