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

#### Friedman Test
Paired data. We have several *test objects*. These could be different algorithms run the same data, we are testing if there is a difference on their outputs.

We use the **same test object for different populations**.

Requires that the test objects can be run on the same populations.

$H_{0}$: $\forall m_{i} \overset{?}{=} m$

Rank of a test object is found for each row of populations.

The average rang in each column in the rank matrix should be approximately the same to confirm the null hypothesis. 

#### Contingency Table Test
*Categorical data*: Factor combinations with **counts**.

$O(i, j)$: Number of observations for each combination of factors (categories) $A_{i}$ and $B_{i}$.

$H_{0}$: Factors $A$ and $B$ are **independent**.

We calculate the *expected counts* $E(i, j)$.

**Test Statistic**
$$
T= 
\sum_{i=1}^{r}
\sum_{j=1}^{c}
\frac{
[O(i,j) - E(i,j)]^{2}
}{
E(i,j)
}\sim
\chi^{2}_{(r-1)(c-1)}
$$

**P-value**
$$
\mathbf{P}\big[ \chi^{2}_{(r-1)(c-1)} > T \big]
$$

#### One Sample Kolmogorov-Smirnoff Test
We calculate the sample CDF from data and plot it. We should have **resonably many datapoints** for this test. Otherwise, the sample CDF will be hard to use.

$$
\hat{F}(x) = \frac{\mathrm{\#obs \leq x}}{n} = \frac{1}{n} \sum_{i=1}^{n} 1_{x_{i} \leq x}
\quad \mathrm{where}\quad
1_{x_{i} \leq x} =
\begin{cases}
1 & x_{i} \leq x \\
0 & x_{i} > x \\
\end{cases}
$$

**Test Statistic**
We find the maximum vertical distance between the sample CDF and actual CDF.
$$
D = \underset{x}{\mathrm{max}} | \hat{F}(x) - F(x) |
$$

**Critical Value**
$$
c(\alpha) = \sqrt{\frac{-\frac{1}{2} \log \frac{\alpha}{2}}{n}}
$$
If we set $\alpha = 0.02$ then $c(\alpha) \approxeq 1.36\sqrt{n}$.

#### Two Sample Kolmogorov-Smirnoff Test
Same as  One Sample Kolmogorov-Smirnoff Test, but here we compare *two* sample CDF, to test if they are from the samme distribution.


#### Goodness Of Fit Test (Pearson’s Chi-Squared test)
The likelihood that a population belongs to a specific **type of distribution**.

We claim a distribution type, estimate its parameters and evaluate to "goodness" of the fit.
