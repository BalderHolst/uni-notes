# Direct Samling
Generate samples from [[Bayesian Networks]].

Let $S_{PS}$ be the probability that a specific event is generated. Then:

$$
S_{PS}(x_{1}, \dots, x_{n}) = \prod_{i=1}^{n} P(x_{i}|\mathrm{Parents}(X_{i})) = P(x_{1}, \dots, x_{n})
$$

Let $N_{PS}(x_{1}, \dots, x_{n})$ be the number of times the event $x_{1},\dots,x_{n}$ occurs. The, by the law of large numbers we have:
$$
\lim_{N \to \infty} \frac{1}{N} N_{PS}(x_{1},\dots, x_{n}) = S_{PS}(x_{1},\dots,x_{n})=P(x_{1},\dots,x_{n})
$$

With enough samples the estimate approaches the true distribution.


---
#intelligent-systems