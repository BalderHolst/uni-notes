# The Bootstrap
Estimate the underlying distribution of a sampled distribution, but with only a single (usually limited) dataset.

Say the original dataset has $n$ samples. Create new datasets by sampling $n$ samples from the original dataset **with replacement**. These new datasets are called *bootstrapped dataset*.

#### Steps
1. Make a bootstrapped dataset
2. Calculate a parameter of the dataset (mean, median or something else)
3. Save the parameter for later
4. Repeat previous steps many times

The resulting distribution tells *how the paramenter may change if we redid the experiment*. This could also be used to generate a confidence interval.

---
#statistics