# Fisher Information
A measure for how much information each sample contains.

$$
\mathcal{I}_{n}(\lambda)
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

### Calculating
1. Calculate *likelihood* function
2. Calculate *log-likelihood* function
3. Take derivative to get *score* function
4. Calculate *fisher information*


---
#notag