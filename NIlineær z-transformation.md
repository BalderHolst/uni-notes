# BIlineær z-transformation
See [[lektion 9 - Design af IIR filtre.pdf|slides]].
$$s= \frac{2}{T} \frac{z-1}{z+1}$$
$$H(z) = H(s)|_{s = f(z)}$$

### Warping
Normalt er  en vinkel på $\pi$ lig 
![[Pasted image 20231107084334.png|300]]

>[!tip]- Hvorfor?
>Oversættelsen til $z$-domæne er normalt $z = e^{sT}$. Dette betyder også:
>$$s = \frac{1}{T} \ln(z)$$
>Da $\ln(x)$ er en uendelig sum giver dette et uendeligt antal poler/nulpunker i overføringsfunktioner i $z$-domænet.
>
>I stedet approximerer vi med et [[Taylorpolynomium|førsteordens-taylorpolynomium]]:
>$$\ln(x) \approx 2 \frac{x-1}{x+1}$$
>Det giver udtryk:
>$$s= \frac{2}{T} \frac{z-1}{z+1} \arrows z = \frac{\frac{2}{T} + s}{\frac{2}{T}-s}$$

---
#signalprocessing
