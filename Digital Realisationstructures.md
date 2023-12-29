## Digital Realisationstructures
A representation of a digital filter that could be implemented in a programming language. See [[lektion 7 - Digitale realisationsstrukturer.pdf|slides]].

$$y(n) = \sum_{i=0}^{N}  a_{i} \cdot x(n-i) - \sum_{i=1}^{N}b_{i} \cdot y(n-1) $$
$n$: time step
$x(n)$: input in the discrete time domain
$y(n)$: output in discrete time domain

### Different Ways of Implementing a Transfer Function
The ***Direct Type 1*** is the intuitive way to implement a discrete transfer function.
![[Pasted image 20231229141244.png|350]]

The ***Direct Type 2*** is the *better way* of implementing


---
#signalprocessing