# Marginal Distribution
Marginalization. See [[lecture6a.pdf#page=12|slides]].

- [[#Discrete]]
- [[#Continuous]]

---
## Discrete

if $X$, $Y$ have a joint distribution with mass function $f_{X,Y}$, then the **marginal mass function for $X$** is defines by:
$$
f_{X}(x) = \mathbf{P}(X=x) = \sum_{y}\mathbf{P}(X=x, Y=y) = \sum_{y}f_{X,Y}(x,y)
$$

And the marginal mass function for $Y$:
$$
f_{Y}(y) = \mathbf{P}(Y=y) = \sum_{x}\mathbf{P}(X=x, Y=y) = \sum_{x}f_{X,Y}(x,y)
$$
---

## Continuous
Marginal densities for continuous variables
$$
f_{X}(x) = \int f(x,y)\, dy \quad \mathrm{and} \quad f_{Y}(y) = \int f(x,y)\, dx
$$


---
#statistics #distribution