# Central Limit Theorem
See [[lecture8.pdf#page=19|slide]].

The sample mean of ***any*** distribution follows a normal distribution!

Works if
- The distributions are [[IID]]
- Variance is finite

Let $D$ be the distribution of the sum of $n$ number of random variables ($n$ draws from some [[IID]] distribution), normalized so that the *mean is zero* and the *standard deviation is one*.
$$
D = \frac{(X_{1} + \dots + X_{n}) - n \cdot \mu}{\sigma \cdot \sqrt{n}}
$$
$n$: Number of draw from the original distribution
$\mu$: Mean of the $X_{1} + \dots + X_{n}$
$\sigma$: Standard deviation of $X_{1} + \dots + X_{n}$

then
$$
\lim_{n\to\infty} \mathbb{P}(a < D < b) = \underbrace{
\int_{a}^{b} \frac{1}{\sqrt{2\pi}}e^{-x^{2}/2} \mathrm{dx}
}_{\mathrm{Area\ under\ Gaussian}}
$$

>[!video]- 3B1B Video
>![](https://www.youtube.com/watch?v=zeJD6dqJ5lo)


---
#statistics