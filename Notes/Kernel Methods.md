---
created: 2026-10-22
tags:
  - machine-learning
---
# Kernel Methods
A way of measureing similarity between points.

$$
K(x, z) = \phi(x) \bullet \phi(z)
$$
$x, z$: Points
$\phi$: Kernel function


The kernel function lifts our point into a higher dimension (very spiritual!).

The higher our the dimensions of our dataset, the more likely it is that our data is linearly seperable.

A kernel *must* be destillable to a dot product.

> [!example] Example - Square Lift
> $$\phi(x) = [x_{1}, x_{2}, x_{1}^{2} + x_{2}^{2}]$$
> This will "lift" the a 2D dataset to 3D, making it possible to seperate a group around $(0, 0)$ and another group around it.
>
> This results in a kernel being
> $$
> \begin{align}
> K(x, z) &= \phi(x)\phi(z) \\
> &= x \bullet z + ||x||^2 ||z||^2 \\
> \end{align}
> $$

### Kernel Matrix
$$
K_\mathrm{matrx} = \Phi \Phi^{T}
$$
This will contain the "similarity" of each point with every other point.

The diagonal will e $1$s, and the [[Notes/Eigen values and vectors|eigen values]] will be positive.

### Practical Kernels

> [!example]- Examples of kernels in classification
> ![[poly_kernel_comparison.png]]

##### Polynomial Kernels

$$
K(x, z) = (x \bullet z + c)^{d}
= \sum_{k=1}^{d}
\begin{pmatrix} {d} \\ k \end{pmatrix}
c^{d-k} (x\bullet z)^{k}
$$
$c$: Constant / bias
$d$: Degree of the kernel

> [!example]- Example - Second Degree
> Constants: $d=1$, $c=1$
> 
> Kernel:
> $$
> K(x, z) = (x \bullet z + 1)^{2}
> $$
> 
> Lifting function:
> $$
> \phi(x) =
> \begin{bmatrix}
> 1 & \sqrt{2} & x_{1} & \sqrt{2} & x_{2} & x_{1}^{2} & x_{2}^{2} & \sqrt{2} x_{2} x_{3}
> \end{bmatrix}
> $$
> This is a way more difficult than simply calculating the kernel.

> [!warning] Restructions
> - Cannot seperate data which is not encompassing the origin
> - Odd degree $d$ kernels cannot encompas data with $c=0$.

##### RBF - Radial Bases Function Kernel
"Universal" - It has infinite dimensions we are lifting into
$$
K(x, z) = e^{-\gamma\ ||x - z||^{2}}
= e^{-\gamma}
\cdot e^{||x||^{2}}
\cdot e^{||z||^{2}}
\cdot \underbracket{e^{2 \gamma xz}}_\mathrm{Taylor\ series}
$$
$\gamma$: Variancy

The $e^{2\gamma xz}$ can be expanded into *any* higher dimension with a taylor series
$$
e^{2 \gamma xz} = \sum_{k=0}^{\infty} \frac{(2 \gamma)^{k}}{k!}(x \cdot z)^{k}
$$

##### Sigmoid Kernel
Not an actual kernel.

$$
K(x, z) = \tanh(\alpha \cdot x^{T} z + c)
$$
There are bounds where it behaves like a kernel.

> [!example]- Example for class seperation
> ![[rbf_gamma_effect.png]]

## Multi-class Dataset

##### OvR - One vs. Rest
Train a classifier that seperates one class from the rest.

##### Ovo - One vs. One
Train a classifier to seperate one class from another.

Bigger mode, but may provide better results.

### Cross Validation
Consider that the validation dataset may not be completely representitive, as it may be quite small.

To midigate some of this, we train multiple times on different "folds" of the data. In each fold, we choose a now split of the training and validation data. The output is found by averaging the output of all the folds. We **do not use the training data**.