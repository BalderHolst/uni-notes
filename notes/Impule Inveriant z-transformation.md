## Impule Inveriant z-transformation
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=56|slides]]. Keeps impulse response the same.

$$H(z) = T \cdot \mathcal{Z}[h(n)]$$

$$H(z) = T \sum_{i=1}^{N}k_{i}\frac{z}{z - e^{s_{i}T}} = T \sum_{i=1}^{N}k_{i}\frac{1}{1 - e^{s_{i}T}z^{-1}}$$
##### Procedure
1. Bestem det analoge prototypefilters frekvensnormerede overføringsfunktion H(s).
2. [[Partialbrøker|Partialbrøksopløs]] $H(s)$ til 1. og 2. ordens overføringsfunktioner (maksimalt antal 2. ordens overføringsfunktioner) (.



3. Denormer koefficienterne $k_i$ og polerne $\sigma_{i} + j\omega$ i ved multiplikation med
afskæringsfrekvensen eller centerfrekvensen.
4. Bestem den digitale overføringsfunktions koefficienter.
5. Implementer overføringsfunktionen som en parallelstruktur.

---
#signalprocessing 