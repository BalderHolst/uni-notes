# Fisher Information
A measure for how much information each sample contains. Also the *variance of the score function*.

### Single Parameter Estmation

For a *single parameter* $\lambda$:
$$
\mathcal{I}_{n}(\lambda)
= \sum_{i=1}^{n}\mathbb{V}_{\lambda}\big( S_{n}(\lambda) \big)
= - \mathbb{E}\Big[ \ell''_{n}(\lambda) \Big]
= - \mathbb{E}\Big[ S'_{n}(\lambda) 
\Big]
$$

$\mathcal{I}_{n}(\lambda)$: Fisher information
$\ell(\lambda)$: Log-likelihood function
$S$: [[Score Function]]

If is also the **inverse variance**:
$$
\mathcal{I}_{n}(\lambda) = \mathbb{V}(\lambda)^{-1}
$$

#### Calculating
1. Calculate *likelihood* function
2. Calculate *log-likelihood* function
3. Take derivative to get *score* function
4. Calculate *fisher information*

### Multi Parameter Estimators
Now we are estimating multiple parameters $\theta = (\theta_{1}, \theta_{2}, \dots, \theta_{k})$.
$$
H_{jj} = \frac{\partial^{2}\ell_{n}}{\partial \theta^{2}_{j}}
\quad\mathrm{and}\quad
H_{jk} = \frac{\partial^{2}\ell_{n}}{\partial \theta_{j} \partial \theta_{k}}
$$

$$
\mathcal{I}_{n}(\theta) =
\begin{bmatrix}
\mathbb{E}(H_{11}) & \mathbb{E}(H_{11}) & \cdots &  \mathbb{E}(H_{1k}) \\
\mathbb{E}(H_{21}) & \mathbb{E}(H_{22}) & \cdots &  \mathbb{E}(H_{2k}) \\
\vdots &  \vdots &  \ddots &  \vdots  \\
\mathbb{E}(H_{k1}) & \mathbb{E}(H_{k2}) & \cdots &  \mathbb{E}(H_{kk}) \\
\end{bmatrix}
$$
The is a [[Symetric Matrices|symetric matrix]]

---
#notag