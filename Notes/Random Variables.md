# Random Variables
See [[Lecture 12 - The KalmanFilter.pdf#page=29|slides]].

Variables that describe a range of outcomes.

>[!example]- Dice Example
>Let $X$ be a random variable describing the outcome of rolling a fair dice. The fair dice is characterized by:
>- It has $6$ different outcomes $\set{1, 2, 3, 4, 5, 6}$.
>- The probability of getting each of the six outcomes is the same, i.e., $\mathrm{Pr}(X = 4) = \frac{1}{6}$
>- The outcome of each roll of the dice is independent.

$p_{X}$ is the propability mass function in *discrete* systems.

$f_{X}$: The probability density function for *continuous* systems. It outputs the propability of a certain outcome.

$\mu$ is the average value of outcomes.
$\sigma$ is the standard deviation which describes the spread of outcomes.

>[!tip] Capitalization
>$X$: Random variable
>$x$: Realization/Sample

##### Identities
Probability of $a$ *given* $b$
$$
P(a|b) = \frac{P(a, b)}{P(b)}
$$
Probability of $a$ *and* $b$
$$
P(a, b) = P(a|b)P(b)
$$
Bayes formula (flip the order of given variable)
$$
P(b|a) = P(a|b) \cdot \frac{P(b)}{P(a)}
$$

##### Probability
Probability of a range of outcomes (continuous)
$$
\mathrm{Pr}(\set{a \leq X \leq b}) = \int_{a}^{b} f_{X}(x)\;\mathrm{dx}
$$
$f_{X}$: Probability density function

##### Variance
$$
\mathrm{Var}(X) = E[(X - \mu)^2]
$$


---
#statistics
