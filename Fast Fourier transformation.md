# Fast Fourier transformation
See [[Lektion 3 - Introduktion til FFT.pdf|slides]].

[[Fourier-transformation]]

![[Pasted image 20230928082902.png|450]]

## Diskret Fourier Transformation

Skalleringen ($1/N$) kan være i begge formler, bare den kun er i én af dem.
$$X(m) := \sum_{n=0}^{N-1}x(nT) W_{N}^{mn}$$
$$x(n) = \frac{1}{N} \sum_{m=0}^{N-1}X(m) W_{n}^{-mn}$$
$$W_{N}= e^{-j2\pi /N}$$


---
#signalprocessing