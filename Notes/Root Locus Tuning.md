# Root Locus Tuning
See [[Lecture 5 - Root Locus.pdf#page=46|slides]].

Use if a model of the system ***IS AVAILABLE***. If not, use [[Zeigler Nichols Tuning Method]] instead for tuning [[PID-controller|PID-controllers]].

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

>[!example]- Examples of Locus Plots
>![[Pasted image 20240304095810.png]]
>![[Pasted image 20240304095732.png]]

##### Rules
See [[Lecture 5 - Root Locus.pdf#page=52|slides]].

There are many rules that a root locus plot follows. Here are a few.
1. $N = \mathrm{max}(m, n)$, where $N$ is number of lines (*loci*), $m$ is number of zeros and $n$ is number of poles.
2. As $K$ increases from $0$ to $\infty$, the roots move from the poles of $G(s)$ to the zeros of $G(s)$.
3. When roots are complex, they appear in complex conjugate pairs.
4. The portion of the real axis to the left of an *odd number* of open loop poles and zeros are part of the loci.
5. Lines must enter and leave the real axis at $90\degree$
6. Lines go to infinity along asymptotes. The angles of the asymptotes are
$$\phi_{l} = \frac{180\degree + 360\degree (l - 1)}{n-m}, \s \text{for}\ l = 1, \dots,n-m$$
The centroid of the asymptotes is

$$
\frac{\sum_{i=1}^{n} p_{i} - \sum_{j=1}^{m} z_{j}}{n-m}
$$
7. The angle(s) departure of a branch of the locus from a pole of *multiplicity* $q$ is given by
$$
\phi_{l,dep} = \frac{\sum \psi_{i} - \sum_{i \neq l} \phi_{i} - 180\degree - 360\degree (l-1) }{q}
$$
$\sum \psi_{i}$: The sum of angles to all the zeros
$\sum_{i\neq l} \phi_{i}$: The sum of angles to all but the $l$'th pole
8. The same root will never cross its own path
9. If there are not enough poles and zeros to make a pair, the remaining lines go to infinity.


---
#controlsystems
