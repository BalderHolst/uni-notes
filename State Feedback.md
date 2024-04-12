# State Feedback
See [[Lecture 9 - State Feedback Control.pdf|slides]].

- [[Controllability]]
- [[Controllable Canonical Form]]

Let A ∈ Rn×n, B ∈ Rn×1 be given.
1. Choose desired closed loop polynomial
det(λI − (A + BF)) = λn − acl,1λn−1 − . . . − acl,n.
2. Determine T, such that Ac = T −1AT and Bc = T −1B are in controllable canonical
form.
3. Determine open loop polynomial det(λI − A) = λn − a1λn−1 − . . . − an
4. Define Fc =
�
acl,1 − a1
. . .
acl,n − an
�
.
5. Compute resulting feedback gain F = FcT −1.


---
#controlsystems