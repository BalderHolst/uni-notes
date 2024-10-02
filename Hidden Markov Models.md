# Hidden Markov Models
See [[lecture6.pdf|slides]].

$$X_{t} \in \set{1,\dots, S}$$
$X_{t}$: States
$S$: Number of states

$$T \in \mathbb{R}^{S \times S}, \; [T]_{ij} = P(X_{t} = j | X_{t-1} = i)$$

$T$: Transition matrix
$$
O_{t} \in \mathbb{R}^{S\times S}, \; [O_{t}]_{ii} = P(e_{t}|X_{t} = i)
$$




---
#intelligent-systems