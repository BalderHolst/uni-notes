# Bayesian Networks
A mix of graph theory and probability theory. See [[lecture3a.pdf#page=3|slides]].

Represents relations between dependent and independent random events as a graph.

Each node represents a [[Random Variables|random variable]], and has a conditional probability distribution given its parents.
$$
P(X_{i}|\mathrm{parrents}(X_{i}))
$$

>[!w]

#### Full Joint Distribution
The formula for calculating joint distribution at all nodes in the system.
$$
P(x_{1}, \dots, x_{n}) = \prod_{i=i}^{n}P(x_{i}|\mathrm{parrents}(x_{i}))
$$

#### Chain Rule
$$
P(x_{1}, \dots, x_{n})= \prod_{i=1}^{n}P(x_{i}|x_{i}-1,\dots,x_{1})
$$

---

>[!example]- Burglar Alarm Example
>![[lecture3a.pdf#page=4]]

---
#intelligent-systems 