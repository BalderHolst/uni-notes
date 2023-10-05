# Fast Fourier transformation
See [[Lektion 3 - Introduktion til FFT.pdf#page=37|slides]].

An algorithm for computing a [[Diskret Fourier Transformation]]. This can be implemented in *many ways*.

Time complexity:
$$O\left(\frac{n}{2} \log_{2}(n)\right)$$

#### Idea
$W_N$ can be calculated once, and *rotated* in the imaginary plane to find the others. There will be $N$ amount of $W_N$ going clockwise around the imaginary unit circle.
$$W_{N}^{1}, W_{N}^{2} \dots W_{N}^{N-1}$$
This means that

#### Matlab
```matlab
fft()
```


---
#signalprocessing