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

**DETTE NORMERER OGSÅ FREKVENSERNE**

$$\Omega_{a} = C \tan\left(\frac{\omega_{a}T}{2}\right) \arrows C= \cot\left(\frac{\omega_{a}T}{2}\right)$$
$T$: Periode ($1/f_s$)


---
## Procedure
1. Prewarping konstanten bestemmes som
$$C= \cot\left(\frac{\omega T}{2}\right)$$
hvor $\omega = \omega_a$ ved lavpasfilterdesign og $\omega = \omega_{c}$ ved design af båndpas- og båndstopfiltre.


2. Prewarp og normer frekvenserne med formlen:

$$\Omega = c \cdot \tan\left(\frac{\omega T}{2}\right)$$
>[!tip]- Frequencies for band pas/stop filters
>$$Q = \frac{f_{c}}{\Delta f}$$
>$$f_{1} = f_{c} \cdot \left(\sqrt{1 + \frac{1}{4Q^{2}}} - \frac{1}{2Q}\right)$$
>$$f_{2} = f_{c} \cdot \left(\sqrt{1 + \frac{1}{4Q^{2}}} + \frac{1}{2Q}\right)$$

3. Find formfaktoren $F$ bestem [[Filters#Actual filter types|filtertype]] og find filterordenen.

**Low/High-pass**:
$$F = \frac{\Omega_{s}}{\Omega_{a}}$$
**båndpas**:
$$F = \frac{\Omega_{s_{2}}- \Omega_{s_{1}}}{\Omega_{a_{2}}- \Omega_{a_{1}}}$$

4. Den frekvensnormerede og faktoriserede analoge overføringsfunktion $H(s)$ opstilles (findes i tabel).
5. Transform to correct filter type ([[Filter Transformations]])

6. Overføringsfuntionen [[Filters#Frekvensnormering|denormeres]]

7. Lav z-transformationen

$$s \rightarrow C \frac{z-1}{z+1}$$

6. Filtret implementeres som en kaskadekoblet realisationsstruktur.

>[!example]- Example with bandpass filter
>![[lektion9.pdf]]

---
#signalprocessing
