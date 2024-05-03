# Kalman Filter
See [[Lecture 12 - The KalmanFilter.pdf#page=47|slides]].

Both measurements and observer outputs are in represented as [[random variables]] to model measurement noise and observer inaccuracy.

We define how *confident* we are in the *model* and *measurements* respectively by defining their [[covariance]].

#### Stages
See [[Lecture 12 - The KalmanFilter.pdf#page=51|slides]].

The Kalman filter works in two **stages**: *Prediction* and *update*.

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