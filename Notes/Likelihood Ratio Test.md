# Likelihood Ratio Test

> [!info]- Slide
> ![[Lessons/Semester 7/statistics/Lektion 3 slides.pdf#page=5|slide]]

Comparing an unrestrained model and a restrained model, to see how different they are.

Given observations
$$
X_{1}, \dots, X_{n}
\quad
\mathrm{iid}
\quad
X_{j} \sim N_{p}(\mu, \Sigma)
$$
$H_{0}$: $\mu \overset{?}{=} \mu_{0}$

**Unconstrained model**:
$$
(\mu, \Sigma\ \mathrm{vary\ freely})
$$

Likelihood function:
$$
L(\mu, \Sigma) = \mathbf{P}(\mathrm{observations} | \mu, \Sigma)
$$

**Constrained model**:
$$
(\mu = \mu_{0}, \Sigma\ \mathrm{vary\ freely})
$$
Likelihood function:
$$
L_{0}(\Sigma) = \mathbf{P}(\mathrm{observations} | \Sigma)
$$

We *maximize* both likelihood funcitons, and compare to get the likelihood ratio $\Lambda_{LR}$.

$$
\Lambda_{LR} =
\frac{ \mathrm{max}(L_{0}(\Sigma )) }{ \mathrm{max}(L(\mu, \Sigma)) } 
\quad 0 \leq \Lambda_{LR} \leq 1
$$

$\Lambda_{LR} \approx 1$: $H_{0}$ is *true*!
$\Lambda_{LR} \approx 0$: $H_{0}$ is false!

Given [[Multivariate Normal Distribution|MVN]] pdf's:
$$
\Lambda_{LR} = \left(\frac{|S|}{|\hat{\Sigma_{0}}|}\right)^{n / 2}
$$
Large Sample Distribution
$$
-2 \log \Lambda_{LR} = -\log \frac{|S|}{|\hat{\Sigma_{0}}|} \sim \chi^{2}(\mathrm{df} - \mathrm{df}_{0})
$$
where:
$\mathrm{df}$: $\mathrm{dim}(L(\mu, \Sigma)) = \mathrm{dim}(\mu) + \mathrm{dim}(\Sigma)$
$\mathrm{df}_{0}$: $\mathrm{dim}(L_{0}(\Sigma)) = \mathrm{dim}(\Sigma)$

$$
-2 \log \Lambda_{LR} \geq \chi^{2}(p)_{\alpha}
\quad\Rightarrow\quad
\mathrm{reject}\ H_{0}
$$

---
#multivariate-statistics 