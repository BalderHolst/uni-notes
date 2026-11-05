---
created: 2026-11-05
tags:
  - machine-learning
slides:
---

# Gausian Process

### Prior
All the infromation you are starting with. This could be assumptions could be about the mean $\mu$ and standard deviation $\sigma_{f}^{2}$ of the model functions. **The prior is the set of all function that fit the assumptions**.

### Posterior
What happens when we reevaluate the prior belifs with the data points.

We calculate the updated mean $\mu_{*}$ and standard deviation $\sigma_{*}$.

Only the functions that pass near points "survive".

$$
f \sim \mathbf{BP}(m(x), k(x, x'))
$$
where
$$
k(x_{i}, x_{j}) = \sigma_{f}^{2}\ \underbracket{e^{\frac{-(x_{i} - x_{j})^{2}}{2l^{2}}}}_\mathrm{RBF\ kernel}
$$
This is the covariance kernel we use. Notice that it is an [[Kernel Methods#RBF - Radial Bases Function Kernel|RBF]] kernel with $\gamma = \frac{1}{2l^{2}}$.

This creates two hyperparameters:
$\sigma_{f}^{2}$: Expected variance of the data
$l$: The length of the kerne - (small = jagged functions - big = smooth)

#### Calculating
$$
y_{i} = f(x) + \epsilon_{i}, \quad \epsilon \sim \mathbf{N}(0, \sigma_{n}^{2})
$$
$y_{i}$: Predicted output
$e_{i}$: Noise
$\sigma_{n}^{2}$: How close functions have to pass a point to "survive"

$$
K = K_{xx}
$$
$K$: Covariance matrix between all the training point
$$
(k_{*})_{i} = k(x_{i}, x_{*})
$$
$k_{*}$: Vector of covariances between new data points and training datapoints

$$
K_{**} = \sigma^{2}_{f}
$$
$K_{**}$: Expexted variance

$$
\begin{bmatrix}
y \\ f(x_{*})
\end{bmatrix}
\sim
\mathbb{N} \left(
m(x),
\begin{bmatrix}
K + \sigma_{n}^{2} I & k_{*} \\
k_{*}^{T} & k_{**}
\end{bmatrix}
\right)
$$

#### Closed form Solution

$$
\begin{align}
\mu_{*} &= k_{*}^{T} (K + \sigma_{n}^{2}I)^{-1}y \\
\sigma_{*}^{2} &= k_{**} - k_{*}^{T}(K + \sigma_{n}^{2} I)^{-1}k_{*}
\end{align}
$$
$\mu_{*}$: Posterior mean
$\sigma_{*}^{2}$: Posterior variance

We can calculate part of the $\mu_{*}$ to a set of weights
$$
\alpha = (K + \sigma_{n}^{2}I)^{-1}y \\
$$
Predicted points $y_{*}$ can then be found as
$$
y_{*} = \sum_{i=1}^{n} \alpha_{i} k(x_{*}, x_{i})
$$

> [!warning]
> - Assumptions may change
> - We are doing matrix inversion, which can be heavy with large datasets
> - Points need neighbors - Works better in lower dimensions

