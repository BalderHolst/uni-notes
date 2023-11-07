# Bilineær z-transformation
See [[lektion 9 - Design af IIR filtre.pdf|slides]].
$$s = f(z) = C \frac{z-1}{z+1}$$
$$H(z) = H(s)|_{s = f(z)}$$
$C$: [[#Pre-Warping|Prewarping-konstanten]]

>[!tip]- Hvorfor?
>Oversættelsen til $z$-domæne er normalt $z = e^{sT}$. Dette betyder også:
>$$s = \frac{1}{T} \ln(z)$$
>Da $\ln(x)$ er en uendelig sum giver dette et uendeligt antal poler/nulpunker i overføringsfunktioner i $z$-domænet.
>
>I stedet approximerer vi med et [[Taylorpolynomium|førsteordens-taylorpolynomium]]:
>$$\ln(x) \approx 2 \frac{x-1}{x+1}$$
>Det giver udtryk:
>$$s= \frac{2}{T} \frac{z-1}{z+1} \arrows z = \frac{\frac{2}{T} + s}{\frac{2}{T}-s}$$

## Warping
Normalt er  en vinkel på $\pi$ lig en frekvens lig $f_o$. Her er en vinkel på $\pi$ eller $-\pi$ lig en **uendelig frekvens**. Dette betyder at (specielt høje) frekvenser forvrænges.
![[Pasted image 20231107084334.png|center|350]]

$\Omega$: Original frekvens
$\omega$: Warpet frekvens
![[Pasted image 20231107085053.png|center|300]]

#### Pre-Warping
For at komme udenom warping warper vi først overføringsfunktionen i den mosatte retning, sådan et den resulterende overføringsfunktion har $f_{a}$.

*Stopbåndsfrekvensen er knap så vigtig* da warping blåt gør dæmpningen større.

$$\Omega_{a} = C \tan\left(\frac{\omega_{a}T}{2}\right) \arrows C= \cot\left(\frac{\omega_{a}T}{2}\right)$$
$T$: Periode ($1/f_s$)

---
#signalprocessing
