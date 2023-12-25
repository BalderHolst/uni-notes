# Fast Fourier transformation
See [[Lektion 3 - Introduktion til FFT.pdf#page=37|slides]].

An algorithm for computing a [[Diskret Fourier Transformation]]. This can be implemented in *many ways*.

Time complexity:
$$O\left(\frac{n}{2} \log_{2}(n)\right)$$

#### Idea
$W_N$ can be calculated once, and *rotated* in the imaginary plane to find the others. There will be $N$ amount of $W_N$ going clockwise around the imaginary unit circle.
$$W_{N}^{1}, W_{N}^{2} \dots W_{N}^{N-1}$$
$$W_{N}^{N} = W_{N}^{1},\,\, W_{N}^{N+2} = W_{N}^{3}$$

### Window

$$h(n) = h_{\infty}(n)w(n)$$
A good window will be as **narrow as possible** in the frequency domain.
#### Rectangular

$$
w(n) = \begin{cases}
1, \,\, -M \leq n \leq M \\ \\
0, \,\, \text{else}
\end{cases}
$$
$h_{\infty}(n)$: The infinite impulse response

A rectangular window results in the frequency domain getting multiplied by a $\text{sinc}$ function.

The $\text{sinc}$ function creates oscillations called Gipps oscillations.

#### Barlett
Main lobe is wider and in rectangular window, meaning a worse window. It does however reduce Gipps oscillations.
$$
w(n) =
\begin{cases}
1- \frac{|n|}{M}, &\text{if} -M \leq n \leq M \\
0, &\text{else}
\end{cases}
$$

$n$: sample number

#### Hamming and Hanning
Still a *wider main lobe* than the rectangular window, but **much lower oscillations**.

Hanning: $\alpha = 0.5$
Hamming: $\alpha = 0.54$

$$
w(n) =
\begin{cases}
\alpha + (1- \alpha) \cos\left(\frac{n\pi}{M}\right), &\text{if} -M \leq n \leq M \\
0, &\text{else}
\end{cases}
$$

### Errors in FFT
- Picket fencing: We may not be able to see the frequency we are interested in if it exists between the FFT "bars".

## Matlab
```matlab
fft()
```



---
#signalprocessing
