---
created: 2026-10-08
tags: []
---

# Classification Forrest
We create [[Classification Trees]]. Typically between 100 and 500. Each tree is created using a sub-population of our training data. These sub-populations are created by sampling the training data **with replacement**.

Each tree should split $m$ features pr. branch.
$$
m = \sqrt{k}
$$
$k$: Number of features

To evaluate the forrest, all trees are evaluated and their average output is calculated.



