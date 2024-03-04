# Root Locus Tuning
See [[Lecture 5 - Root Locus.pdf#page=46|slides]].

Us if a model of the system ***IS AVAILABLE***. If not, use [[Ziegler Nichols Tuning Method]] instead.

Here *one* parameter $K$ is changed, and the changes in the poles and zeros are plotted.

To tune a system with this method, the transfer function of the closed loop system should be on this form:
$$
H(s) = \frac{KG(s)}{1+KG(s)}, \s K \in \mathbb{R}
$$

Poles are now given by the characteristic formula:
$$1 + KG(s) = 0$$

>[!tip]- Convert to standard form
>1. Group all $K$-terms
>2. Divide by all non-$K$ terms

#### Root Locus Plot
Describes how the closed loop poles move in the $s$-place, when the $K$ changes. We move from the poles to the zeroes of the *open-loop* system.

##### Rules
See [[Lecture 5 - Root Locus.pdf#page=52|slides]].

There are many rules that a root locus plot follows. Here are a few.
1. $N = \mathrm{max}(m, n)$, where $N$ is number of lines (*loci*), $m$ is number of zeros and $n$ is number of poles.
2. As $K$ increases from $0$ to $\infty$, the roots move from the poles of $G(s)$ to the zeros of $G(s)$.
3. When roots are complex, they appear in complex conjugate pairs.
4. The portion of the real axis to the left of an *odd number* of open loop poles and zeros are part of the loci.
5. Lines must enter and leave the real axis at $90\degree$
6. Lines go to in


---
#controlsystems
