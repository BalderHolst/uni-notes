# Simulation of Robot Dynamics
$$
B(q)\ddot{q} + C(q, \dot{q}) \dot{q} + g(q) = \Gamma\tau
\quad \Rightarrow \quad

\ddot{q} = B(q)^{-1} \Big[\Gamma\tau - C(q, \dot{q}) \dot{q} + g(q) \Big]

$$

**Simulation**: Integrate $\ddot{q}$ over time to get $\dot{q}$ and $q$.

Requirements for the system:
- $B(q)$ must be inversible/have full rank
- $B(q)$ must only have *positive eigenvalues*
- $\ddot{q}$ and $\dot{q}$ must be integratable

### Nonlinear State Space Model
$$
\dot{x} = f(x) + g(x)u
$$
$x$: State vector
$$

\dot{x} =
\begin{bmatrix}
\dot{q} \\
\ddot{q}
\end{bmatrix}
=
\begin{bmatrix}
\dot{q} \\
-B(q)^{-1} \Big[\Gamma\tau - C(q, \dot{q}) \dot{q} + g(q) \Big]
\end{bmatrix}
+
\begin{bmatrix}
0 \\
B^{-1}(q)\Gamma
\end{bmatrix}
\tau
$$

$q$ and $\dot{q}$ will always be the state variables for mechanical systems.


---
#underactuated-robots