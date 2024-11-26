# Convergence of Random Variables
See [[lecture8.pdf|slides]].

Let $X_{1}, X_{2}, \dots$ be a *sequence* of random variables and $X$ be another random variable.

There are multiple ways do define RV convergence:

1. $X_n$ converges to $X$ in **propability**, written $X_{n} \xrightarrow{P} X$, if every $\epsilon > 0$
$$
\mathbf{P}(|X_{n} - X| > \epsilon) \to 0
$$
as $n \to \infty$

2. $X_{n}$ converges to $X$ in **distribution**, written $X_{n} \rightsquigarrow X$, if
$$
\lim_{n\to\infty} F_{n}(t) = F(t)
$$
at all $t$ for which $F$ is continuous

$F_{n}$: The CDF of $X_n$
$F$: The CDF of $X$

3. 

---
#statistics