---
created: 2026-10-21
tags:
  - multivariate-statistics
slides:
  - "[[Lessons/Semester 7/statistics/Lektion 6 slides.pdf]]"
  - "[[Linear regression models and terminology.pdf]]"
---

# Univariate Multivariate Linear Regression (UMLR)

$$
Y = \beta_{0} + \beta_{1} z_{1} + \cdots + \beta_{r}z_{r} + \epsilon
$$
$Y$: Measured response
$z_{1}, \dots, z_{r}$: *Known* predictor variables
$\beta_{0}, \dots, \beta_{r}$: *Unknown* regression coefficients
$\epsilon$: Random (unknown) error term

**Assumptions**:
$\mathbb{E}[\epsilon] = 0$: There should be an equal amout of positive and negative errors
$\mathbb{V}[\epsilon] = \sigma^{2}$: The variance in error should be approcimately **constant**.

#### Organize the Dataset

Obs # $j$: $j = 1,\dots, n$ $(Y_{j}, z_{j1}, \dots, z_{jr})$

$$
\begin{bmatrix}
Y_{1} \\ Y_{2} \\ \vdots \\ Y_{n}
\end{bmatrix}
=
\underbracket{
\begin{bmatrix}
1 & z_{11} & z_{12} & \cdots & z_{1r} \\
1 & z_{21} & z_{22} & \cdots & z_{2r} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & z_{n1} & z_{n2} & \cdots & z_{nr} \\
\end{bmatrix}
}_\mathrm{Design\ Matrix\ (n\times (r+1))}

\begin{bmatrix}
\beta_{1} \\
\beta_{2} \\
\vdots \\
\beta_{r} \\
\end{bmatrix}
+
\begin{bmatrix}
\epsilon_{1} \\
\epsilon_{2} \\
\vdots \\
\epsilon_{n} \\
\end{bmatrix}
$$
edNote the collumn of ones. It corresponds to the **intercept term** $\beta_{0}$.

Writing the same using matrix symbols:
$$
Y = Z \cdot \beta + \epsilon
$$
If $Z$ was intertible, it would be easy to solve for $\beta$, but $Z$ is *not square*. Therefore we use the [[pesudu inverse]] of $Z$.

#### Least Square Error
See [[Lessons/Semester 7/statistics/Lektion 6 slides.pdf#page=3|slides]].

The unknowns can be estibamated by minimizing the square error.
$$
\mathrm{SSE} = \sum_{j=1}^{n} \hat{\epsilon}^{2}_{j} = \hat{\epsilon}^T\hat{\epsilon}
$$
The solution will be where the gradient of the error is zero.
$$
\begin{align}
\mathrm{SSH}(\hat{\beta}) &= (Y - z \cdot \hat{\beta})^T (Y - z \cdot \beta) \\
\vec{\nabla} \mathrm{SSE}(\hat{\beta}) &= 0
\end{align}
$$
The solution to this is given as
$$
\hat{\beta} = \underbrace{(z^{T}z)^{-1}z^{T}}_{\mathrm{Pseudoinverse}} Y
$$
This is the hyperplane that make the projections of the points to the plane optimized.
### Projections
Projections of each point onto the plane can be found as

$$
\hat{Y} = Z_{\hat{\beta}} = \underbrace{z(z^{T}z)^{-1} z^{T}}_{H}  Y = H \cdot Y
$$
$H$: Projection matrix

### Bias and Consistensy
This estimator is unbiased
$$
\begin{align}
\mathbf{E}[\hat{\beta}] &= (z^{T}z)^{-1}z^{T} \mathbf{E}(Y) \\
&= (z^{T}z)^{-1}z^{T} z \cdot \beta \\
&= \beta
\end{align}
$$
$$
\mathbf{Cov}[\hat{\beta}] = \sigma^{2}(z^{T}z)^{-1}
$$
It is also consistent because $z^{T}z$ becomes bigger with more samples, and therefore the variance becomes smaller.

##### Variance Estimate
$$
\hat{\sigma}^{2} = \frac{\mathrm{SSE}}{n - (r + 1)}
$$

### Model Fit
$$
R^{2} := \frac{\mathrm{SSR}}{\mathrm{SST}} = 1 - \frac{\mathrm{SSE}}{\mathrm{SST}}, \quad 0 \leq R^{2} \leq 1
$$
$R^{2} \approx 1$: Good fit
$R^{2} \ll 1$: Bad fit

Strictly speaking, always use $R^{2}_\mathrm{adj}$. This adjusts for degrees of freedom and is always less than $R^{2}$.

## Inference on Beta
![[Lessons/Semester 7/statistics/Lektion 6 slides.pdf#page=4|Lektion 6 slides]]

## Model Simplification
Slit up $\beta$:
$$
\beta =
\begin{bmatrix}
\beta_{0} \\
\beta_{1} \\
\vdots \\
\beta_{r} \\
\end{bmatrix}
=
\begin{bmatrix}
\beta(1) \\ \beta(2)
\end{bmatrix}
$$
$\beta(1)$: Important coefficients (size $q+1$)
$\beta(2)$: Not so important coefficients (size $r-q$)

$H_{0}$: $\beta(2) \overset{?}{=} \mathbf{0}$ 

Full model: use whole $\beta$
Reduced model: use only $\beta(1)$

$$
\begin{align}
\underbracket{\mathrm{SST}}_{\mathrm{fixed}} = \sum_{j=1}^{n} (Y_{j} - \bar{Y})^{2} &= \mathrm{SSE(\beta)} + \mathrm{SSR}(\beta) \\
&= \mathrm{SSE(\beta(1))} + \mathrm{SSR}(\beta(1))
\end{align}
$$
**NOTE**: To find $\mathrm{SSE}(\beta(1))$ and  $\mathrm{SSR}(\beta(1))$, make a *seperate* optimization.

How much is better is our fit with the full model?
$$
\begin{align}
\mathrm{ESS}(\beta(1) \to \beta) &= \mathrm{SSR}(\beta) - \mathrm{SSR}(\beta(1))\\
&= \mathrm{SSE}(\beta) - \mathrm{SSE}(\beta(1))
\end{align}
$$

**Test statistic**
$$
\mathrm{TS} = \frac{\mathrm{ESS(\beta(1) \to \beta)}}{n - q} \cdot \hat{\sigma}^{2} \sim F(r-q, n - (r+1))
$$

$$
\begin{align}
\mathrm{TS} \leq F(r-q, n - (r+1)) &\Rightarrow \mathrm{Accept}\ H_{0} \\
&\Rightarrow \mathrm{remove}\ \beta(2)\ \mathrm{and\ corresponding}\ z\mathrm{'s}
\end{align}
$$

