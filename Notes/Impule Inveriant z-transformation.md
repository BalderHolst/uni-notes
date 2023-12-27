## Impule Inveriant z-transformation
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=56|slides]]. Keeps impulse response the same.

$$H(z) = T \cdot \mathcal{Z}[h(n)]$$

If
$$H(s) = \sum_{i=1}^{N} \frac{k_{i}}{s-s_{i}}$$
then
$$H(z) = T \sum_{i=1}^{N}k_{i}\frac{z}{z - e^{s_{i}T}} = T \sum_{i=1}^{N}k_{i}\frac{1}{1 - e^{s_{i}T}z^{-1}}$$

---
## Procedure

1. Bestem det analoge prototypefilters frekvensnormerede overføringsfunktion $H(s)$.
2. [[Partialbrøker|Partialbrøksopløs]] $H(s)$ til 1. og 2. ordens overføringsfunktioner (maksimalt antal 2. ordens overføringsfunktioner).
3. [[Filters#Frekvensnormering|Denormer]] koefficienterne $k_i$ og polerne $\sigma_{i} + j\omega$ i ved *multiplikation med afskæringsfrekvensen ($\omega_{a}$) eller centerfrekvensen ($\omega_{c}$)*.
$$H(s) = \sum_{i=1}^{N} \frac{k_{i}}{s-s_{i}}$$
4. Bestem den digitale overføringsfunktions koefficienter. Hvis and ordens led se [[#Tranformation af 2. Ordens Overføringsfunktion]].
$$H(z) = T \sum_{i=1}^{N}k_{i}\frac{z}{z - e^{s_{i}T}} = T \sum_{i=1}^{N}k_{i}\frac{1}{1 - e^{s_{i}T}z^{-1}}$$
5. Implementer overføringsfunktionen som en parallelstruktur.

---

#### Tranformation af 2. Ordens Overføringsfunktion
See [[lektion 8 - Introduktion til IIR filtre.pdf#page=66|slides]].

Dette er den *denormerede* overføringsfunktionen
$$ H(s) = \frac{A_{0}}{B_{0} + B_{1} s + B_{2}s}$$
[[Notes/Partialbrøker|Partialbrøkopløs]] for at finde $\alpha$ og $\beta$.
$$
H(s) = \frac{k}{s-s_{i}} + \frac{k^{*}}{s-s_{i}^{*}}, \s
\begin{cases}
k = \alpha + j \beta \\
s_{i} = \sigma_{i} + j \omega_{i} \\
\end{cases}
$$
Udregn konstanter
$$
\begin{align}
a_{0} &= 2 \alpha_{i} \\
a_{1} &= -2e^{\sigma_{i}T}(\alpha \cos(\omega_{i}T) - \beta_{i} \sin(\omega_{i}T)) \\
b_{1} &= -(2e^{\sigma_{i}T} \cos(\omega_{i} T)) \\
b_{2} &= e^{2\sigma_{i}T}
\end{align}
$$

Opskriv overføringsfunktionen i z-donæne.
$$ H(z) = \frac{a_{0} + a_{1}z^{-1}}{1+b_{1}z^{-1} + b_{2}z^{-2}} $$

---
#signalprocessing 