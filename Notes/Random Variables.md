# Random Variables
See [[Lecture 12 - The KalmanFilter.pdf#page=29|slides]].

Variables that describe a range of outcomes.
$$
X: \Omega \rightarrow \mathbb{R}
$$

>[!example]- Dice Example
>Let $X$ be a random variable describing the outcome of rolling a fair dice. The fair dice is characterized by:
>- It has $6$ different outcomes $\set{1, 2, 3, 4, 5, 6}$.
>- The probability of getting each of the six outcomes is the same, i.e., $\mathrm{Pr}(X = 4) = \frac{1}{6}$
>- The outcome of each roll of the dice is independent.

$f_{X}$ is the propability mass function (pmf) in *discrete* systems.

$\Omega$ is the space containing all outcomes (sample space).
$\mu$ is the average value of outcomes.
$\sigma$ is the standard deviation which describes the spread of outcomes.

>[!tip] Capitalization
>$X$: Random variable
>$x$: Realization/Sample

## Terminomogy
| Symbol            | Term                                            |
| ----------------- | ----------------------------------------------- |
| $\Omega$          | Sample space                                    |
| $\omega$          | Outcome                                         |
| $A$               | Event (subset of $\Omega$)                      |
| $\neg A$ or $A^c$ | Complement (not $A$)                            |
| $A \cup B$        | Union ($A$ or $B$)                              |
| $A\cap B$         | Intersection ($A$ and $B$)                      |
| $A-B$             | Set difference ($\omega$ in $A$ but not in $B$) |
| $A\subset B$      | Set inclusion                                   |
| $\emptyset$       | Null event (always false)                       |
| $\Omega$          | True event (always true)                        |
 
## Discrete Variables

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
This *only applies if $A_{i}$ is a **partition** of $\Omega$.
$$
\sum_{i} A_{i} = 1
$$

---
## Continuous Variables
Probability of a range of outcomes
$$
\mathrm{P}(\set{a \leq X \leq b}) = \int_{a}^{b} f_{X}(x)\;\mathrm{dx} = F_{X}(b) - F_{X}(a)
$$
$f_{X}$: Probability density function (pdf).

$$
F_{X}(x) = P(X \leq x) = \int_{-\infty}^{x}f_X(t)\; \mathrm{dt}
$$
$F_{X}$: Cumulative density function (cdf) for *continuous* systems. Integral of $f_X$. Should equal $1$ as input ($\Omega$) approaches $\infty$.

$$
\lim_{x\to\infty} F_{X}(x)  = 1
$$

#### Expected Value
The *mean* of outcomes
$$
\mathbb{E}(X) 
$$

>[!tip] Useful property
>$X$s do not have to be intependent.
>$$
>\mathbb{E}\left(\sum_{i}a_{i}X_{i} \right) = \sum_{i} a_{i} \mathbb{E}(X_{i})
>$$

If $X_{i}$s are intependent:
$$
\mathbb{E}\left(\prod_{i=1}^{n}X_{i} \right) = \prod_{i} \mathbb{E}(X_{i})
$$

#### Quantile Function
Inverse of the cdf.
$$
F_{X}^{-1} = \inf\left\{ x:\; F_X(x) > q \right\}, \quad q \in [0, 1]
$$
To get the $25\%$ quantile, do $F_{X}^{-1}(25\%)$

#### Variance
$$
\mathrm{Var}(X) = E(X - \mu)^2
$$



---
#statistics
