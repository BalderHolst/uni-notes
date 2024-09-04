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

---
#intelligent-systems
