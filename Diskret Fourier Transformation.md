# Diskret Fourier Transformation
See [[Lektion 3 - Introduktion til FFT.pdf|slides]].

![[Pasted image 20230928091317.png]]

Skalleringen ($1/N$) kan være i begge formler, bare den kun er i én af dem.
$$X(m) := \sum_{n=0}^{N-1}x(nT) W_{N}^{mn}$$
$$x(n) = \frac{1}{N} \sum_{m=0}^{N-1}X(m) W_{n}^{-mn}$$
$$W_{N}= e^{-j2\pi /N}$$
---
#signalprocessing 