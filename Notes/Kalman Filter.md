# Kalman Filter
See slides:
- [[Lecture 12 - The KalmanFilter.pdf#page=51|Control Systems - Kalman Filter]]
- [[lecture7a.pdf|Intelligent Systems - Kalman Filter]]
- [[lecture7b.pdf|Intelligent Systems - Kalman Filter (Vector  Case)]]



Both measurements and observer outputs are in represented as [[random variables]] to model measurement noise and observer inaccuracy.

We define how *confident* we are in the *model* and *measurements* respectively by defining their [[covariance]].

#### Stages

The Kalman filter works in two **stages**: *Prediction* and *update*. Every step results in a new [[Normalfordelingen|gaussian distribution]].

**Prediction**:
$$
P(X_{t+1}|e_{1:t}) = \int_{x_{t}} 
\;
\underbrace{P(X_{t+1}|x_{t})}_{\mathrm{Transition\ Model}}
\;\;
\underbrace{P(x_{t}|e_{1:t})}_{\mathrm{Current\ Dist.}}
$$

**Update**:
$$
P(X_{t+1}|e_{1:t+1}) =
\alpha
\,
\underbrace{P(e_{t+1}|X_{t+1})}_{\mathrm{New\ Evidence}}
\;
\underbrace{P(X_{t+1}|e_{1:t})}_{\mathrm{Prediction}}
$$

>[!tip]- Nice Slide
>![[lecture7b.pdf#page=10|slide]].

$\hat{x}_{k+1|k}$: The prediction of $x$ at $k+1$ given information at sample $k$.

$K_k$: is the "observer" gain for the Kalman filter.

The **Kalman gain** is defines as
$$
K_{k} = P_{k+1|k} C^{T} (CP_{k+1|k} C^{T} + R_{k})^{-1}
$$

$R_{k}$: Inaccuracy of measurements
$P_{k}$: Inaccuracy of model

---
#controlsystems
