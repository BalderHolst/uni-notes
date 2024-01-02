# Fourier-transformation
[[Trigonometri|Trigonometric]] approximations for *aperiodic signals*.

Make the period of the signal, as large as the signal duration and use [[Fourieseries]].
$$L \to \infty$$
$$
X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} \mathrm{dt}
$$

$$
x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j \omega t} \mathrm{d\omega}
$$

---
#matematik #signals 