---
created: 2026-10-28
tags:
  - multivariate-statistics
slides:
  - "[[Lessons/Semester 7/statistics/Lektion 7 slides.pdf]]"
---

# Multivariate Multiple Linear Regression

Where the [[Univariate Multivariate Linear Regression (UMLR)|UMLR]] fits a linear hyprplane to a multidimensional observation set, the MMLR fits **multiple hyprplanes** to multidimensional data. Here, we have ***several output / response variables*** and we do a linear regression on each.

### Model
$$

\underbracket{
\begin{bmatrix}
Y_{11} & Y_{12} & \cdots & Y_{1m} \\
Y_{21} & Y_{22} & \cdots & Y_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
Y_{n1} & Y_{n2} & \cdots & Y_{nm} \\ 
\end{bmatrix}
}_{Y}

=

\underbracket{
\begin{bmatrix}
1 & z_{11} & z_{12} & \cdots & z_{1r} \\
1 & z_{21} & z_{22} & \cdots & z_{2r} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & z_{n1} & z_{n2} & \cdots & z_{nr} \\
\end{bmatrix}
}_{Z}

\underbracket{
\begin{bmatrix}
\beta_{01} & \beta_{02} & \cdots & \beta_{0m} \\
\beta_{11} & \beta_{12} & \cdots & \beta_{1m} \\
\vdots & \vdots & \ddots & \vdots \\
\beta_{r1} & \beta_{r2} & \cdots & \beta_{rm} \\
\end{bmatrix}
}_{\beta}

+

\underbracket{
\begin{bmatrix}
\epsilon_{11} & \epsilon_{12} & \cdots & \epsilon_{1r} \\
\epsilon_{21} & \epsilon_{22} & \cdots & \epsilon_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
\epsilon_{n1} & \epsilon_{n2} & \cdots & \epsilon_{nr} \\
\end{bmatrix}
}_{\epsilon}

$$
$n$: Number of observations
$m$: Number of dimensions for each observation
$r$: Number of variables

> [!example]- Slide
>![[Lessons/Semester 7/statistics/Lektion 7 slides.pdf#page=2|Lektion 7 slides]]

### Estimates
$$
\hat{\beta} = (Z^{T}Z)^{-1}Z^{T} Y
$$
**Projections**
$$
\hat{Y} = Z \cdot \hat{\beta} = \underbrace{Z(Z^{T}Z)^{-1}Z^{T}}_{H}Y
$$
$H$: Projection matrix

**Residuals**
$$
\hat{\epsilon} = Y - \hat{Y}
$$
**Covariance**
$$
\hat{\Sigma} = \frac{\text{"SSE"}}{\mathrm{df}} =
\frac{\hat{\epsilon}^{T}\hat{\epsilon}}{\mathrm{df}}
=
\frac{\hat{\epsilon}^{T}\hat{\epsilon}}{n-(r+1)}
$$


### Informal Model Fit Measure

Informal because we are using determinants to get at scalar. This is strictly not equal to what we did in the [[Univariate Multivariate Linear Regression (UMLR)#Model Fit|UMSR]].
$$
R^{2} = 1 - \frac{|\mathrm{SSE}|}{|\mathrm{SST}|}
$$