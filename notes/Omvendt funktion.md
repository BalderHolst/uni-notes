# Omvendt funktion (inverse funktion)
En funktion der gør det modsatte af en anden funktion

Den omvendte funktion til $f(x)$ kaldes $f^{-1}(x)$ .

Altså:
$$f(f^{-1}(x))=f^{-1}(f(x))=x$$

Den inverse funktion kan også findes ved at spejle grafen i $y=x$.


>[!Note]- Eksempler
>
>$$f(x) = e^x \: \Rightarrow \: f^{-1}(x) = ln(x)$$
>$$f(x)=\sqrt{x} \:\Rightarrow\: f^{-1}(x)=x^2$$
>

### Hvornår *har* en funktion en omvendt funktion?
Det kan den hvis den er *injektiv*, altså at hver $y$-værdi *ikke* har mere end *en* $x$-værdi


### Hvordan *finder* man en omvendt funktion?
1. Byt $x$ og $y$
2. Isoler $y$
3. (check at $f(f^{-1}(x))=x$)


>[!Note]- Eksempel
>
>eks.
>$$f(x)=y=2x+3$$
>Bytter om på $x$ og $y$
>$$x=2y+3$$
>Vi kan nu isolere $y$
>$$\frac{x-3}{2}=y$$
>Altså er dette den omvendte funktion:
>$$f^{-1}(x)=\frac{x-3}{2}$$
>
>

### Differentiering med omvendte funktioner
$$\frac{d}{dx}(x^{x+\sin(x)})$$
$$x = e^{\ln (x)} \arrow \frac{d}{dx}(e^{ln(x)})^{x+sin(x)})$$
$$a^{b^c} = a^{a \cdot c} \arrow \frac{d}{dx}(e^{ln(x) \cdot (x + sin(x))})$$
Bruger kædereglen
$$\frac{d}{dx}(e^{f(x)}) = e^{f(x)} \cdot f'(x) \arrow e^{ln(x) \cdot (x+sin(x))} \cdot \frac{d}{dx}(ln(x) \cdot (x+sin(x))$$
$$= x^{x+sin(x)} \cdot (\frac{1}{x} \cdot (x+sin(x)+ln(x)\cdot (1+cos(x))))$$

---
#matematik #funktioner