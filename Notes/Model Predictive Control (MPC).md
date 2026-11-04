---
created: 2026-11-02
tags:
  - controlsystems
slides:
  - "[[CAS-2026-Lecture6-LectureNotes.pdf]]"
  - "[[CAS-2026-Lecture6-MPC-fdblin.pdf]]"
---

# Model Predictive Control
Very similar to [[Optimal Control (LQR)|LQR]] as we want to find a control signal that mimizes the cost function:
$$
J(k) = \sum_{i=0}^{N-1}[x(k+i)^{T} Q x(k+i) + u(k+i)^{T}R u(k+i)]
$$
We make the optimization ***for every time step***. It is much heavier because of this.

In MPC, physical **actuator constraints can be directly included in the optimizer** as opposed to LQR.


