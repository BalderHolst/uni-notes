# Dynamic Bayesian Networks
See [[lecture8a.pdf|slides]].

Initial state distribution: $P(X_{0})$
Transition Model: $P(X_{t+1}|X_{t})$
Sensor Model: $P(E_{t}|S_{t})$

These probabilities do not change over time.

### Inference
Exact inference is not feasible for DBNs. As you need to "unroll" the network over time, increasing the complexity with each time step. Therefore, an approximation is used instead.

Here are a few:
- [[Particle Filtering]]


---
#intelligent-systems