---
created: 2026-10-07
tags:
  - multivariate-statistics
slides:
  - "[[Lessons/Semester 7/statistics/Lektion 9 slides.pdf]]"
  - "[[Non-parametric hypothesis tests.pdf]]"
---

# Non-parametric Hypothesis Test

Less powerful than [[Notes/Hypothesis Testing|parametric hypothesis testing]].


Medians are better than means!

#### Sign Test

> "Very crude test"
> \- Claus

Parametric Equivalent: Student T-test

We test for the *median*.

$H_{0}$: $m \overset{?}{=} m_{0}$

We count how many are above and below.

$$
\mathrm{sign}(x_{i} - m_{0}) \rightarrow + \; \mathrm{or} \; -
$$

#### Signed Rank Test
Same as sign test, but we introduce *rank*.


**Rank** ($R_{x_i}$)
Create a *sorted list*, where samples are sorted with the key $|x_{i} - m_{0} |$. The rank of a sample is its **index** into this list

**Test statistic**
$$
W = \sum_{i=1}^{n_{r}} \mathrm{sign}(x_{i} - m_{0})\ R_{x_{i}}
$$
This would be $0$ if the proposed median $m_{0}$ is the median of the dataset.


#### Mann Whitney Test / Rank Sum Test
Test if the difference in median between two populations is significant.

$H_{0}$: $m_{x} \overset{?}{=} m_{y}$

$$
S(x, y) =
\begin{cases}
1 &x > y \\
1 / 2 &x = y \\
0 &x < y
\end{cases}
$$

**Test Statistic**
$$
U = 
\sum_{i=1}^{n_{x}}
\sum_{j=1}^{n_{y}}
S(x_{i}, y_{j})
$$

#### Kruskall Wallis Test
Test if the medians of several populations could be the same.

$H_{0}$: $\forall m_{i} \overset{?}{=} m$

We use ranks as they are less vulnerable to outliers.


Rank $r_{ij}$ is gathered by sorting all observations from all populations in increasing order. Their rank is the index of this list.

$$
\set{x_{ij}} \rightarrow \set{r_{ij}} \in \set{1, 2, \dots, N = \sum_{i=1}^{g} n_{i}}
$$
$x_{ij}$: Observations
$r_{ij}$: Ranks among all observations
$n$: Number of observations in each population
$N$: The total number of observations in all populations

For each population we can calculate all the ranks. We expect them to be equally distributed in all populations to accept the hypothesis.

**Test Statistic**
$$
H = (N-1)
\frac{
\sum_{i=1}^{g} n_{i} (\bar{r}_{i} - \bar{r})^{2}
}
{
\sum_{i=1}^{g}
\sum_{j=1}^{g}
(\bar{r}_{ij} - \bar{r})^{2}
}
\sim
\chi^{2}_{g-1}
$$
$\bar{r}_{i} = \sum_{j=1}^{g}r_{ij} / n_{i}$ : Average rank of all observations in population $i$.
$\bar{r} = (N + 1) / 2$: Average rang of all observations.