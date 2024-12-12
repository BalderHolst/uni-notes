# Hypothesis Testing
Test if an alternative hypothesis is worth accepting or rejecting as opposed to the currently accepted hypothesis.

$H_{0}$: Null hypothesis; currently accepted hypothesis
$H_{a}$: Alternative hypothesis

#### Tests
- [[Wald Test]]
- [[Log-likelihood Test]]
- [[Score Test]]

#### Error Types

**Type I Error ($\alpha$)**
Rejecting the null hypothesis ($H_0$) when it is actually true. Represents a "false positive".

**Type II Error ($\beta$)**
Failing to reject the null hypothesis ($H_0$) when it is actually false. Represents a "false negative."

$$
\beta =
\begin{cases}
\mathbf{P}(Z \leq p_\mathrm{upper}) - \mathbf{P}(Z \leq p_\mathrm{lower}) \\
\mathbf{P}(Z \leq p)
\end{cases}
$$
$Z$: [[Z-distribution|Z distributed]] random variable
$p$: [[P-value]]. One or two depending on the type of test (single/double sided)


---
#statistics