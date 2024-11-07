# Expectation
Expected value, or **mean**, or first moment. See [[lecture7.pdf|slides]].

$$
\mathbb{E}(X) = \int x\ dF(x) =
\begin{cases}
\sum_{x} x\, f(x) &\mathrm{if}\ X\ \mathrm{is\ discrete} \\
\int_{x} x\, f(x) &\mathrm{if}\ X\ \mathrm{is\ continuous}
\end{cases}
$$

Assuming the sum (or integral) is well defined. We use the following *notation* to denote the expected value of $X$:

$$
\mathbb{E}(X) =
\mathbb{E}X =
\mu =
\mu_X =
\int x \, dF(x)
$$

#### Properties

Let $X_1, \dots, X_n$ be ***independent*** random variables. Then,

$$
\mathbb{E}\left(
\prod_{i=1}^{n}X_i
\right)
= \prod_i \mathbb{E}(X_i)
$$


---
#statistics
