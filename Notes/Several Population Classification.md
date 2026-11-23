---
created: 2026-11-18
tags:
  - multivariate-statistics
slides:
  - "[[Lecture Material/Semester 7/statistics/Lektion 11 slides.pdf]]"
  - "[[Lecture Material/Semester 7/statistics/Several-populations classification model.pdf]]"
---

# Several Population Classification
[[Two Popolation Classification|Two Popolation Classification]] with more than two classes.

##### Problem definition
Much the same as [[Two Popolation Classification]], but with $g \geq 2$.

![[Lecture Material/Semester 7/statistics/Lektion 11 slides.pdf#page=3|Lektion 11 slides]]


##### General Classificaiton Criteria
Also the same as [[Two Popolation Classification]], but now we need to sum over *all combinations* of misclassification to get the total ESM (Expected Cost of Misclassification).

![[Lecture Material/Semester 7/statistics/Lektion 11 slides.pdf#page=5|Lektion 11 slides]]

$f_{i}(x)$: *general* PDF of the $i$'th variable.

##### Training
Training the model amounts to estimating the PDFs of the populations.

##### MVN Assumption
We assume that the population are [[Notes/Multivariate Normal Distribution (MVN)|MVN]] distributed.

$$
X | \pi_{i} \sim N_{p}(\mu_{i}, \Sigma_{i})
$$

![[Lecture Material/Semester 7/statistics/Lektion 11 slides.pdf#page=6|Lektion 11 slides]]

$D$: [[Mahalanobis Distance]]


##### Soft Decisions
Calculate *posterior* (after new observation) propabilities

$$
P(\pi_{k} | x_{0}) = 
\frac{
p_{k} f_{k}(x_{0})
}{
P(x_{0})
}
,\quad
k = 1, \dots, g
$$
with
$$
P(x_{0}) = \sum_{i=1}^{g} p_{i}f_{i}(x_{0})
$$
The sum of these propabilities should be $1$.

**MAP (Maximum Aposteriori Prob.)**: We choose $d_{k}$ (predicted class) to maximize $P(\pi_{k} | x_{0})$

We classify only if one of the propabilites are close to $1$.
$$
\begin{cases}
d_{*}, &\quad P(\pi_{*} | x_{0}) \approx 1 \\
\mathrm{no\ class}, &\quad \mathrm{otherwise}
\end{cases}
$$



