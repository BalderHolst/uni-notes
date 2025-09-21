# Laplace Transformation
Se [regneregler](https://tutorial.math.lamar.edu/classes/de/Laplace_Table.aspx).

### Overføringsfunktion
$$\text{impuls} \rightarrow \text{respons}$$

$$
H(s) = \mathcal{L}\{h(t)\} = \int_{-\infty}^{\infty} h(t) e^{-st} \, dt, \s s  = \sigma + j\omega$$

$h(t)$: Impulse response in the *time* domain.
$s$: Input signal 

$$H(s) = \frac{\text{output}(s)}{\text{input}(s)}$$

#### Poles
$$H(s) = \frac{\beta}{\alpha} \Rightarrow 
\begin{cases}
\beta = 0 &\Rightarrow \text{nulpunkter} \\
\alpha = 0 &\Rightarrow \text{poles}
\end{cases}
$$
$\alpha$: den karakteristikle ligning

Pol = Singularitet i frekvensdomæne

![[Laplace-Transformation-Poles.png|Pasted image 20230913215819.png]]

If poles are **on the imaginary axis** the impulse response will result in a constant oscillation at the frequency.

### Table
![[Laplace-Transformation-Table.png|Pasted image 20231208095254.png]]

---
## Inverse Laplace Transformation
$$\text{respons} \rightarrow \text{impuls}$$

Try to use tables instead of this equation.

$$
f(t) = \frac{1}{2\pi j} \int_{\sigma_{c}-j\infty} TODO
$$


---
#matematik #signals
