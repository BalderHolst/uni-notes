# Window Functions

When you multiply in the time domain, you [[Foldningssum|fold]] in the frequency domain.

We therefore want our window function to be as narrow as possible. Ideally window should resemble the [[Unit Sample]] in the frequency domain. 

## Effects on Filters
Filters dampening will also depend on the window function used.

If we assume an ideal filter, the transition from amplification of $1$ to amplification of $0$ with have the same width of the main lobe of the window function.

## Windows
See [[lektion 11 - Design af FIR filtre.pdf#page=7|slides]].

### Rectangular Window
$$w(n) = 
\begin{cases}
1, &\mathrm{for}\ -M \leq n \leq M \\
0                 , &\mathrm{Otherwise}
\end{cases}
$$

### Bartlet (Triangle)
$$w(n) = 
\begin{cases}
a - \frac{|n|}{M} , &\mathrm{for}\ -M \leq n \leq M \\
0                 , &\mathrm{Otherwise}
\end{cases}
$$

### Hanning and Hamming window
$$w(n) = 
\begin{cases}
\alpha + (1 - \alpha) \cdot \cos(\frac{n\pi}{M}) , &\mathrm{for}\ -M \leq n \leq M \\
0                 , &\mathrm{Otherwise}
\end{cases}
$$
### Kaiser Window
See [[lektion 11 - Design af FIR filtre.pdf#page=34|slides]].

$\beta$ alters the side lobe amplification.

---
#notag