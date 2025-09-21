# Diskret Fourier Transformation
See [[Lektion 3 - Introduktion til FFT.pdf|slides]].

![[Diskret-Fourier-Transformation.png|Pasted image 20230928091317.png]]

Skalleringen ($1/N$) kan være i begge formler, bare den kun er i én af dem.
$$X(m) = \frac{1}{N} \sum_{n=0}^{N-1}x(nT) W_{N}^{mn}$$
$$x(n) = \sum_{m=0}^{N-1}X(m) W_{n}^{-mn}$$
$$W_{N}= e^{-j2\pi /N}$$
$N$: Samples pr. period ($\frac{1}{N} = FT$)
$T$: Time between samples

**The distance between samples in the frequency spectrum is $f_{s}/N$.**

Therefore we can get a higher resolution by *zero-padding*, which just means adding a bunch of zeros to the end of the signal in the time domain before transforming it.

---
#signalprocessing 