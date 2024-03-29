## Differentialregning - Basis

### Definition af et Differentiale

![Illustration af variabler|center|300](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.webmatematik.dk%2FOldsite%2Fmedia%2F34490424%2F2-38.png&f=1&nofb=1)

Vi skal finde hældningen af [[Sekant#Sekant|sekanten]], der går gennem de to punkter. Til dette kan vi bruge [[Linære Funktioner#To-punktsformlen|topunktsformlen]].

$$a=\frac{y_2-y_1}{x_2-x_{1}}= \frac{\Delta y}{\Delta x}$$

Vi kan nu sættespunkterne $(x_0,f(x_0))$ og $(x_0+h,f(x_0+h))$ ind i formlen

$$a=\frac{f(x_0+h)-f(x_0)}{\bcancel{x_0}+h-\bcancel{x_0}} \arrows a=\frac{f(x_0+h)-f(x_0)}{h}$$

For at finde hældningen i det første punkt $(x_0,f(x_0))$, skal vi minimere størrelsen af $h$. Det gør vi med en grænseværdi. Derfor er $f'(x)$ (den differentierede funktoin) defineret på denne måde:

$$f'(x_0) = 
\lim_{h\to 0} \left(  a=\frac{f(x_0+h)-f(x_0)}{h} \right)$$

Dette er nu funktionen for [[Sekant#Tangent|tangenten]] i $x_0$'s hældning (differentialkvotienten).

Hvis man skal differentiere den funktion i hånden på denne måde kan man bruge [[Tretrinsraketten]].




---




### Se også
- [[Differential Equations]]
- [[Differentialregning Regneregler]]
- [[Integraler]]
- [Differentialkvotient og differenskvotient](https://www.webmatematik.dk/lektioner/matematik-b/differentialregning/differenskvotient-og-differentialkvotient)

---
#matematik #differentialer