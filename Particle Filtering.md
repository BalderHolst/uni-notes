# Particle Filtering

Also known as
- Sequential Monte Carlo (SMC)
- Sequential Importance Sampling (SIS)
- Sequential Importance Resampling (SIR)
- Bootstrap filtering
- Condensation (computer vision)
- Interacting particle approximation
- Survival of the fittest

#### Steps
0.  Sample $N$ particles from $P(X_{0})$
1. Each sample is propagated forward by sampling the next state value $x_{t+1}$ given the value $x_{t}$ for the sample, based on the transition model $P(X_{t+1}|X_{t})$.
2. Each sample is weighted by the likelihood it assigns to the new evidence, $P(e_{t+1}|x_{t+1})$.
3. The population is *resampled* to generate a new population of $N$ samples. Each new sample is selected from the current population; the probability that a particular sample is selected is proportional to its weight. The new samples are unweighted.

---

>[!tip]- Slide
>![[lecture8a.pdf#page=10]]

---
#intelligent-systems