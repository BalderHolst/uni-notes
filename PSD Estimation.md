---
created: 2026-11-16
tags:
  - statistical-signal-processing
slides:
  - "[[Lessons/Semester 7/ssp/Lektion 8 slides.pdf]]"
---

# PSD Estimation (Non-parametric)
[[Power Spectral Density (PSD)|Power Spectral Density]] Estimation.

$$
P_{x}(f) = \mathcal{F}\{ r_{xx}(\tau) \} = \mathbf{E}[|X(f)|^{2}]
$$
$P_{x}(f)$: Estimated Power Spectral  Transfer Function
$x(n)$: Input signal
$X(f)$: Transfer function of $x(n)$

##### Task
We take $N$ samples of $x(n)$. We use this to get an estimate of $P_{x}(f)$.


### Periodogram (Naive)
$$
\hat{P}_{x}(f) = \frac{1}{N}|X_{N}(f)|^{2}
$$
$X_{N}(f)$: DFT/FFT of $x(n)$.

This is **biased**:
$$
\mathbb{E}[P_{x}(f)] = P_{x} * W_\mathrm{bartlett}(f)
$$
As $N \to \infty$, the window becomes a [[Dirac Delta Function]], which is the ideal result.

Asymptotically unbiased.

It is however **not consistent**:

$$
\mathbb{V}[\hat{P}_{x}(f)] \simeq P^{2}_{x}(f)
$$

#### Bartlett Method
Averaging of sub-periodograms.

We split the signal of $N$ samples into $K$ blocks of length $L$.

$$K = \frac{N}{L}$$
We then do a periodogram on each section:
$$
\hat{P}^{(i)}_{x}(f) = \frac{1}{L} |X_{L}^{(i)}(f)|^{2}
$$
And an average on all PSDs
$$
\hat{P}_{x}(f) = \frac{1}{K} \sum_{i=1}^{k}P^{(i)}_{x}(f)
$$
It is still asymptotically unbiased, just like the periodogram.

It is however now **consistent**
$$
\mathbb{V}[\hat{P}_{x}(f)] = \frac{1}{K} P_{x}^{2}(f)
$$

**Resolution** is *worse*
$$
f_{2} - f_{1} \geq 0.89 \frac{f_{s}}{L}
$$

#### Welch's Method
Allow overlapping blocks and use windows to create smooth edges of blocks.

- Averaging sub-blocks, same as the Bartlett method.
- Allow overlapping blocks -> more blocks -> less variance
- Smoothing window

Usually $50\%$ overlap is usually ideal.

$$
K_{50\%} = 2 \frac{N}{L} - 1
$$

We use a **smoothing window**:
$$
x_{L}^{(i)}(n) * W_{L}(n)
$$
$W_{L}(n)$: Smoothing hamming window.

We have to compensate for the energy lost to the window function.

**Resolution**
$$
(f_{2} - f_{2}) \geq 1.28 \frac{f_{s}}{L}
$$

