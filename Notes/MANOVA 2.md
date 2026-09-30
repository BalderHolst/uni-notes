---
created: 2026-09-30
tags:
  - multivariate-statistics
---
# MANOVA 2
See [[Lessons/Semester 7/statistics/Lektion 5 slides.pdf|slides]].

2: Factors

$$
X_{lkj} \sim N_{p}(\mu_{lk}, \Sigma)
$$
$l$: Factor 1
$k$: Factor 1
$j$: Observation count

$$
\mu_{lk} = \mu + \tau_{l} + \beta_{k} + \gamma_{lk}
$$
$\mu$: Overall
$\tau_{l}$: Factor 1 effect
$\beta_k$: Factor 1 effect
$\gamma_{lk}$: Interaction (non-linearities)

$\gamma_{lk}$ should be small, otherwise it destroys the test.

**Hypothesis**:
$H_{0}$: $\forall \mu_{lk} = \mu \Leftrightarrow \forall \tau_{l} = 0\ \land\ \forall \beta_{k} = 0$

#### Sample Means

Overall
$$
\bar{X} = \frac{1}{gbn} \sum_{l} \sum_{k} \sum_{j} X_{lkj}
$$
Populationwise
$$
\bar{X}_{lk} = \frac{1}{n} \sum_{j} X_{lkj}
$$
Columnwise
$$
\bar{X}_{l\bullet} = \frac{1}{bn} \sum_{k}\sum_{l} X_{lkj}
$$
Rowwise
$$
\bar{X}_{\bullet k} = \frac{1}{gn} \sum_{l}\sum_{j} X_{lkj}
$$
