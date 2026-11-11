---
created: 2026-11-11
tags:
  - statistics
slides:
  - "[[Lessons/Semester 7/statistics/Lektion 10 slides.pdf]]"
  - "[[Agenda MULTISTAT lecture 10.pdf]]"
  - "[[Two-population classification Training data, New data, Procedures.pdf]]"
---

# Classification - 2 populations
We have two populations: $\Pi_{1}$ and $\Pi_{2}$.

Observations are of dimension $p$:
$$
x_{0} \in \mathbb{R}^{p}
$$

Decision rule
$$
\mathbb{R}^{p} = R_{1} \cup R_{2}, R_{1} \disjoint R_{2} = Ø
$$
Decision region
$$
d(x_{0}) =
\begin{cases}
d_{1},\ x_{0} \in R_{1} \\
d_{2},\ x_{0} \in R_{2}
\end{cases}
$$
This is a **hard decision**, because we are *always* giving a point a class.

We can then create a confusion matrix as

|         | $d_1$                      | $d_2$                      |
| ------- | -------------------------- | -------------------------- |
| $\Pi_1$ | $\mathbf{P}(d_1 \| \Pi_1)$ | $\mathbf{P}(d_2 \| \Pi_1)$ |
| $\Pi_2$ | $\mathbf{P}(d_1 \| \Pi_2)$ | $\mathbf{P}(d_2 \| \Pi_2)$ |

and a cost matrix that defines the cost of making the wrong predictions

|         | $d_1$             | $d_2$             |
| ------- | ----------------- | ----------------- |
| $\Pi_1$ | $0$               | $C(d_2 \| \Pi_1)$ |
| $\Pi_2$ | $C(d_1 \| \Pi_2)$ | $0$               |

$C$: Cost of an outcome

And priors
$$
\begin{align}
p_{1} &= \mathbf{P}(\Pi_{1}) \\
p_{2} &= \mathbf{P}(\Pi_{2}) \\
p_{1} + p_{2} &= 1
\end{align}
$$

Flat prior: $p_{1} = p_{2} = \frac{1}{2}$.

#### ECM - Expected Cost of Misclassification
This is the metric we want to minimize.

$$
\mathrm{ECM} =
p_{1}\ \mathbf{P}(d_{2} | \Pi_{1})\ C(d_{2} | \Pi_{1})
+
p_{2}\ \mathbf{P}(d_{1} | \Pi_{2})\ C(d_{1} | \Pi_{2})
$$
NOTE: We don't need the cases there predictions are correct, as the have no cost.

Now we try to minimize this cost: put in the error propabilities $\mathbf{P(d_{i}|\Pi_{k})}$:
$$
\Rightarrow
\frac{f_{1}(x_{0})}{f_{2}(x_{0})} \underset{d_2}{\overset{d_{1}}{\gtrless}} \frac{p_{2}}{p_{1}} \underbrace{\frac{C(d_{1}|\Pi_{2})}{C(d_{2}|\Pi_{1})}}_\mathrm{Cost\ Fraction}
$$

If the costs are equal, the cost fraction is removed.
If priors are also unknown or equal the whole right side will be $1$.
$$
\Rightarrow
\frac{f_{1}(x_{0})}{f_{2}(x_{0})} \underset{d_2}{\overset{d_{1}}{\gtrless}} 1
$$
This corresponds to a [[Maximum Likelihood Estimation (MLE)|maximum likelihood estimate]].

##### MAP - Maximum Aposteriori Propability
Apostieriori: After i make an observation

We use [[Bayes Theorem|Bayes rule]]:
$$
\begin{align}
\mathbf{P}(\Pi_{1}|x_{0}) &= \frac{f_{1}(x_{0}) p_{1}}{\mathbf{P}(x_{0})} \\
\mathbf{P}(\Pi_{2}|x_{0}) &= \frac{f_{2}(x_{0}) p_{2}}{\mathbf{P}(x_{0})}
\end{align}
$$
And
$$
\mathbf{P}(\Pi_{1} | x_{0}) + \mathbf{P}(\Pi_{2} | x_{0}) = 1
$$
$$
\Rightarrow
\begin{cases}
\mathbf{P}(\Pi_{1} | x_{0}) &= \frac{p_{1}f_{1}(x_{0})}{p_{1} f_{1}(x_{0}) + p_{2}f_{2}(x_{0})} \\
\mathbf{P}(\Pi_{2} | x_{0}) &= \frac{p_{2}f_{2}(x_{0})}{p_{1} f_{1}(x_{0}) + p_{2}f_{2}(x_{0})} \\
\end{cases}
$$
And then the MAP is
$$
\mathbf{P}(\Pi_{1} | x_{0})
\underset{d_2}{\overset{d_{1}}{\gtrless}}
\mathbf{P}(\Pi_{2} | x_{0})

\quad
\Leftrightarrow
\quad

p_{1}f_{1}(x_{0})
\underset{d_2}{\overset{d_{1}}{\gtrless}}
p_{2}f_{2}(x_{0})
$$

### Classification with Normally Distributed Classes

Assumption
$$
\mathbf{P}(X | \Pi_{i}) \sim \mathcal{N}_{p}(\mu_{i}, \Sigma_{i}),\quad i = 1, 2
$$
Which gives us pdfs
$$
\Rightarrow f_{i}(x_{0}) = (2\pi)^{\frac{-p}{2}} |\Sigma_{i}|^{-\frac{1}{2}} e^{-\frac{1}{2}(x_{0} - \mu_{i})^{T} \Sigma_{i}^{-1}(x_{0} - \mu_{i})}, i = 1, 2
$$
