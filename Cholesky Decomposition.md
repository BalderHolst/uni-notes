# Cholesky Decomposition
See [[week2.pdf#page=12|slides]].


$$
A = L'D(L'D)^{T} = LL^{T} 
$$

$A$: A [[Symetric Matrices|symetric]] and [[Positive semi-definite matrix|positive semi-definete]] matrix
$L'$: The $L$ from [[LU Decomposition]]

where
$$
L= L'D
$$
with 
$$L_{ii} = 1$$

---

- About twice as fast as [[LU Decomposition]]
- There is no need to swap rows
- A little mure numerically stable than [[LU Decomposition]]

---

>[!warning] Not a general method
> Requires $A$ to be a [[Symetric Matrices|symetric]] and [[Positive semi-definite matrix|positive semi-definete]].


---
#numerical-methods 