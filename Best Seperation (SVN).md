---
created: 2026-10-29
tags:
  - machine-learning
---

# Best Seperation (SVN)

We want to maximize the distance between class seperation line and the classified datapoints.

The boundry exists where
$$
W \cdot x + b = y = 0
$$
We want to maximise the margin so that
$$
y_{i}(Wx_{i} + b) \geq \gamma, \quad i=1, \dots,n
$$
$\gamma$: Margin

We define $||W'||$:
$$
\begin{align}
||W'|| = \frac{1}{\gamma} ||W|| \\
\Rightarrow \quad \gamma = \frac{1}{||W'||} \\
\end{align}
$$
Which means we want to minimize $||W'||$ to maximize $\gamma$.

To get a nice landscape for gradient decent, we really minimize the following:
$$
\min \left[\frac{1}{2}||W'||^{2}\right]
$$
**Lagrangian**
We define a lagrangian like so
$$
L(W, b, \alpha) = f(W, b) - \alpha (g(W, b) - c), \quad \mathrm{where}\ g(W, b) = c
$$
Which results in
$$
\begin{align}
L(W', b, \alpha) &= \frac{1}{2} ||W'||^{2} - \sum_{i=1}^{u} \alpha_{i} [y_{i} (W'x_{i}+b) - 1] \\
W' &= \sum_{i=1}^{u}\alpha_{i}y_{i}x_{i}
\end{align}
$$
Which leads to
$$
\begin{align}
L(W', b, \alpha) &= \sum \alpha_{i} - \frac{1}{2} \sum_{i=1}^{u}\sum_{j=1}^{u} \alpha_{i}\alpha_{j} y_{i}y_{j}(x_{i}, x_{j}) \\
\end{align}
$$
### Classification funciton
$$
f(x) = \sum \alpha_{i}y_{i}K(x_{i}, x) + b, \quad
\mathrm{where}\
\begin{cases}
f(x) \geq 0 \Rightarrow\ \mathrm{class} \ 0 \\
f(x) <    0 \Rightarrow\ \mathrm{class} \ 1
\end{cases}
$$
Most $\alpha$s will be $0$. Only points influencing the boundry position will have non-zero values. Therefore, we don't have to carry the whole dataset, when classifying new points, only the parts of the dataset with non-zero $\alpha$s. These points are called **support vectors**.

If the number of support vectors is large, it could mean that the model is not providing much generalization.