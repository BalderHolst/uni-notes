# Window Functions

When you multiply in the time domain, you [[Foldningssum|fold]] in the frequency domain.

We therefore want our window function to be as narrow as possible. Ideally window should resemble the [[Unit Sample]] in the frequency domain. 

## Effects on Filters
Filters dampening will also depend on the window function used.

## Windows

### Bartlet (Triangle)
$$w(n) = 
\begin{cases}
a - \frac{|n|}{M} , &\mathrm{for}\ -M \leq n \leq M \\
0                 , &\mathrm{Otherwise}
\end{cases}
$$

##

---
#notag