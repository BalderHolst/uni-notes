# Propability Space
A triple $(\Omega, \mathcal{F}, P)$. See [[lecture2.pdf#page=4|slides]].
$\Omega$: A set of outcomes
$\mathcal{F}$: A set of events
$P$: A function which assigns probabilities to events

### Rules
Rules for probability operations

##### Conditional Probability
> "Probability of $B$ given $A$"

$$
P(B|A) = \frac{P(B \cap A)}{P(A)}
$$

##### Multiplication
$$
P(A \cap B) = P(A)\,P(B|A)
$$

##### Bayes Rule
$$
P(B | A) = \frac{P(B \cap A)}{P(A)} = \frac{P(A|B)P(B)}{P(A)}
$$

### Independence
Outcomes are independent if:

>[!warning]
>Independence is **not intuitive**.

$$
P(A) = P(B|A)
$$

### Distributions
Different distributions have different **probability mass functions**.

##### Bernoulli
> *"Flipping coins"*

$$
X \sim Bernoulli(p)
$$

$$\begin{cases}
P(X = 0) = p \\
P(X = 1) = 1-p
\end{cases}
$$

##### Binomial
$$
X \sim Binomial(p, n) \Rightarrow 
$$
##### Geometric
$$
X \sim Geometric(p)
$$

##### Poisson
$$
X \sim Poison(\lambda),\; \mathrm{where}\; \lambda > 0
$$
$$
P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}
$$

---
### Joint Distribution
Probability of $X$ and $Y$.
$$
P(X, Y)
$$

### Marginalisation
$$
P(X = x) = \sum_{y} P(X=x, Y=y)
$$

When $X$ and $Y$ are independent, this results in [[convolusion]].

---
### Expected Value
> *"Center of mass"* or *"mean value"*

Here $X$ is a *discrete* random varable.
$$
\mathbb{E}h(X) = \sum_{x}h(x)P(X=x)
$$

For $c \in \mathbb{R}$


##### Linearity
$$
\mathbb{E}(X_{1}, \dots, X_{n}) = \mathbb{E}X_{1} + \dots + \mathbb{E}X_{n}
$$

If $X$s are independent
$$
\mathrm{var}(X_{1} + \dots + X_{n}) = \mathrm{var}(X_{1}, \dots, X_n)
$$

## Moment Generating Function
**Defines the distribution** of the random variable.

$$
\begin{align}
\phi x(t) &= \mathbb{E}(e^{tX}) \\
\phi' x(t) &= X \mathbb{E}(e^{tX}) \\
\phi'' x(t) &= X^2 \mathbb{E}(e^{tX}) 
\end{align}
$$
$X$: Random variable

You can find the distribution from the moment generating function like this:
$$
\phi'x(0) = X
$$

---
#intelligent-systems
