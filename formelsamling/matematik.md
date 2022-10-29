### Fordoblingskonstanten
Se [[notes/Fordoblings- og halveringkonstant#Fordoblingskonstanten]].

$$T_2= \frac{ln(2)}{ln(a)}$$

$a$ : $a$-værdien i den [[Eksponentielle Funktioner|eksponentielle funktion]].

---

### Halveringskonstanten
Se [[notes/Fordoblings- og halveringkonstant#Halveringskonstanten]].

$$T_2= \frac{ln(\frac{1}{2})}{ln(a)}$$

$a$ : $a$-værdien i den [[Eksponentielle Funktioner|eksponentielle funktion]].

---

### Gradient
Se [[notes/Gradient#Gradient]].

$$\nabla f(x_0,y_0)=\v{f_x'(x_0,y_0)}{f_y'(x_0,y_0)}$$


---

### Andengradspolynomier
Se [[notes/Andengradspolynomier#Andengradspolynomier]].

$$f(x) = ax^2 + bx + c$$


---

### Toppunktet
Se [[notes/Andengradspolynomier#Toppunktet]].

$$\left( \frac{-b}{2a}, \frac{-d}{4a} \right)$$

$$f(x) = ax^2+bx+c$$

$$f'(x)=2ax+b$$

$$0 = 2ax+b$$

$$x=\frac{-b}{2a}$$

$$f(x)=a \cdot \left(\frac{-b}{2a} \right)^2 + b \cdot \left(\frac{-b}{2a} \right) + c$$

$$f(x)=a \cdot \frac{(-b)^2}{2^2 \cdot a^2} + \frac{-b^2}{2a} + c \arrows f(x)=\cdot \frac{\c{a} \cdot b^2}{4a^\c{2}} + \frac{-b^2}{2a} +c$$

$$f(x)=\cdot \frac{b^2}{4a} + \frac{-b^2}{2a} + c$$

$$f(x)=\frac{b^2}{4a} + \frac{-2b^2}{4a} + \frac{4ac}{4a} = \frac{-b^2+4ac}{4a}$$

$$\left(\frac{-b}{2a}, \frac{-d}{4a} \right)$$


---

### Diskriminanten
Se [[notes/Andengradspolynomier#Diskriminanten]].

$$d = b^2 - 4ac$$

$$x = \frac{-b \pm \sqrt{d}}{2a}$$


---

### Definition af et Differentiale
Se [[notes/Differentialregning#Definition af et Differentiale]].

$$a=\frac{y_2-y_1}{x_2-x_1}$$

$$a=\frac{f(x_0+h)-f(x_0)}{\bcancel{x_0}+h-\bcancel{x_0}} \arrows a=\frac{f(x_0+h)-f(x_0)}{h}$$


---

### Linære Funktioner
Se [[notes/Linære Funktioner#Linære Funktioner]].

$$f(x) = ax +b$$


---

### To-punktsformlen
Se [[notes/Linære Funktioner#To-punktsformlen]].

$$a=\frac{\Delta y}{\Delta x}=\frac{y_2-y_1}{x_2-x_1}$$

$$b = y_1 - ax_1$$


---

### Omvendt funktion (inverse funktion)
Se [[notes/Omvendt funktion#Omvendt funktion (inverse funktion)]].

$$f(f^{-1}(x))=f^{-1}(f(x))=x$$

$$f(x) = e^x \: \Rightarrow \: f^{-1}(x) = ln(x)$$

$$f(x)=\sqrt{x} \:\Rightarrow\: f^{-1}(x)=x^2$$


---

### Hvordan *finder* man en omvendt funktion?
Se [[notes/Omvendt funktion#Hvordan *finder* man en omvendt funktion?]].

$$f(x)=y=2x+3$$

$$x=2y+3$$

$$\frac{x-3}{2}=y$$

$$f^{-1}(x)=\frac{x-3}{2}$$


---

### Differentiering med omvendte funktioner
Se [[notes/Omvendt funktion#Differentiering med omvendte funktioner]].

$$\frac{d}{dx}(x^{x+\sin(x)})$$

$$x = e^{\ln (x)} \arrow \frac{d}{dx}(e^{ln(x)})^{x+sin(x)})$$

$$a^{b^c} = a^{a \cdot c} \arrow \frac{d}{dx}(e^{ln(x) \cdot (x + sin(x))})$$

$$\frac{d}{dx}(e^{f(x)}) = e^{f(x)} \cdot f'(x) \arrow e^{ln(x) \cdot (x+sin(x))} \cdot \frac{d}{dx}(ln(x) \cdot (x+sin(x))$$

$$= x^{x+sin(x)} \cdot (\frac{1}{x} \cdot (x+sin(x)+ln(x)\cdot (1+cos(x))))$$


---

### Bevis for [[Linjer og Vektorer i 2D#Parameterfremstilling|Parameterfremstilling]]
Se [[notes/Bevis for Parameterfremstilling#Bevis for [[Linjer og Vektorer i 2D#Parameterfremstilling|Parameterfremstilling]]]].

$$\vec{OP_0}$$

$$\vec{OP_0} + \vec{P_0P}$$

$$\v{x_0}{y_0} + t \cdot \v{r_1}{r_2}$$

$$\v{x}{y} = \v{x_0}{y_0} + t \cdot \v{r_1}{r_2}$$


---

### Planer
Se [[notes/Planer#Planer]].

$$\vec{n} \bullet(P-P_0) = 0$$

$\vec{n}$ : Normalvektor til planen.
$P_0$ : Et "startpunkt" på planen.
$P$ : Et hvilken som helst punkt på planen.

---

### Kvadratkomplettering
Se [[notes/Kvadratkomplettering#Kvadratkomplettering]].

$$x^2 + 2kx = (x + k)^2 - k^2$$

$$x^2 + 6 \cdot x  \Leftrightarrow  x^2 + 2 \cdot 3 \cdot x$$

$$k = 3$$

$$x^2 + 2 \cdot 3 \cdot x = (x + 3)^2 - 3^2$$


---

### Formel for tangentplan
Se [[notes/Tangentplan#Formel for tangentplan]].

$$z = p \cdot (x-x_0)+q \cdot (y-y_0) + z_0$$

$x_0$ : punktets $x$-koordinat
$y_0$ : punktets $y$-koordinat
$z_0$ : punktets $z$-koordinat
$f_x'(x,y)$ : funktionen [[Differentiation af funktioner med to variable|differentieret]] med hensyn til $x$
$f_y'(x,y)$ : funktionen [[Differentiation af funktioner med to variable|differentieret]] med hensyn til $y$
$$p=f_x'(x_0,y_0) \s\text{og}\s q=f_y'(x_0,y_0)$$

$x_0$ : punktets $x$-koordinat
$y_0$ : punktets $y$-koordinat
$z_0$ : punktets $z$-koordinat
$f_x'(x,y)$ : funktionen [[Differentiation af funktioner med to variable|differentieret]] med hensyn til $x$
$f_y'(x,y)$ : funktionen [[Differentiation af funktioner med to variable|differentieret]] med hensyn til $y$

---

### Flere Trigonometriske Sammenhlænge
Se [[notes/Integraler Regneregler#Flere Trigonometriske Sammenhlænge]].

$$\int\frac{1}{\sqrt{1-x^{2}}}\dx=\arcsin(x)$$


---

### Bevis for Løsningsformlen
Se [[notes/Bevis for Løsningsformlen#Bevis for Løsningsformlen]].

$$f(x) = ax^2+bx+c = 0$$

$$4a^2x^2 + 4abx + 4ac = 0$$

$$4a^2x^2 + 4abx + 4ac + b^2 - 4ac = b^2  - 4ac $$

$$\text{venstre:}\s 4a^2x^2 + b^2 + 4abx$$

$$a=2ax,\, b=b$$

$$\text{venstre: } \s (2ax+b)^2$$

$$(2ax+b)^2 = b^2 -4ac$$

$$d = b^2-4ac$$

$$(2ax+b)^2 = d$$

$$(2ax+b)^2 = d \arrows 2ax+b = \sqrt{d} \arrows 2ax = \sqrt{d} - b \arrows x = \frac{\sqrt{d} - b}{2a}$$

$$x = \frac{-b \pm \sqrt{d}}{2a}$$


---

### Flader
Se [[notes/Flader#Flader]].

$$n \bullet (r-r_0)=0 \arrows A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$$

$$Ax + By + Cz = D \s \text{hvor } D = Ax_0 + By_0 + Cz_0$$


---

### Cylinderiske Koordinater
Se [[notes/Cylinderiske Koordinater#Cylinderiske Koordinater]].

$$P = [r, \theta,z]$$

$r$ : Længden fra $z$ aksen.
$\theta$ : Vinklen fra $x$ aksen i $xy$ planen.
$z$ : Højden

---

### Oversæt til Cartesiske koordinater
Se [[notes/Cylinderiske Koordinater#Oversæt til Cartesiske koordinater]].

$$x= \cos \theta \s y = r \sin \theta \s z = z$$


---

### Gange med matricer
Se [[notes/Matricer#Gange med matricer]].

$$c_{ij} = \sum_{k=1}^n a_{ik} \cdot b_{kj}$$

$$A_{m\times n} \cdot B_{n\times n}\s\checkmark$$


---

### Ikke Kommutativ
Se [[notes/Matricer#Ikke Kommutativ]].

$$A \cdot B \neq B \cdot A$$


---

### Associativ
Se [[notes/Matricer#Associativ]].

$$A \cdot (B \cdot C) = (A \cdot B) \cdot C$$


---

### Resultat
Se [[notes/Matricer#Resultat]].

$$C_{m\times p} = A_{n\times m} \cdot B_{n\times p}$$


---

### Addition
Se [[notes/Matricer#Addition]].

$$A + B = B + A$$


---

### Transposition
Se [[notes/Matricer#Transposition]].

$$\left(A^T\right)^T = A$$

$$(A \cdot B)^{T} = B^{T} \cdot A^{T}$$


---

### For $2\times 2$
Se [[notes/Matricer#For $2\times 2$]].

$$M=\left( {\begin{array}{cccc} a & b \\ c & d \\ \end{array} } \right)$$

$$det(M) = detM = |M| = ad-cb$$


---

### For $3\times 3$
Se [[notes/Matricer#For $3\times 3$]].

$$det(M) = |M| = a \cdot \left|\left( {\begin{array}{cccc} e & f \\ h & i \\ \end{array} } \right)\right| - b \cdot  \left|\left( {\begin{array}{cccc} d & f \\ g & i \\ \end{array} } \right)\right| + c \cdot \left|\left( {\begin{array}{cccc} d & e \\ g & h \\ \end{array} } \right)\right|$$


---

### Integralregning
Se [[notes/Integralregning#Integralregning]].

$$\int f(x) \,dx = F(x) + k$$


---

### At finde $k$
Se [[notes/Integralregning#At finde $k$]].

$$\int f(x) = \int x^2 = F(x) = \frac{x^3}{3}+k$$

$$F(2) = 10 \Longleftrightarrow \frac{2^3}{3}+k=10 \Longleftrightarrow 8+k=10 \Longleftrightarrow k = 2$$

$$F(x)=\frac{x^3}{3}+2$$


---

### Integration i Hånden
Se [[notes/Integralregning#Integration i Hånden]].

$$\int 2x \, dx= 2 \cdot \frac{x^2}{2} = x^2 + k$$


---

### Bestemt Integrale
Se [[notes/Integralregning#Bestemt Integrale]].

$$\int_{a}^{b} f(x) \,dx = F(b) - F(a)$$


---

### Integraler og Bevægelse
Se [[notes/Integralregning#Integraler og Bevægelse]].

$$a(t)$$

$$\int a(t)\, dt = v(t) + k$$

$$\iint a(t)\,dt = \int v(t) + k\,dt = s(t) + kx + c$$


---

### Harmoniske svingninger
Se [[notes/Harmoniske svingninger#Harmoniske svingninger]].

$$x(t)= A \cdot \sin(\omega \cdot t + \phi) + d$$

$x(t)$ : Position som funktion af Tid
$A$ : Amplituden
$\omega$ : [[Vinkelfrekvens|Vinkelfrekvensen]]
$\phi$ : Faseforskydning
$d$ : Position forskydning

---

### Ekstra formler til aflæsning af transformation i x-retningen
Se [[notes/Harmoniske svingninger#Ekstra formler til aflæsning af transformation i x-retningen]].

$$T = \frac{2\pi}{\omega}$$

$$\frac{-\phi}{\omega}$$

$$sin(x) = cos(x-\frac{\pi}{2})$$


---

### Hastighed
Se [[notes/Harmoniske svingninger#Hastighed]].

$$v(t)=\omega \cdot A \cdot \cos(\omega \cdot t + \phi)$$


---

### Acceleration
Se [[notes/Harmoniske svingninger#Acceleration]].

$$a(t)=\omega^2 \cdot A \cdot \cos(\omega \cdot t + \phi)$$


---

### Med Fjeder
Se [[notes/Harmoniske svingninger#Med Fjeder]].

$$\omega=\sqrt{\frac{k}{m}} \s \text{og} \s T=2\pi \sqrt{\frac{m}{k}} \Rightarrow T\propto \sqrt{m} \s \text{og} \s f=\frac{1}{2\pi} \sqrt{\frac{k}{m}}$$


---

### Energi
Se [[notes/Harmoniske svingninger#Energi]].

$$U(x) = \frac{1}{2}kx^2$$

$$K(v)=\frac{1}{2}mv^2$$

$$E_{mek} = K(v) + U(x)= \frac{1}{2}kA^2=\frac{1}{2}m\omega^2A^2$$

$$\frac{dE_{mek}}{dt}=0$$


---

### Dæmpede Svingninger
Se [[notes/Harmoniske svingninger#Dæmpede Svingninger]].

$$\vec{F_d}=-b\vec{v}=-b \frac{d\vec{x}}{dt}$$

$\vec{F_d}$ : Dæmpningskraften
$b$ : Dæmpningskoefficienten
$$F_{res}=-F_{fjeder}-F_{d} \arrow m \cdot x'' + b x' + k \cdot x = 0$$

$b$ : Dæmpningskoefficienten
$$x(t)=A e^{-\alpha t}\sin(\omega't+\phi)$$


---

### Tvungne Svingninger
Se [[notes/Harmoniske svingninger#Tvungne Svingninger]].

$$F(t)=F_{0} \sin(\omega t)$$

$F_0$ : Den kraft der påvirker systemet
$\omega_0$ : Resonans [[Vinkelfrekvens|vinkelfrekvensen]]
$$A(\omega) = \frac{F_{0}}{\sqrt{m^{2} (\omega^{2} - \omega_0^{2})+b^2\omega^{2} }}$$

$\omega_0$ : Resonans [[Vinkelfrekvens|vinkelfrekvensen]]
$$\omega_{max} = \omega_{0}^{2} \frac{-1}{2}\left(\frac{b^{2}}{m^{2}}\right)$$


---

### Optimering
Se [[notes/Optimering#Optimering]].

$$o = 200$$

$$A = x \cdot y$$

$$o = 2x + 2y$$

$$y = 100 - x$$

$$A = x \cdot y \arrows A = x \cdot (100 - x) \arrows A(x) = - x^2 + 100x$$

$$x = A'(x) = 0 \arrows x = 50$$

$$y = A(50) = 2500$$


---

### At Gøre Prøve
Se [[notes/Differentialligninger#At Gøre Prøve]].

$$f'(x)=32e^{16x}$$

$$y = 16y  \s f'(x) = 16 \cdot f(x) \s 32e^{16x} = 16 \cdot 2e^{16x} \s 32e^{16x} = 32e^{16x}$$


---

### *Fuldstændig* og *partikulær* løsning
Se [[notes/Differentialligninger#*Fuldstændig* og *partikulær* løsning]].

$$f(x)=C \cdot e^{k \cdot x}$$


---

### Skrivemåde
Se [[notes/Differentiation af funktioner med to variable#Skrivemåde]].

$$f_{xy}'(x,y)$$

$$f_x'(x,y)=2x+1 \cdot y+ 0 + 0 = 2x+y$$

$$f_y'(x,y)=0+x+\frac{1}{3}+0=x+\frac{1}{3}$$


---

### [[Isaac Newton|Newtons]] Afkølingslov
Se [[notes/Newtons Afkølingslov#[[Isaac Newton|Newtons]] Afkølingslov]].

$$T' = \frac{dT}{dt} = -k \cdot (T-T_{omg})$$

$T_{omg}$ : Temperaturen af omgivelserne.
$k$ : [[#k -værdien|Proportionalitetskonstanten]].
$$T'(t) = -k \cdot (T(t)-T_{omg})$$

$T_{omg}$ : Temperaturen af omgivelserne.
$k$ : [[#k -værdien|Proportionalitetskonstanten]].

---

### Afkølingsloven og differentialligninger
Se [[notes/Newtons Afkølingslov#Afkølingsloven og differentialligninger]].

$$T' = -k \cdot (T-T_{omg}) \arrows T' = -k \cdot T + k \cdot T_{omg} \arrows T' = k \cdot T_{omg} -k \cdot T$$

$T_{omg}$ : Temperaturen af omgivelserne.
$k$ : [[#k -værdien|Proportionalitetskonstanten]].
$a$ : en konstant, der er lig $k$.
$b$ : en anden konstant der er lig $k \cdot T_{omg}$-
$$T = T_{omg}+C \cdot e^{-kt} \arrows T = \frac{b}{a}+C \cdot e^{-at}, \s \text{hvor } a=k \text{ og } b=k \cdot T_{omg}$$

$a$ : en konstant, der er lig $k$.
$b$ : en anden konstant der er lig $k \cdot T_{omg}$-
$k$ : [[#k -værdien|Proportionalitetskonstanten]].
$T_{omg}$ : Temperaturen af omgivelserne.
$$a = k, \s\s b = k \cdot T_{omg}$$

$b$ : en anden konstant der er lig $k \cdot T_{omg}$-
$a$ : en konstant, der er lig $k$.
$k$ : [[#k -værdien|Proportionalitetskonstanten]].
$T_{omg}$ : Temperaturen af omgivelserne.
$$T = \frac{b}{a} + C  \cdot e^{-at} = \frac{\cancel{k} \cdot T_{omg}}{\cancel{k}}+C \cdot e^{-kt} = T_{omg} + C \cdot e^{-kt}$$

$b$ : en anden konstant der er lig $k \cdot T_{omg}$-
$a$ : en konstant, der er lig $k$.
$k$ : [[#k -værdien|Proportionalitetskonstanten]].
$T_{omg}$ : Temperaturen af omgivelserne.

---

### Logistisk vækst
Se [[notes/Logistisk vækst#Logistisk vækst]].

$$y'=y \cdot (b-ay) \arrows y'=ay \cdot (M-y), \text{ hvor } M = \frac{b}{a} \arrows y' = k \cdot y \left(1+ \frac{y}{M}\right)$$

$M$ : grenseværdien/bærekapaciteten
$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}} \arrows f(x)=\frac{M}{1+C \cdot e^{-bx}}$$

$M$ : grenseværdien/bærekapaciteten
$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-bx}}, \s f(x) \ne 0$$

$$y'=y \cdot (b-ay) \arrows f'(x)=f(x) \cdot (b-a \cdot f(x))$$

$$f'(x)=f(x) \cdot b-a \cdot f(x)^2$$

$$-\frac{1}{f(x)^2} \cdot f'(x)=-\frac{1}{f(x)^{\c{2}}} \cdot \c{f(x)} \cdot b-\left(-\frac{1}{\c{f(x)^2}}\right) \cdot a \cdot \c{f(x)^2}$$

$$-\frac{1}{f(x)^2} \cdot f'(x) = -\frac{1}{f(x)} \cdot b +a \arrows -\frac{1}{f(x)^2} \cdot f'(x) = a-\frac{1}{f(x)} \cdot b$$

$$g'(x) = \left(\frac{1}{f(x)}\right)' = -\frac{1}{(f(x))^2} \cdot f'(x)$$

$$g'(x)=a-g(x) \cdot b$$

$$g(x) = \frac{a}{b} + K \cdot e^{-b \cdot x}$$

$$\frac{a}{b} + K \cdot e^{-b \cdot x} = \frac{1}{f(x)} \arrows f(x)=\frac{1}{\frac{a}{b} + K \cdot e^{-b \cdot x}}$$

$$f(x) =\frac{1 \cdot \frac{b}{a}}{\frac{\c{b}}{\c{a}} \cdot \frac{\c{a}}{\c{b}} + \frac{b}{a} \cdot K \cdot e^{-b \cdot x}} = \frac{\frac{b}{a}}{1+\frac{b}{a} \cdot K \cdot e^{-b \cdot x}}$$

$$f(x)=\frac{\frac{b}{a}}{1+C \cdot e^{-b \cdot x}}$$


---

### Bevis at $f(x)$ har to forskellige stamfunktioner: $F_1(x)$ og $F_2(x)$.
Se [[notes/Små Integrationsbeviser#Bevis at $f(x)$ har to forskellige stamfunktioner: $F_1(x)$ og $F_2(x)$.]].

$$\int f(x)\,dx = F_1(x) + k = F_2(x) + k$$

$$F_1(x) = F_2(x) \Longleftrightarrow F_1(x) - F_2(x) = 0$$

$$F_1(x) - F_2(x) = k$$

$$F_1(x) = F_2(x) + k$$


---

### Bevis for ligningen $\int k \cdot f(x)\, dx = k \cdot \int f(x)\, dx$
Se [[notes/Små Integrationsbeviser#Bevis for ligningen $\int k \cdot f(x)\, dx = k \cdot \int f(x)\, dx$]].

$$(\int k \cdot f(x)\, dx)' = (k \cdot\int f(x)\, dx)'$$

$$k \cdot f(x)\, dx = k \cdot (\int f(x)\, dx)'$$

$$k \cdot f(x)\, dx = k \cdot f(x)\, dx$$


---

### Bevis for udtrykket $\int f(x)+g(x)\,dx = \int f(x)\,dx + \int g(x)\,dx$
Se [[notes/Små Integrationsbeviser#Bevis for udtrykket $\int f(x)+g(x)\,dx = \int f(x)\,dx + \int g(x)\,dx$]].

$$(\int f(x)+g(x)\,dx)' = (\int f(x)\,dx + \int g(x)\,dx)'$$

$$(\int f(x)+g(x)\,dx)' = (\int f(x)\,dx)' + (\int g(x)\,dx)'$$

$$f(x)+g(x) = f(x) + g(x)$$


---

### Cirklens Ligning
Se [[notes/Cirklens Ligning#Cirklens Ligning]].

$$\sqrt{(x-x_0)^2 + (y-y_0)^2} = r$$

$$(x-x_0)^2 + (y-y_0)^2 = r^2$$


---

### Stationære punkter
Se [[notes/Stationære punkter#Stationære punkter]].

$$\nabla f(x_0,y_0)=\v{0}{0}$$


---

### Linjens Ligningning
Se [[notes/Linjer og Vektorer i 2D#Linjens Ligningning]].

$$p = (x_0,y_y)$$

$$a \cdot (x-x_0) + b \cdot (y - y_0) = 0$$

$$a \cdot x + b \cdot y + c = 0$$

$$c = - (a \cdot x_0 + b \cdot y_0)$$


---

### Parameterfremstilling
Se [[notes/Linjer og Vektorer i 2D#Parameterfremstilling]].

$$x(t) = x_0 + t \cdot r_1$$

$$y(t) = y_0 + t \cdot r_2$$

$$\v{r_1}{r_2} = \vec{r}$$


---

### Vinklen mellem vektorer
Se [[notes/Linjer og Vektorer i 2D#Vinklen mellem vektorer]].

$$cos(v) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$


---

### Afstanden til et punkt fra en linje (uden at kende punktet på linjen).
Se [[notes/Linjer og Vektorer i 2D#Afstanden til et punkt fra en linje (uden at kende punktet på linjen).]].

$$y = a \cdot x + b$$


---

### Monotoniforhold
Se [[notes/Monotoniforhold#Monotoniforhold]].

$$f'(x) = 0$$

$$f'(x) > 0$$

$$f'(x) < 0$$


---

### Trin 1
Se [[notes/Tretrinsraketten#Trin 1]].

$$f(x_0 + h) - f(x_0) = 3 (x_0+h)^2-3x_0^2 = 3 \cdot (h^2 + 2 \cdot h \cdot x_0 + x_0^2)-3x_0^2 = 3 \cdot h^2 + 6 \cdot h \cdot x_0 + \bcancel{3 \cdot x_0^2} - \bcancel{3 \cdot x_0^2}$$

$$f(x_0 + h) - f(x_0) = 3h^2 + 6 h x$$


---

### Trin 2
Se [[notes/Tretrinsraketten#Trin 2]].

$$\frac{f(x_0 + h) - f(x_0)}{h} = \frac{3h^{\bcancel{2}} + 6 \bcancel{h} x}{\bcancel{h}} = 6x + 3h$$


---

### Trin 3
Se [[notes/Tretrinsraketten#Trin 3]].

$$\lim_{h\to 0} (6x+3h)$$

$$f'(x) = 6x$$


---

### Normalform
Se [[notes/Ellipse#Normalform]].

$$\frac{x^2}{a^2}+\frac{y^2}{b^2} = 1$$

$a$ : halvdelen af storaksen
$b$ : halvdelen af lilleaksen

---

### Formel
Se [[notes/Ellipse#Formel]].

$$|\vec{PF_1}| + |\vec{PF_2}| = k$$


---

### Brændpunkter
Se [[notes/Ellipse#Brændpunkter]].

$$|\vec{F_1 T}| = |\vec{F_2 T}| = \frac{k}{2}$$


---

### Ellipser som [[Vektorfunktioner]]
Se [[notes/Ellipse#Ellipser som [[Vektorfunktioner]]]].

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \s \Rightarrow \s \v{x}{y}=\v{a \cdot cos(t)}{b \cdot sin(t)}, \:\:\text{hvor}\: 0 \leq t \leq 2\pi$$


---

### [[Tangent]]
Se [[notes/Ellipse#[[Tangent]]]].

$$\frac{x_0x}{a^2}+\frac{y_0y}{b^2}=1$$


---

### Areal
Se [[notes/Ellipse#Areal]].

$$A=\pi \cdot a \cdot b$$


---

### Det Komplekse Plan
Se [[notes/Det Komplekse Plan#Det Komplekse Plan]].

$$\C = \{x + yi : x,y \in \R\}$$


---

### Linært Afhængige Vektorer
Se [[notes/Linært Afhængige Vektorer#Linært Afhængige Vektorer]].

$$\vec{c}=k_{1}\cdot \vec{a}+k_{2}\cdot \vec{b}$$


---

### Sætning
Se [[notes/Linært Afhængige Vektorer#Sætning]].

$$k_{1}\cdot \vec{a_{1}} + k_{2}\cdot \vec{a_{2}}+\dots+k_{n}\cdot \vec{a_{n}} = \vec{0}$$


---

### Vektorfunktioner
Se [[notes/Vektorfunktioner#Vektorfunktioner]].

$$\vec{f}(t)=\v{x(t)}{y(t)}$$


---

### Andenordens inhomogene differentialligninger
Se [[notes/Andenordens inhomogene differentialligninger#Andenordens inhomogene differentialligninger]].

$$ay''+by'+cy=f(x)$$

$a, b, c$ : Konstanter.

---

### Find Løsningen!
Se [[notes/Andenordens inhomogene differentialligninger#Find Løsningen!]].

$$ay''+by'+cy=0$$

$$y=y_h+y_p$$


---

### Cosinus og Sinus
Se [[notes/Trigonometri#Cosinus og Sinus]].

$$\sin(\theta) = \frac{\text{Modstående}}{\text{Hypotenusen}}$$

$$\cos(\theta) = \frac{\text{Hoslæggende}}{\text{Hypotenusen}}$$

$$\tan(\theta)= \frac{\text{Modstående}}{\text{Hoslæggende}} = \frac{\sin(\theta)}{\cos{(\theta)}}$$


---

### Flere Relationer 
Se [[notes/Trigonometri#Flere Relationer ]].

$$\sin(\theta) = \sin(\pi - \theta)$$

$$\cos(\theta) = \sin\left(\theta + \frac{\pi}{2}\right)$$

$$\cos(\theta) = \cos(-\theta)$$

$$\sin(-\theta) = -\sin(\theta)$$


---

### Den med Tangens
Se [[notes/Trigonometri#Den med Tangens]].

$$\tan^{-1}(x)= \int\frac{1}{1+y^2}dy$$


---

### Additionsformler
Se [[notes/Trigonometri#Additionsformler]].

$$\cos(x+y) = \cos x \cdot \cos y - \sin x \cdot \sin y$$

$x$ : En konstant.
$y$ : En anden konstant.
$$\sin(x+y) = \cos x \cdot \sin y - \sin x \cdot \cos y$$

$x$ : En konstant.
$y$ : En anden konstant.

---

### Grundrelationen (Idiot-reglen)
Se [[notes/Trigonometri#Grundrelationen (Idiot-reglen)]].

$$\cos(\theta)^2 + \sin(\theta)^2 = 1$$


---

### Pythagoras Læresætning
Se [[notes/Trigonometri#Pythagoras Læresætning]].

$$a^2 + b^2 = c^2$$

$a$ : Den ene katete.
$b$ : Den anden katete.
$c$ : Hypotenusen.

---

### Vinkel Halvering
Se [[notes/Trigonometri#Vinkel Halvering]].

$$\cos^2(\theta) = \frac{\cos(2\theta)-1}{2}$$


---

### Inverse Trig Funktioner
Se [[notes/Trigonometri#Inverse Trig Funktioner]].

$$\arctan(x)=x- \frac{x^3}{3}- \frac{x^5}{5}-\frac{x^7}{7}-\frac{x^9}{9}\dots$$


---

### Grænser
Se [[notes/Grænser#Grænser]].

$$\lim_{x\rightarrow \infty}\left(f(x)\right) = L$$


---

### L'Hopital-reglen
Se [[notes/Grænser#L'Hopital-reglen]].

$$\lim_{x\rightarrow g}(f(x)) = \lim_{x\rightarrow g}(g(x)) = 0$$

$$\lim_{x\rightarrow g}(f(x)) = \lim_{x\rightarrow g}(g(x)) = \pm\infty$$

$$\lim_{x\rightarrow g}\left( \frac{f(x)}{g(x)} \right) = \lim_{x\rightarrow g}\left( \frac{f'(x)}{g'(x)} \right)$$


---

### Halveringtid
Se [[notes/Halveringtid#Halveringtid]].

$$N = N_0 \cdot (1/2)^{\frac{t}{T_{\frac{1}{2}}}}$$

$$A = A_0 \cdot (1/2)^{\frac{t}{T_{\frac{1}{2}}}}$$


---

### Punkter
Se [[notes/n-Space#Punkter]].

$$(x_1, x_2, x_3, \dots, x_n)$$


---

### Længde mellem punkter
Se [[notes/n-Space#Længde mellem punkter]].

$$L =\sqrt{(y_1 - x_1)^2 + (y_2 - x_2)^2 + \dots + (y_n-x_n)^n}$$

$L$ : Længden mellem punkterne
$y_{1\dots n}$ : Det $n$'te koordinat i $y$-punktet.

---

### Rotationsmatricer
Se [[notes/Rotationsmatricer#Rotationsmatricer]].

$$R_{\theta}= \left( {\begin{array}{cccc} \cos{\theta} & -\sin{\theta} \\ \sin\theta & \cos{\theta} \\ \end{array} } \right)$$


---

### Rotation af Punkt
Se [[notes/Rotationsmatricer#Rotation af Punkt]].

$$R_{\theta} \bullet p$$


---

### Normalfordelingen
Se [[notes/Normalfordelingen#Normalfordelingen]].

$$X\sim N(\mu,\sigma)$$

$$f(x) = \frac{1}{\sigma \cdot \sqrt{2\pi}} \cdot e^{-\frac{1}{2} \cdot \left( \frac{x \cdot \mu}{\sigma}  \right)^2}$$


---

### Fordelingsfunktionen (sumkurve):
Se [[notes/Normalfordelingen#Fordelingsfunktionen (sumkurve):]].

$$F(x) = \int f(x)$$


---

### Vektorer
Se [[notes/Vektorer#Vektorer]].

$$længde\ af\ vektor = \left| \overrightarrow{a} \right|,\ \ x^{2} + y^{2} = {|\overrightarrow{a}|}^{2}$$


---

### Prik produkt
Se [[notes/Vektorer#Prik produkt]].

$$\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2  \cdot b_2 + \dots = \sum_{i=1}^{n}a_i b_i$$


---

### Krydsprodukt
Se [[notes/Vektorer#Krydsprodukt]].

$$\vt{a_1}{a_2}{a_3} \times \vt{b_1}{b_2}{b_3} = \vt{a_2b_3-a_3b_2}{-(a_1b_3 - a_3b_1)}{a_1b_2-a_2b_1}$$

$$\vec{u} \times \vec{u} = \vec{0} \s \text{fordi den er parallel med sig selv}$$

$$\vec{u} \times \vec{v} = -\vec{v} \times \vec{u}$$


---

### Længden af et krydsprodukt
Se [[notes/Vektorer#Længden af et krydsprodukt]].

$$|\vec{u} \times \vec{v}| = |\vec{u}||\vec{v}| \cdot \sin \theta$$

$\theta$ : Vinkel mellem vektorene.

---

### Angle between vectors
Se [[notes/Vektorer#Angle between vectors]].

$$\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} \arrows \vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}| \cdot \cos \theta$$


---

### Length
Se [[notes/Vektorer#Length]].

$$|\vec{a}| = \sqrt{\sum _{i=1}^n a_i^2}$$


---

### Scalar Projektion
Se [[notes/Vektorer#Scalar Projektion]].

$$s = \vec{u} \cdot \frac{\vec{v}}{|\vec{v}|} = |\vec{u} | \cdot \cos \theta $$

$\theta$ : angle between $b$ and $a$

---

### Vektor projektion
Se [[notes/Vektorer#Vektor projektion]].

$$\vec{u}_{\vec{v}} = s \cdot \hat{\vec{v}} = \left(\vec{u} \cdot \frac{\vec{v}}{|\vec{v}|}\right) \cdot \frac{\vec{v}}{|\vec{v}|}$$


---

### 1. Generel løsningsformel
Se [[notes/Linære førsteordensdifferentialligninger#1. Generel løsningsformel]].

$$y' + p(x)  \cdot y = q(x) \arrows y' = q(x) - p(x) \cdot y \arrows \frac{dy}{dx}+p(x) \cdot y=q(x)$$

$p(x)$ : en funktion af $x$
$q(x)$ : en anden funktion af $x$
$P(x)$ : **en** stamfunktion for $p(x)$
$$f(x) = e^{-P(x)} \cdot \int e^{P(x)} \cdot q(x)dx$$

$P(x)$ : **en** stamfunktion for $p(x)$
$q(x)$ : en anden funktion af $x$
$$f(x) = e^{-P(x)}$$

$P(x)$ : **en** stamfunktion for $p(x)$
$$y' = \frac{1}{x} \cdot y = 5x^3$$

$$A(x) = \int \frac{1}{x}dx = ln(x)$$

$$f(x) = e^{-ln(x)} \cdot \int e^{ln(x)} \cdot 5x^3dx$$

$$f(x) = \frac{1}{x} \cdot \int e^{ln(x)} \cdot 5x^3dx$$

$$f(x) = \frac{1}{x} \cdot \int x \cdot 5x^3dx \Arrows f(x) = \frac{1}{x} \cdot \int 5x^4dx$$

$$\frac{1}{x}  \cdot (x^5 + k) \s = \s x^4 + \frac{k}{x}$$

$$f(x) = x^4 + \frac{k}{x}$$

$$\frac{dy}{dx} - \frac{2}{x} \cdot y = e^x$$

$$y' = sin(x) - 5y$$


---

### 2. Løsningsformel
Se [[notes/Linære førsteordensdifferentialligninger#2. Løsningsformel]].

$$y' = k \cdot y \arrows f(x)=C \cdot e^{k \cdot x}$$


---

### $k$-værdien
Se [[notes/Linære førsteordensdifferentialligninger#$k$-værdien]].

$$\frac{y'}{y} = k$$

$$\frac{s'(3)}{s(3)} = 0.25 \arrows \frac{s'(t)}{s(t)} = 0.25$$

$$y=8x$$

$$y=8x+c$$

$$5=8 \cdot (-2) + c \s 5=-16 + c \s 21=c $$

$$y=8x+21$$

$$k = 3,5$$

$$f(x) = C \cdot e^{3,5x}$$

$$f(x) = C \cdot e^{-0.12x}$$

$$20 = C \cdot e^{-0.12 (0)} = C \cdot e^0 = C \s \Leftrightarrow \s C = 20$$

$$f(x) = 20 \cdot e^{-0.12x}$$


---

### 3. Løsningsformel ([[Newtons Afkølingslov]])
Se [[notes/Linære førsteordensdifferentialligninger#3. Løsningsformel ([[Newtons Afkølingslov]])]].

$$y'=b-a \cdot y \Arrows f(x) =  \frac{b}{a} + C  \cdot e^{-ax}, \s a \neq0$$

$a$ : En konstant.
$b$ : En anden konstant.
$C$ : Integrationskonstanten.
$$\lim\limits_{x \to \infty}(f(x)) =  \frac{b}{a}, \s 0<a$$

$b$ : En anden konstant.
$a$ : En konstant.
$$\lim\limits_{x \to -\infty}(f(x)) =  \frac{b}{a}, \s a<0$$

$b$ : En anden konstant.
$a$ : En konstant.
$$f'(x) = b-a \cdot f(x)$$

$b$ : En anden konstant.
$a$ : En konstant.
$$f'(x) = -a \left(f(x)-\frac{b}{a} \right)$$

$b$ : En anden konstant.
$a$ : En konstant.
$$g(x) = f(x) - \frac{b}{a}, \s \text{der kan differentieres til } f'(x)$$

$b$ : En anden konstant.
$a$ : En konstant.
$$g'(x) = -a \cdot g(x)$$

$a$ : En konstant.
$$g(x) = f(x) - \frac{b}{a}$$

$b$ : En anden konstant.
$a$ : En konstant.
$$C \cdot e^{-ax} = f(x) - \frac{b}{a}$$

$C$ : Integrationskonstanten.
$b$ : En anden konstant.
$a$ : En konstant.
$$f(x) = \frac{b}{a} + C \cdot e^{-ax}$$

$C$ : Integrationskonstanten.
$b$ : En anden konstant.
$a$ : En konstant.

---

### 4. løsningsformel - Separation af de variable
Se [[notes/Linære førsteordensdifferentialligninger#4. løsningsformel - Separation af de variable]].

$$y'=e^{-y} \cdot 2x \arrows dy = \frac{1}{e^y} \cdot 2x \cdot dx \arrows e^y \cdot dy = 2x \cdot dx$$

$$\int e^y \cdot dy = \int 2x \cdot dx \arrows e^y + k_1 = x^2 + k_2 \arrows e^y = x^2+k_1-k_2$$

$$c=k_1-k_2$$

$$e^y = x^2+c = ln(e^y) = ln(x^2+c) \arrows y = ln(x^2+c)$$


---

### Snitkurver
Se [[notes/Snitkurver#Snitkurver]].

$$f(x,y) = x^2+x \cdot y-8$$

$$f(3,y)=3^2+3y-8=3y+1$$

$$z=3y+1$$


---

### Begyndelsesværdier
Se [[notes/Andenordensdifferentialligninger#Begyndelsesværdier]].

$$y'' + y' - 2y=0, \s y(0),\s y'(0)=-1$$

$$r^{2}+r-2=0 \arrow = \frac{-1\pm\sqrt{1+8}}{2}=\begin{cases} r_1=1\\ r_2=-2 \end{cases}$$

$$y=A \cdot e^{x}+B\cdot e^{-2x}$$

$$y'=A \cdot e^{x} -B \cdot 2 \cdot e^{-2x}$$

$$(A+B)-(A-2B)=2-(-1) \arrow A=1,\s B=1$$


---

### Middelværdisætningen
Se [[notes/Middelværdisætningen#Middelværdisætningen]].

$$f'(c)= \frac{f(b)-f(a)}{b-a}$$


---

### Formel
Se [[notes/Omdrejningslegne#Formel]].

$$V=\pi \cdot \int_{a}^{b} (f(x))^2 \,dx$$


---

### Seperable Diff-ligninger
Se [[notes/Førsteordensdifferentialligninger#Seperable Diff-ligninger]].

$$\frac{dy}{dx} = h(x,y)$$

$$h(x,y)=g(y) \cdot f(x)$$

$$\frac{dy}{dx} =g(y) \cdot f(x) \arrows \frac{1}{g(y)} \frac{dy}{dx} = f(x)$$

$$\int \frac{1}{g(y)} \cdot \frac{dy}{\c{dx}} \cdot  \c{dx}=\int f(x)dx$$

$$\int f(x)= \int \frac{1}{g(y)}dy$$

$$\frac{dy}{dx} = \frac{x}{y}$$

$$y \cdot dy= x \cdot dx$$

$$\int y \cdot dy= \int x \cdot dx \arrows \frac{1}{2}y^2= \frac{1}{2}x^2+c$$

$$y^2=x^2+2c \arrows y=\pm \sqrt{x^2+2c}$$


---

### Bevis for den Gennerelle Løsningsformel til [[Linære førsteordensdifferentialligninger]]
Se [[notes/Bevis for den Gennerelle Løsningsformel til Linære Førsteordensdifferentialligninger#Bevis for den Gennerelle Løsningsformel til [[Linære førsteordensdifferentialligninger]]]].

$$f'(x) \cdot e^{A(x)} + a(x) \cdot f(x) \cdot e^{A(x)} = b(x) \cdot e^{A(x)}$$

$$\left(g(x)  \cdot  e^{A(x)}\right)' = g'(x) \cdot e^{A(x)} + g(x) \cdot e^{A(x)} \cdot a(x)$$

$$\left(f(x)  \cdot  e^{A(x)}\right)' = b(x) \cdot e^{A(x)}$$

$$\int  \left(f(x)  \cdot  e^{A(x)}\right)'dx = \int b(x) \cdot e^{A(x)}dx \arrows f(x)  \cdot  e^{A(x)} = \int b(x) \cdot e^{A(x)}dx$$

$$f(x) = \frac{1}{e^{A(x)}} \cdot \int b(x) \cdot e^{A(x)}dx$$

$$f(x) = e^{-A(x)} \cdot \int b(x) \cdot e^{A(x)}dx$$


---

### Koordinatsystem og Flader
Se [[notes/Koordinatsystem og Flader#Koordinatsystem og Flader]].

$$a = \sqrt{x^2 + y^2 + z^2}$$


---

### Længde mellem punkter
Se [[notes/Koordinatsystem og Flader#Længde mellem punkter]].

$$P_1 = (x_1, y_1,z_1) \s P_2= (x_2,y_2,z_2)$$

$r$ : Længde mellem punkterne.
$$r = \sqrt{|x_2-x_1|^2 + |y_2-y_1|^2 + |z_2-z_1|^2}$$

$r$ : Længde mellem punkterne.

---

### Fladens Ligning
Se [[notes/Koordinatsystem og Flader#Fladens Ligning]].

$$\vec{n} \cdot (P-P_0) = 0 \arrows \vt{A}{B}{C} \cdot \vt{x-x_0}{y-y_0}{z-z_0} = 0$$

$$Ax + By + Cz = D \s \text{hvor} \s D=Ax_0+By_0+Cz_0$$


---

### Flere Trigonometriregler
Se [[notes/Differentialregning Regneregler#Flere Trigonometriregler]].

$$\arcsin'(x) = \frac{1}{\sqrt{1-x^2}}$$


---

### Funktioner af to Variable
Se [[notes/Funktioner af to Variable#Funktioner af to Variable]].

$$f(x,y)$$

$$f(x,y)=z=\sqrt{x} \cdot y$$

$$V=h \cdot b^2$$

$$\Updownarrow$$

$$V(h,b)=h \cdot b^2$$


---

### Definitionsmængde
Se [[notes/Funktioner af to Variable#Definitionsmængde]].

$$f(x,y)=x \cdot y$$

$$Dm(f) = \R \times \R$$

$$g(x,y)=\sqrt{x} \cdot y$$

$$dm(d)=[0;\infty[ \:\times\: \R$$


---

### Logaritmer
Se [[notes/Logaritmer#Logaritmer]].

$$\log_n(x) = y \arrows n^y = x$$


---

### Regneregler
Se [[notes/Logaritmer#Regneregler]].

$$\log(a) + \log(b) = \log(a \cdot b)$$


---

### Skift base
Se [[notes/Logaritmer#Skift base]].

$$\log_a(n) = \frac{\log_b(n)}{\log_b(a)}$$


---

### Den Naturlige logatitme
Se [[notes/Logaritmer#Den Naturlige logatitme]].

$$ln(x) = a \arrows e^a=x$$


---

### Den Naturlige [[Eksponentielle Funktioner|Eksponentielle Funktion]]
Se [[notes/Logaritmer#Den Naturlige [[Eksponentielle Funktioner|Eksponentielle Funktion]]]].

$$e^x = \frac{x^{0!}}{0!} + \frac{x^{1!}}{1!} + \frac{x^{2!}}{2!} + \frac{x^{3!}}{3!} \dots \frac{x^{n!}}{n!}$$

$$(e^x)' = e^x$$


---

### Komplekse Tal
Se [[notes/Komplekse Tal#Komplekse Tal]].

$$w = a + ib, \s i^2 = -1$$

$$Re(w) = Re(a+ib)= a, \s Im(w) = Im(a+ib)  = b$$

$$x = \frac{-b \pm i \sqrt{-d}}{2a}$$

$$2z^2 + 4z + 10 = 0$$

$$d = b^2 - 4ac= -64$$

$$x = \frac{-b \pm i \sqrt{-(d)}}{2a} = -1 \pm 2i$$


---

### Addition
Se [[notes/Komplekse Tal#Addition]].

$$z_1 + z_2 = a + ib + c-id = a+c+i(b+d)$$


---

### Subtraktion
Se [[notes/Komplekse Tal#Subtraktion]].

$$z_1 - z_2 = a + ib - c-id = a-c+i(b-d)$$


---

### Multiplikation
Se [[notes/Komplekse Tal#Multiplikation]].

$$z_1 \cdot  z_2 = (a+ib)(c-id) = ac - iad + ibc + - i^2bd$$

$$ = ac + i^2bd + i(ac+bc)$$

$$z_1 \cdot z_2 = ac - bd + i(ac+bc)$$


---

### Multiplikation med [[#den kompleks konjugerede]]
Se [[notes/Komplekse Tal#Multiplikation med [[#den kompleks konjugerede]]]].

$$z_1 \cdot  \bar{z_1} = (a+ib)(a-ib) = a^2 - i^2b^2 - \c{aib} + \c{aib} = a^2 + b^2$$


---

### Division
Se [[notes/Komplekse Tal#Division]].

$$\frac{z_1}{z_2} = \frac{a + ib}{c + id}$$

$$\frac{(a+ib)(c-id)}{(c+id)(c-id)}$$

$$= \frac{ac -i^2bd + i(ab-ad)}{c^2-d^2} = \frac{ac+bd+i(bc+ad)}{c^2 + d^2}$$


---

### Polær Form
Se [[notes/Komplekse Tal#Polær Form]].

$$z=M\cos(\theta) + iM\sin(\theta)$$

$$z=M \cdot e^{i\theta}$$

$$z=M\angle\theta$$


---

### Modulus
Se [[notes/Komplekse Tal#Modulus]].

$$|z| = \sqrt{a^2 + b^2}$$


---

### Argumentet
Se [[notes/Komplekse Tal#Argumentet]].

$$arg(z) = \theta$$

$$arg(z)= \theta =\tan^{-1}\left(\frac{Im(z)}{Re(z)}\right) + p\pi, \s p \in \{-1,0,1\}$$

$$z_1 \cdot z_2 = M_1 \cdot  e^{i\theta_1} \cdot  M_2 \cdot  e^{i\theta_2} = M_1 \cdot  M_2 \cdot  e^{i(\theta_1 + \theta_2)}$$

$$M_1(\cos\theta_1 + i\sin\theta_1) \cdot M_2(\cos\theta_2 + i \sin\theta_2)$$

$$\Updownarrow$$

$$M_1M_2(\cos\theta_1 \cos\theta_2 - \sin \theta_1 \sin\theta_2 + i(\sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2))$$

$$\Updownarrow$$

$$M_1M_2(\cos(\theta_1 + \theta_2)+i \sin(\theta_1 + \theta_2))$$

$$\frac{z_1}{z_2} = \frac{M_1 \cdot e^{i\theta_1}}{M_2 \cdot e^{i\theta_2}} = \frac{M_1}{M_2} \cdot e^{i(\theta_1-\theta_2)}$$

$$z=M \cdot e^{i\theta}$$

$$z^n = (M \cdot e^\theta)^n = M^n \cdot e^{i\theta \cdot n} = M^n (\cos(\theta n) + i\sin(\theta n))$$


---

### de Moivre's Formel
Se [[notes/Komplekse Tal#de Moivre's Formel]].

$$n = 1,\s z = \cos(\theta) + i \sin(\theta)$$

$$z^1= (\cos(\theta) + i \sin(\theta))^1 \arrow \text{sandt!}$$

$$z^k= (\cos(\theta) + i \sin(\theta))^k \arrow \text{Antages sandt}$$

$$(\cos(\theta) + i \sin(\theta))^{k+1} \s=\s (\cos(\theta) + i \sin(\theta))^{k} \cdot (\cos(\theta) + i \sin(\theta))^{1}$$

$$= (\cos(k\theta) + \sin(k\theta)) \cdot (\cos(\theta) + i \sin(\theta))$$

$$= \cos(k\theta) \cdot \cos(\theta) - \sin(k\theta) \cdot \sin(\theta) + i(\cos(k\theta) \cdot \sin(\theta) + \sin(k\theta) \cdot \cos(\theta))$$

$$\cos(k\theta+\theta)+i\sin(k\theta + \theta) \s=\s \cos((k+1)\theta) + i\sin((k+1)\theta)$$

$$\cos(n\theta) + i\sin(n\theta)$$


---

### For rationelle tal
Se [[notes/Komplekse Tal#For rationelle tal]].

$$z^{\frac{p}{q}} = r^{\frac{p}{q}}\cdot (\cos((\frac{p}{q} \cdot \theta) + i \sin(\frac{p}{q} \cdot \theta))$$


---

### Komplekse løsninger
Se [[notes/Komplekse Tal#Komplekse løsninger]].

$$z^2 = 4$$

$$|z^2| = |4| = \sqrt{4^2 + 0^2} = 4$$

$$arg(z^2) = arg(4) = \tan^{-1}\left(\frac{0}{4}\right) = 0$$

$$z^2 = |z^2| (\cos(arg(z^2) + 2\pi p) + i\sin(arg(z^2)+2\pi p), \s p \in \Z$$

$$z^2 = 4(\cos(0 + 2\pi p) + i\sin(0+2\pi p), \s p \in \Z$$

$$z^n = r^n (cos(n\theta) + i \sin(n\theta)) \arrows z^2 = r^2 (cos(2\theta) + i \sin(2\theta))$$

$$r^2 = 4 \arrow r = 2$$

$$2\pi p = 2\theta \arrow \theta = \pi p$$

$$p = 0: \s \theta_1 = \pi \cdot 0 = 0$$

$$p = 1: \s \theta_2 = \pi \cdot 1 = \pi$$

$$z = \cos(\theta) + i\sin(\theta)$$

$$z + \frac{1}{z} = z + z^{-1} = \cos(\theta) + {i\sin(\theta)} + \cos({-\theta}) + i\sin(-\theta) $$

$$\cos(\theta) + \c{i\sin(\theta)} + \cos({-\theta}) \c{- i\sin(\theta)} $$

$$z + \frac{1}{z} = 2\cos{\theta}$$


---

### Bevis for [[Linjer og Vektorer i 2D#Linjens Ligningning|Linjens Ligning]]
Se [[notes/Bevis for Linjens Ligning#Bevis for [[Linjer og Vektorer i 2D#Linjens Ligningning|Linjens Ligning]]]].

$$\vec{n} \cdot \vec{p_0p} = 0$$

$$a \cdot (x-x_0) + b \cdot (y - y_0) = 0$$


---

### Integration med Substidution
Se [[notes/Integration med Substidution#Integration med Substidution]].

$$\int sin(2t + \pi) dt$$

$$u = 2t + \pi$$

$$u' = \frac{du}{dt} = 2$$

$$dt = \frac{1}{2}du$$

$$\int sin(u) \cdot \frac{1}{2}du \arrows \frac{1}{2} \cdot \int sin(u) du \arrows \frac{1}{2} \cdot (-cos(u)+k)$$

$$\frac{1}{2} \cdot (-cos(2t+\pi)+k)\s = \s \frac{-cos(2t+\pi)+k}{2} $$


---

### Eksponentielle Funktioner
Se [[notes/Eksponentielle Funktioner#Eksponentielle Funktioner]].

$$f(x) = a \cdot e^{k \cdot x}$$

$a$ : Skæring med $y$-aksen
$$y' = k \cdot y$$


---

### Formel for $a$
Se [[notes/Eksponentielle Funktioner#Formel for $a$]].

$$a = \sqrt[x_2-x_1]{\frac{y_2}{y_1}}$$


---

### Gym form
Se [[notes/Eksponentielle Funktioner#Gym form]].

$$f(x)=b \cdot a^x$$

$b$ : Skæring med $y$-aksen
$a$ : Faktor for hvor hurtigt grftager

---

### En-en-tydig Funktion
Se [[notes/En-en-tydig Funktion#En-en-tydig Funktion]].

$$x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)$$


---

### Konnektiver
Se [[notes/Beviser#Konnektiver]].

$$p \land q, \s \text{"og/konjunktion"}$$

$$p \:\lor\: q, \s \text{"eller/disjunktion"}$$

$$p\Rightarrow q,\s \text{"medfører/implikation"}$$

$$p \arrows q, \s\text{"biimplikation"}$$

$$\lnot p, \s\text{"ikke/negation"}$$


---

### Udsagn
Se [[notes/Beviser#Udsagn]].

$$5=6$$

$$4>3$$

$$10 \cdot 4 = 20  \cdot 2 \arrows 1=1$$


---

### Prædikater
Se [[notes/Beviser#Prædikater]].

$$p(x): x < 10$$


---

### Kvantorer
Se [[notes/Beviser#Kvantorer]].

$$\exists x \in \R: p(x)$$


---

### Modstridsbevis
Se [[notes/Beviser#Modstridsbevis]].

$$\sqrt{2} = \frac{m}{n} \arrows 2 = \frac{m^2}{n^2} \arrows 2n^2 = m^2$$

$$2n^2=(2p)^2 = 4p^2$$


---

### Linarisering
Se [[notes/Linarisering#Linarisering]].

$$L(x) = f(a)+f'(a) \cdot (x-a)$$

$a$ : $x$-værdien i punktet 

---

### Sekantens hældning (differenskvotienten)
Se [[notes/Sekant#Sekantens hældning (differenskvotienten)]].

$$a=\frac{y_2-y_1}{x_2-x_1} = \frac{f(x_0+h)-f(x_0)}{\c{x_0} + h - \c{x_0}} = \frac{f(x_0+h)-f(x_0)}{h}$$


---

### Sfæriske Koordinater
Se [[notes/Sfæriske Koordinater#Sfæriske Koordinater]].

$$P = (R, \phi, \theta)$$

$R$ : Længden fra orego til $P$
$\phi$ : Vinkel opad 
$\theta$ : Vinklen fra $x$-aksen i $xy$-planen

---

### Oversæt til Cartesiske koordinater
Se [[notes/Sfæriske Koordinater#Oversæt til Cartesiske koordinater]].

$$R^2 = x^2 + y^2 + z^2 = r^2+z^2$$

$$r = \sqrt{x^2 + y^2} = R \cdot  \sin \phi$$

$$\tan \phi = \frac{r}{z} = \frac{\sqrt{x^2 + y^2}}{z} \s \text{og} \s \tan \theta =\frac{y}{x}$$


---

### Dæmpede Svingninger
Se [[notes/Dæmpede Svingninger - Differentialligning#Dæmpede Svingninger]].

$$a \cdot y'' + b \cdot y' + c \cdot y = 0 \arrows (a \cdot r^2 + br + c) \cdot e^{rt} = 0$$

$$a \cdot y'' + b \cdot y' + c \cdot y = 0$$

$$a \cdot r^2 \cdot e ^{rt} + b \cdot r \cdot e^{rt} + c \cdot e^{rt} = 0$$

$$(a \cdot r^2 + br + c) \cdot e^{rt} = 0$$


---

### Rødder, dæmpningstype og løsninger
Se [[notes/Dæmpede Svingninger - Differentialligning#Rødder, dæmpningstype og løsninger]].

$$y(x) = A \cdot e^{r_1x} + B \cdot e^{r_2x}$$

$k$ : det reelle komponent af $r$.
$w$ : det imaginære komponent af $r$.
$r$ : rod/rødder.
$B$ : Den anden integrationskonstant.
$A$ : Den første integrationskonstant.
$$y(x) = A \cdot e^{rx} + B \cdot x \cdot e^{rx}$$

$k$ : det reelle komponent af $r$.
$w$ : det imaginære komponent af $r$.
$r$ : rod/rødder.
$B$ : Den anden integrationskonstant.
$A$ : Den første integrationskonstant.
$$y(x) = A \cdot e^{kx} \cdot \cos(\omega x) + B \cdot  e^{kx} \cdot \sin(\omega x)$$

$k$ : det reelle komponent af $r$.
$w$ : det imaginære komponent af $r$.
$B$ : Den anden integrationskonstant.
$A$ : Den første integrationskonstant.
$$r = k \pm \omega i$$

$k$ : det reelle komponent af $r$.
$w$ : det imaginære komponent af $r$.
$r$ : rod/rødder.