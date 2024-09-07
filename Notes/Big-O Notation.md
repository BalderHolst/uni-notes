# Big-O Notation
The worst case run-time characteristics of an algorithm. Big-O notation denotes a set which contains all functions that grow slower at the same speed as the input function when $n$ is very big.

It is a way of describing the performance of an algorithm for (infinitely) **large inputs *independent of hardware**.

>[!warning] Small Inputs
>Big-O does *not say anything about small input* run time.
>
> Say $T_1(n) = 100000n$ and $T_2 = n^2$, then $T_1$ may be preferable, even though it has a "worse" time-complexity.

#### Sets and Order

$$
O(1) \:\:\subset\:\: O(n) \:\:\subset\:\: O(n \cdot \log n) \:\:\subset\:\: O(n^2) \:\:\subset\:\: O(n!)
$$


#### Formal Definition
$$
\begin{align}
O(f(n)) &= {g(n): \exists c > 0: \exists n_0 \in \N_+: \forall n \geq n_0: g(n) \leq c \cdot f(n)}\\
\Omega (f(n)) &= {g(n): \exists c > 0: \exists n_0 \in \N_+: \forall n \geq n_0: g(n) \geq c \cdot f(n)}\\
\Theta (f(n)) &= O(f(n)) \cup \Omega (f(n))\\
\end{align}
$$

$n_0$: The point as which the faster growing function will overtake the slower growing one.
$c$: Any constant




---
#algorithms
