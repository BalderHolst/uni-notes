# Emperical CDF
A CDF constructed from the samples of a random variable. Each sample $X_i$ has a "mass" of $1/n$.

$$
\widehat{F}_n(x) = \frac{\sum_{i=1}^{n} I(X_{i} \leq x)}{n}
$$
$\widehat{F}_{n}(x)$: Emperical CDF
$n$: Number of samples
$I(X_{i} \leq x)$: $1$ if the inner statement is `true`, otherwise $0$.

>[!example]- Example Plot
>![[Emperical-CDF.png|Pasted image 20241128093128.png]]

---
#statistics