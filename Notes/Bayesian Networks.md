# Bayesian Networks
A mix of graph theory and probability theory. See [[lecture3a.pdf#page=3|slides]].

Represents relations between dependent and independent random events as a graph.

Each node represents a [[Random Variables|random variable]], and has a conditional probability distribution given its parents.
$$
P(X_{i}|\mathrm{parrents}(X_{i}))
$$

>[!video]- Bayesian Networks Lesson
>![](https://www.youtube.com/watch?v=TuGDMj43ehw)

>[!tip] Markov Blanket
>Each node is *conditionally independent* from nodes outside of
>- Parents
>- Childen
>- Co-parents

>[!warning]
>**Order of variables matters** when constructing a Baysian network.
>
>See [[lecture3a.pdf#page=8|example]].

#### Full Joint Distribution
The formula for calculating joint distribution at all nodes in the system.

$$
P(x_{1}, \dots, x_{n}) = \prod_{i=1}^{n}P(x_{i}|\mathrm{parrents}(x_{i}))
$$

#### Single Joint Probability
An example of getting the probability of $r$ given $s$ in a Bayesian network with variables $R$, $W$, $S$ and $C$.
$$
P(r|s) = \sum_{w}\sum_{c}\frac{P(r, w, s, c)}{P(s)}
$$

#### Chain Rule
$$
P(x_{1}, \dots, x_{n})= \prod_{i=1}^{n}P(x_{i}|x_{i}-1,\dots,x_{1})
$$

#### Noisy OR Model
Assign the probability for a `true` parent to cause the child to be true. See [[lecture3a.pdf#page=11|slides]].

**Assumptions**
- We have listed all cause
- Parents are independent of each other

$$
P(x_{i}|\mathrm{parents}(x_{i})) = 1-\prod_{\{j:\;x_{j}=true\}} = q_{j}
$$


---

>[!example]- Burglar Alarm Example
>![[lecture3a.pdf#page=4]]

---
#intelligent-systems 
