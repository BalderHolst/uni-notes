---
created: 2026-10-22
tags:
  - machine-learning
---
# Kernel Methods
A way of measureing similarity between points.

$$
K(x, z) = \phi(x) \cdot \phi(z)
$$
$x, z$: Points
$\phi$: Kernel function

The kernel function lifts our point into a higher dimension (very spiritual!).

The higher our the dimensions of our dataset, the more likely it is that our data is linearly seperable.


> [!example]- Example - Square Lift
> $$\phi(x) = [x_{1}, x_{2}, x_{1}^{2} + x_{2}^{2}]$$
> This will "lift" the a 2D dataset to 3D, making it possible to seperate a group around $(0, 0)$ and another group around it.
>
> This results in a kernel being
> $$
> K(x, z) = \phi(x)\phi(z) =
> x \bullet z + ||x||^2 ||z||^2
> $$
