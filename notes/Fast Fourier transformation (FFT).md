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

A good window will be as **narrow as possible** in the frequency domain.
#### Rectangular

$$h(n) = h_{\infty}(n)w(n)$$
$$
w(n) = \begin{cases}
1, \,\, -M \leq n \leq M \\ \\
0, \,\, \text{else}
\end{cases}
$$
$h_{\infty}(n)$: The infinite impulse response

A rectangular window results in the frequency domain getting multiplied by a $\text{sinc}$ function.

The $\text{sinc}$ function creates oscillations called Gipps oscillations.

#### Matlab
```matlab
fft()
```


---
#signalprocessing
