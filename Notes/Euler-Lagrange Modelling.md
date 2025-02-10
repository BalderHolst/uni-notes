# Euler-Lagrange Modelling
Using [[Potential Energy|potential]] and [[Kinetic Energy|kinetic]] energy to model systems. See [[Lecture 1 - Euler-Lagrange Modelling.pdf#page=5|slides]].

$$
I(t, q, \dot{q}) = \int_{a}^{b} \mathcal{L}(t, q, \dot{q})
$$

### Only Conservative Forces
$$
\frac{d}{dt} \frac{\partial\mathcal{L}}{\partial\dot{\mathbf{q}}} - \frac{\partial\mathcal{L}}{\partial\mathbf{q}} = 0
$$
$$
\mathcal{L} = E_\mathrm{kin} - E_\mathrm{pot}
$$


$t$: Time
$q$: [[Generalized Coordinates]]

### With Non-conservative Forces
Everything on the left side is the same. Therefore, begin by excluding non-conservative forces and expand the model later.

> [!warning] Q is conservative!
> $Q$ must **ONLY** include *non*-conservative forces. Conservative forces are accounted for by $\mathcal{L}$.

$$
\frac{d}{dt} \frac{\partial\mathcal{L}}{\partial\dot{\mathbf{q}}} - \frac{\partial\mathcal{L}}{\partial\mathbf{q}} = Q
$$
$$
\mathcal{L} = E_\mathrm{kin} - E_\mathrm{pot}
$$


$t$: Time
$q$: [[Generalized Coordinates]]
$Q$: Non-conservative/generalized forces

This results in the dynamics of the system:
$$
\underbracket{B(q)}_\mathrm{Inertia}\ddot{q}
+
\underbracket{C(q, \dot{q})} \dot{q}
+
g(q) = \Gamma\tau
$$
$\tau$: Matrix of forces

---
#underactuated-robots