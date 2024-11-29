# Binomial Distribution
Models the probability of a binary outcome. Flipping a fair coin $50$ times would follow the distribution $B(50, 0.5)$.
$$
X \sim B(n, p)
$$
$n$: Number of samples
$p$: Probability


#### PDF
$$
f(k, n, p) = \mathrm{Pr}(X = k) =
\frac{n!}{k!(n-k)!}
p^{k} (1-p)^{n-k},
\quad k \in \set{0, 1, 2, \dots, n}
$$
$k$: An outcome


---
#statistics #distribution