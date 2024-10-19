# Viterbi Algorithm
Use to find the most likely sequence given some input and a [[Dynamic Bayesian Networks|sensor and transition model]].

$$
\begin{align}
&\max_{x_{1},\dots, x_{t}} P(x_{1},\dots, x_{t},X_{t+1}|e_{1:t+1}) \\
&\quad\quad= \alpha P(e_{t+1}|X_{t+1}) \max_{x_{t}} \left(
P(X_{t+1}|x_{t})\; \max_{x_1,\dots,x_{t-1}} P(x_{1},\dots,x_{t-1},x_{t}|e_{1:e})
\right)
\end{align}
$$

$$
m_{1:t} = \max_{x_1,\dots,x_{t-1}} P(x_{1},\dots,x_{t-1},x_{t}, X_{t}|e_{1:e})
$$

Forward recursion
$$
\begin{align}
f_{1:k+1} &:= P(X_{k+1}|e_{1:k+1}) \\
&= \alpha P(e_{k+1}|X_{k+1}) \sum_{x_{k}} P(X_{k+1}|x_{k})P(x_{k}|e_{1:k})\\
&= \alpha \cdot \mathrm{Forward}(f_{1:k}, e_{k+1})
\end{align}
$$

---
#intelligent-systems