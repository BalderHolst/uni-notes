# Convergence of Random Variables
See [[lecture8.pdf|slides]].

Let $X_{1}, X_{2}, \dots$ be a *sequence* of random variables and $X$ be another random variable.

### Types of Convergence

1. $X_n$ converges to $X$ in **propability**, written $X_{n} \xrightarrow{P} X$, if every $\epsilon > 0$
$$
\mathbb{P}(|X_{n} - X| > \epsilon) \to 0
$$
as $n \to \infty$

2. $X_{n}$ converges to $X$ in **distribution**, written $X_{n} \rightsquigarrow X$, if
$$
\lim_{n\to\infty} F_{n}(t) = F(t)
$$
at all $t$ for which $F$ is continuous

$F_{n}$: The CDF of $X_n$
$F$: The CDF of $X$

3. $X_{n}$ converges to $X$ in **quadratic mean** (aka. $L_{2}$), written $X_{n} \xrightarrow{\mathrm{qm}} X$, if 
$$
\mathbb{E}(X_{n} - X^{2}) \to 0, \quad \text{as}\; n \to \infty
$$

### Convergence Implications
See [[lecture8.pdf#page=14|slide]].

![[Convergence-of-Random-Variables-Convergence-Implications.png|center|550]]

$$
\begin{align}
X_{n} \xrightarrow{\mathrm{qm}} X \quad&\Rightarrow\quad X_{n} \xrightarrow{\mathrm{P}} X \\
X_{n} \xrightarrow{\mathrm{P}} X \quad&\Rightarrow\quad  X_{n} \rightsquigarrow X
\end{align}
$$
And if $X_{n} \rightsquigarrow X$ and $\mathbb{P}(X=c)=1$ where $c \in \mathbb{R}$, then $X_{n} \xrightarrow{\mathrm{P}} X$.

#### With Multiple Variables
![[Convergence-of-Random-Variables-With-Multiple-Variables.png|center|600]]

---
#statistics