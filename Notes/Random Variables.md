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

$\Omega$ is the space containing all outcomes.
$\mu$ is the average value of outcomes.
$\sigma$ is the standard deviation which describes the spread of outcomes.

>[!tip] Capitalization
>$X$: Random variable
>$x$: Realization/Sample

### Independence

Variable $A$ and $B$ are independent, if one's outcome does not affect the other.

$A$ and $B$ are independent if
$$
P(AB) = P(A)P(B)
\Rightarrow A \, {\perp\!\!\!\perp} \, B
$$
A set of *events* $\set{A_{i}: i\in I}$ is independent if
$$
P\left( \bigcap_{i \in J} A_{i} \right) = \prod_{i \in J} P(A_i)
$$
For any finite subset $J$ of $I$. This means that
$$
P(A, B, C) = P(A)P(B)P(C)
$$
If $A$, $B$ and $C$ are independent.

If $A$ and $B$ are *not independent*  we write

$$
A\;\not\!\perp\!\!\!\perp B
$$

>[!warning]
> Disjoint event is not an independent event
>$$\underbrace{P(A, B) = 0}_{\mathrm{disjoint}} \;\;\not\Rightarrow\;\; \mathrm{Independent}$$

### Conditional
Calculate probabilities an outcome given other outcomes.

The propability of $A$ given $B$ is denoted as
$$
P(A|B)
$$

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

>[!warning] Order Matters!!
>$$P(A|B) \not= P(B|A)$$

##### Law of Total Probability
The propability of a variable can be found by *summing* over all possibilities of the variables it depends on.
$$
P(B) = \sum_{i=1}^{k}P(B|A_{i})P(A_{i})
$$

---

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
