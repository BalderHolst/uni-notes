# Bevægelse på Skråplan
![[Bevægelse på Skråplan.png]]


På billedet ovenfor ses en plan klods, der glider ned af et skråplan uden
gnidning. Skråplanet danner vinklen $\alpha$ med vandret. Kræfterne, der
virker på klodsen, er indtegnet på figuren, og de er som følger:

Tyngdekraften:

$$F_{t} = m \cdot g$$

Som kan opdeles i to komposanter:

$$F_{1} = m \cdot g \cdot \sin{(\alpha)}$$

$$F_{2} = m \cdot g \cdot \cos{(\alpha)}$$

Normalkraften er lige så stor og modsatrettet som $F_{2}$:

$$F_{N} = F_{2}$$

Ligger vi et koordinatsystem, så x-aksen følger skråplanet og y-aksen er
vinkelret på skråplanet for vi således:

$$F_{res,x} = F_{1} = m \cdot g \cdot \sin(\alpha)$$

$$F_{res,y} = F_{2} - F_{N} = 0$$

Ud fra [[Newtons Love#Newtons 2 lov Kraftloven|Newtons II lov]] kan vi bestemme accelerationen i x-aksens retning:

$$m \cdot a = m \cdot g \cdot \sin(\alpha) \s \Longleftrightarrow \s a = g \cdot \sin(\alpha)$$

Her kan vi se at tyngdekraften virker i retninen $\alpha$. 

---

Ser vi nu på en plan klods på skråplanet med gnidning, får vi en
gnidningskraft i modsatte retning af $F_{1}$, jf. Figur 2. Denne
gnidningskraft er givet ved:

$$F_{\text{gnid}} = \mu \cdot F_{N} = \mu \cdot m \cdot g \cdot \cos{(\alpha)}$$

Hvorfor den resulterende kraft i x-aksens retning nu er:

$$F_{res,x} = F_{1} - F_{\text{gnid}} = m \cdot g \cdot \sin(\alpha) - \mu \cdot m \cdot g \cdot \cos{(\alpha)}$$

Hvor vi igen ud fra [[Newtons Love#Newtons 2 lov Kraftloven|Newtons II lov]] lov kan finde accelerationen:

$$m \cdot a = m \cdot g \cdot \sin(\alpha) - \mu \cdot m \cdot g \cdot \cos(\alpha) \s \Longleftrightarrow \s a = g \cdot \left( \sin(\alpha) - \mu \cdot \cos(\alpha) \right)$$

Bevæger klodsen sig med konstant hastighed ned af skråplanet, dvs. med
$a = 0$, kan vi bestemme gnidningskoefficienten, $\mu$, ud fra
ovenstående formel:

$$0 = \sin(\alpha) - \mu \cdot \cos(\alpha) \s \Longleftrightarrow \s \mu = \tan(\alpha)$$

Ud fra ovenstående ses det altså, at vi ud fra vinklen, $\alpha$, kan
bestemme henholdsvis acceleration på en plan klods uden
gnidningsmodstand og gnidningskoefficient mellem klods og skråplan med
gnidningsmodstand. Vinklen kan endvidere bestemmes ud fra længde, *l*,
og højden, *h*, af skråplanet:

$$\tan(\alpha) = \frac{h}{l}$$

Vi ser således, at:

$$\mu = \frac{h}{l}$$

Afhængig af opstillingen kan det være nemmere at måle længden af
skråplanet (hypotenusen) i stedet for enten *l* eller *h*. I dette
tilfælde overlades det til laseren selv at finde en forskrift for
gnidningskoefficienten ud fra trigonometriske betragtninger.

---
#fysik 