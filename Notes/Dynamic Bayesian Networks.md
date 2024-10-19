# Dynamic Bayesian Networks
See [[lecture8a.pdf|slides]].

Initial state distribution: $P(X_{0})$
Transition Model: $P(X_{t+1}|X_{t})$
Sensor Model: $P(E_{t}|S_{t})$

These probabilities do not change over time.

### Joint Distribution
$$
P(X_{0:t}, E_{1:t}) = \underbrace{P(X_{0})}_{\mathrm{Initial\; State}}
\prod_{i=1}^{t} \underbrace{ P(X_{i}|X_{i-1}) }_{\mathrm{Transition\; Model}}\;\;
\underbrace{P(E_{i}|X_{i})}_{\mathrm{Sensor\; Model}}
$$

---
### Inference Problems for Dynamic Model
See [[lecture5b.pdf#page=3|slides]].

#### Filtering
See [[lecture5b.pdf#page=4|slides]].

$$
P(X_{t+1}|e_{1:t+1}) = \alpha P(e_{t+1}|X_{t+1})\sum_{x_{t}}P(X_{t+1}|x_{t})P(x_{t}|e_{1:t})
$$
$\alpha$: Normalisation factor

Updated in two steps:

1. *Prediction*: $P(X_{t}|e_{1:t}) \to P(X_{t+1}|e_{1:t})$
2. *Measurement Update*: $P(X_{t+1}|e_{1:t}) \to P(X_{t+1}|e_{1:t+1})$

#### Prediction

#### Smoothing

#### Most Likely Explaination

#### Learning

---

### Inference
Exact inference is not feasible for DBNs. As you need to "unroll" the network over time, increasing the complexity with each time step. Therefore, an approximation is used instead.

Here are a few:
- [[Particle Filtering]]


---
#intelligent-systems